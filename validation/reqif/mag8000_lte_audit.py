#!/usr/bin/env python3
"""Deterministic end-to-end audit of the accepted MAG8000-LTE ReqIF baseline."""

import argparse
import collections
import hashlib
import re
import xml.etree.ElementTree as ET
from pathlib import Path


EXPECTED_SHA256 = "19eb5406e59c27417e57c25c097c948e8ab8b5f23d97a0692b51721ecfc8a5c8"
EXPECTED_GIT_BLOB = "fa29d4f0711864350a3c4127ad7be526c2b68628"
EMPTY_TEXT_IDS = {"adr-10361", "adr-10363"}

CT_CASES = {
    "CT-01": ["adr-10355", "adr-10356", "adr-10357", "adr-10358", "adr-10359", "adr-10334", "adr-10333"],
    "CT-02": ["adr-10325", "adr-10327", "adr-10328", "adr-10339", "adr-10343", "adr-10352"],
    "CT-03": ["adr-10335", "adr-10336", "adr-10337", "adr-10338", "adr-10340", "adr-10341"],
    "CT-04": ["adr-10351", "adr-10354", "adr-10380", "adr-10382", "adr-10385"],
    "CT-05": ["adr-10345", "adr-10346", "adr-10349", "adr-10350", "adr-10360", "adr-10364", "adr-10361", "adr-10363"],
    "CT-06": ["adr-10403"],
    "CT-07": ["adr-10389", "adr-10397", "adr-10342", "adr-10399", "adr-10404"],
    "CT-08": ["adr-10353", "adr-10341", "adr-10406", "adr-10347", "adr-10348"],
    "CT-09": ["adr-10383", "adr-10354", "adr-10351", "adr-10385", "adr-10336", "adr-10408", "adr-10386", "adr-10381", "adr-10407"],
    "CT-10": ["adr-10329", "adr-10331", "adr-10361", "adr-10363"],
    "CT-11": ["adr-10387", "adr-10403", "adr-10384", "adr-10388"],
    "CT-12": ["adr-10370", "adr-10372", "adr-10373", "adr-10384", "adr-10388", "adr-10367", "adr-10369"],
}

EXPECTED_REFERENCES = {
    "adr-10337": ("INVARIANT", "INV-ADR-10337-HOST-ALARM-PRESERVATION"),
    "adr-10389": ("INVARIANT", "INV-ADR-10389-MODULE-HOT-SWAP"),
    "adr-10397": ("INVARIANT", "INV-ADR-10397-TRANSMITTER-HOT-SWAP"),
}

EXPECTED_INTERACTIONS = {
    "INT-WEB-APP-GET-PARAMETER": ("EXT-WEB-APP", "EXTERNAL_TO_SYSTEM", "adr-10353"),
    "INT-MODULE-MQTT-ALARMS": ("EXT-MQTT-BROKER", "SYSTEM_TO_EXTERNAL", "adr-10341"),
    "INT-THINGSTREAM-CLOCK-SYNC": ("EXT-THINGSTREAM-SERVER", "EXTERNAL_TO_SYSTEM", "adr-10406"),
}


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def local_name(tag):
    return tag.rsplit("}", 1)[-1]


def direct_child(node, name):
    if node is None:
        return None
    return next((child for child in list(node) if local_name(child.tag) == name), None)


def descendants(node, name):
    if node is None:
        return []
    return [item for item in node.iter() if local_name(item.tag) == name]


def first_descendant(node, name):
    return next(iter(descendants(node, name)), None)


def normalized_xhtml(node):
    parts = []

    def ends_with(suffix):
        return "".join(parts).endswith(suffix)

    def collect(current):
        tag = local_name(current.tag)
        if tag == "br":
            parts.append("\n")
            return

        if tag in {"td", "th"} and parts and not ends_with("\n") and not ends_with("\t"):
            parts.append("\t")

        is_block = tag in {"div", "p", "li", "tr", "table", "ul", "ol"}
        if is_block and parts and not ends_with("\n"):
            parts.append("\n")

        if current.text:
            parts.append(current.text)

        for child in list(current):
            collect(child)
            if child.tail:
                parts.append(child.tail)

        if is_block and not ends_with("\n"):
            parts.append("\n")

    collect(node)
    raw = "".join(parts).replace("\r\n", "\n").replace("\r", "\n")
    lines = []
    for line in raw.split("\n"):
        normalized = "\t".join(" ".join(cell.split()) for cell in line.split("\t"))
        if normalized:
            lines.append(normalized)
    return "\n".join(lines)


def parse_values(parent, attribute_names, enum_names):
    result = {}
    values_node = direct_child(parent, "VALUES")
    if values_node is None:
        return result

    for value_node in list(values_node):
        definition = direct_child(value_node, "DEFINITION")
        if definition is None:
            continue
        reference = next(
            (child for child in list(definition) if local_name(child.tag).endswith("-REF")),
            None,
        )
        require(reference is not None, f"{local_name(parent.tag)} has an empty attribute definition reference")
        attribute_name = attribute_names.get(reference.text or "")
        require(attribute_name is not None, f"unknown attribute definition {reference.text!r}")

        if "THE-VALUE" in value_node.attrib:
            value = value_node.get("THE-VALUE", "")
        else:
            nested_value = direct_child(value_node, "THE-VALUE")
            if nested_value is not None:
                value = normalized_xhtml(nested_value)
            else:
                enum_container = direct_child(value_node, "VALUES")
                if enum_container is None:
                    value = ""
                else:
                    refs = descendants(enum_container, "ENUM-VALUE-REF")
                    value = " | ".join(enum_names.get(ref.text or "", ref.text or "") for ref in refs)

        require(attribute_name not in result, f"duplicate attribute {attribute_name!r}")
        result[attribute_name] = value
    return result


def parse_source(source_path):
    root = ET.parse(source_path).getroot()
    attribute_names = {}
    for item in root.iter():
        if local_name(item.tag).startswith("ATTRIBUTE-DEFINITION-") and item.get("IDENTIFIER") and item.get("LONG-NAME"):
            attribute_names[item.get("IDENTIFIER")] = item.get("LONG-NAME")

    object_type_names = {
        item.get("IDENTIFIER"): item.get("LONG-NAME")
        for item in descendants(root, "SPEC-OBJECT-TYPE")
    }
    relation_type_names = {
        item.get("IDENTIFIER"): item.get("LONG-NAME")
        for item in descendants(root, "SPEC-RELATION-TYPE")
    }
    enum_names = {
        item.get("IDENTIFIER"): item.get("LONG-NAME", item.get("IDENTIFIER", ""))
        for item in descendants(root, "ENUM-VALUE")
    }

    objects = {}
    for item in descendants(root, "SPEC-OBJECT"):
        object_id = item.get("IDENTIFIER")
        require(object_id, "source SpecObject has no IDENTIFIER")
        type_node = direct_child(item, "TYPE")
        type_ref = first_descendant(type_node, "SPEC-OBJECT-TYPE-REF")
        require(type_ref is not None, f"source object {object_id} has no type reference")
        require(object_id not in objects, f"duplicate source SpecObject ID {object_id}")
        objects[object_id] = {
            "type": object_type_names.get(type_ref.text or ""),
            "attributes": parse_values(item, attribute_names, enum_names),
        }

    relations = {}
    for item in descendants(root, "SPEC-RELATION"):
        relation_id = item.get("IDENTIFIER")
        require(relation_id, "source SpecRelation has no IDENTIFIER")
        type_node = direct_child(item, "TYPE")
        type_ref = first_descendant(type_node, "SPEC-RELATION-TYPE-REF")
        source_ref = first_descendant(direct_child(item, "SOURCE"), "SPEC-OBJECT-REF")
        target_ref = first_descendant(direct_child(item, "TARGET"), "SPEC-OBJECT-REF")
        require(type_ref is not None and source_ref is not None and target_ref is not None,
                f"malformed source relation {relation_id}")
        require(relation_id not in relations, f"duplicate source SpecRelation ID {relation_id}")
        relations[relation_id] = {
            "type": relation_type_names.get(type_ref.text or ""),
            "source": source_ref.text or "",
            "target": target_ref.text or "",
            "attributes": parse_values(item, attribute_names, enum_names),
        }

    specifications = [
        item for item in descendants(root, "SPECIFICATION")
        if item.get("LONG-NAME") == "feature specification baseline 4"
    ]
    require(len(specifications) == 1, "expected exactly one feature specification baseline 4")
    hierarchy_nodes = descendants(specifications[0], "SPEC-HIERARCHY")
    hierarchy_refs = []
    for hierarchy_node in hierarchy_nodes:
        object_ref = first_descendant(direct_child(hierarchy_node, "OBJECT"), "SPEC-OBJECT-REF")
        if object_ref is not None:
            hierarchy_refs.append(object_ref.text or "")

    return objects, relations, hierarchy_nodes, hierarchy_refs


def parse_report(report_path):
    root = ET.parse(report_path).getroot()
    object_nodes = descendants(direct_child(root, "OBJECTS"), "OBJECT")
    relation_nodes = descendants(direct_child(root, "RELATIONS"), "RELATION")
    objects = {item.get("source_id"): item for item in object_nodes}
    relations = {item.get("id"): item for item in relation_nodes}
    require(len(objects) == len(object_nodes), "duplicate source_id in import report")
    require(len(relations) == len(relation_nodes), "duplicate relation ID in import report")
    return root, objects, relations


def parse_report_attributes(report_item):
    attributes_node = direct_child(report_item, "ATTRIBUTES")
    if attributes_node is None:
        return {}
    result = {}
    for item in descendants(attributes_node, "ATTRIBUTE"):
        name = item.get("name")
        require(name is not None, "report ATTRIBUTE has no name")
        require(name not in result, f"duplicate report attribute {name!r}")
        result[name] = item.text or ""
    return result


def check_requirements_analysis(path):
    root = ET.parse(path).getroot()
    require(local_name(root.tag) == "REQUIREMENTS_ANALYSIS", "wrong RequirementsAnalysis.xml root")
    require(root.get("id") == "RA-MAG8000-LTE-BL4", "unexpected RequirementsAnalysis ID")
    require(root.get("system_name") == "MAG8000-LTE", "unexpected system_name")

    external_systems = {item.get("id"): item for item in descendants(root, "EXTERNAL_SYSTEM")}
    interactions = {item.get("id"): item for item in descendants(root, "SYSTEM_INTERACTION")}
    invariants = {item.get("id"): item for item in descendants(root, "INVARIANT")}

    require(len(external_systems) == 3, f"expected 3 external systems, found {len(external_systems)}")
    require(len(interactions) == 3, f"expected 3 C1 interactions, found {len(interactions)}")
    require(len(invariants) == 3, f"expected 3 existing invariants, found {len(invariants)}")
    require(not descendants(root, "ACTOR"), "unconfirmed ACTOR was added")
    require(not descendants(root, "USE_CASE"), "unconfirmed USE_CASE was added")

    for interaction_id, (external_ref, direction, source_id) in EXPECTED_INTERACTIONS.items():
        item = interactions.get(interaction_id)
        require(item is not None, f"missing interaction {interaction_id}")
        require(item.get("external_system_ref") == external_ref, f"wrong external system for {interaction_id}")
        require(item.get("direction") == direction, f"wrong direction for {interaction_id}")
        require(external_ref in external_systems, f"unresolved external_system_ref on {interaction_id}")
        purpose = direct_child(item, "PURPOSE")
        require(purpose is not None and source_id in "".join(purpose.itertext()),
                f"missing source traceability on {interaction_id}")

    for source_id, (_, invariant_id) in EXPECTED_REFERENCES.items():
        item = invariants.get(invariant_id)
        require(item is not None, f"missing existing invariant {invariant_id}")
        require(source_id in "".join(item.itertext()), f"missing source traceability on {invariant_id}")

    ids = [item.get("id") for item in root.iter() if item.get("id")]
    require(len(ids) == len(set(ids)), "duplicate IDs in RequirementsAnalysis.xml")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--requirements-before", required=True)
    parser.add_argument("--requirements-after", required=True)
    parser.add_argument("--inventory", required=True)
    parser.add_argument("--semantic-model", required=True)
    parser.add_argument("--test-scope", required=True)
    parser.add_argument("--c1-output", required=True)
    args = parser.parse_args()

    source_bytes = Path(args.source).read_bytes()
    source_sha256 = hashlib.sha256(source_bytes).hexdigest()
    git_blob_sha = hashlib.sha1(
        b"blob " + str(len(source_bytes)).encode("ascii") + b"\0" + source_bytes
    ).hexdigest()
    require(source_sha256 == EXPECTED_SHA256, f"unexpected ReqIF SHA-256: {source_sha256}")
    require(git_blob_sha == EXPECTED_GIT_BLOB, f"unexpected ReqIF Git blob SHA: {git_blob_sha}")

    source_objects, source_relations, source_hierarchy, source_hierarchy_refs = parse_source(args.source)
    report_root, report_objects, report_relations = parse_report(args.report)

    require(len(source_objects) == 102, f"expected 102 source SpecObjects, found {len(source_objects)}")
    require(len(source_relations) == 26, f"expected 26 source SpecRelations, found {len(source_relations)}")
    require(len(source_hierarchy) == 102, f"expected 102 hierarchy nodes, found {len(source_hierarchy)}")
    require(len(source_hierarchy_refs) == 102, f"expected 102 hierarchy object references, found {len(source_hierarchy_refs)}")
    require(len(report_objects) == 102, f"expected 102 audited objects, found {len(report_objects)}")
    require(len(report_relations) == 26, f"expected 26 audited relations, found {len(report_relations)}")

    expected_report_counts = {
        "total_objects": "102",
        "selected_objects": "102",
        "imported_objects": "0",
        "referenced_objects": "3",
        "skipped_objects": "99",
        "rejected_objects": "0",
        "blocked_objects": "0",
        "out_of_scope_objects": "0",
        "total_relations": "26",
        "unresolved_relations": "26",
        "mapped_relations": "0",
    }
    for name, expected in expected_report_counts.items():
        require(report_root.get(name) == expected,
                f"report {name}: expected {expected}, found {report_root.get(name)!r}")

    blocking_errors = direct_child(report_root, "BLOCKING_ERRORS")
    require(blocking_errors is not None and not descendants(blocking_errors, "ERROR"),
            "import report contains blocking errors")

    source_foreign_ids = {}
    feature_ids = set()
    heading_ids = set()
    for source_id, source_object in source_objects.items():
        report_object = report_objects.get(source_id)
        require(report_object is not None, f"source object {source_id} missing from report")
        require(report_object.get("selected") == "true", f"source object {source_id} was not selected")
        require(report_object.get("source_type") == source_object["type"],
                f"source type changed for {source_id}")

        source_attributes = source_object["attributes"]
        report_attributes = parse_report_attributes(report_object)
        require(source_attributes == report_attributes, f"source attributes changed for {source_id}")

        foreign_id = source_attributes.get("ReqIF.ForeignID", "")
        require(foreign_id, f"source object {source_id} has no ReqIF.ForeignID")
        require(foreign_id not in source_foreign_ids, f"duplicate Polarion ForeignID {foreign_id}")
        require(report_object.get("foreign_id") == foreign_id, f"ForeignID changed for {source_id}")
        source_foreign_ids[foreign_id] = source_id

        if source_object["type"] == "Feature":
            feature_ids.add(foreign_id)
        elif source_object["type"] == "Heading":
            heading_ids.add(foreign_id)
        else:
            raise SystemExit(f"FAIL: unexpected ReqIF object type {source_object['type']!r}")

    require(len(feature_ids) == 70, f"expected 70 Feature IDs, found {len(feature_ids)}")
    require(len(heading_ids) == 32, f"expected 32 Heading IDs, found {len(heading_ids)}")
    require(feature_ids | heading_ids == set(source_foreign_ids),
            "Feature/Heading IDs do not cover the complete source corpus")

    type_counts = collections.Counter(item.get("source_type") for item in report_objects.values())
    require(type_counts == {"Feature": 70, "Heading": 32},
            f"unexpected ReqIF object type counts: {dict(type_counts)}")

    for source_id in EMPTY_TEXT_IDS:
        object_id = source_foreign_ids.get(source_id)
        require(object_id is not None, f"missing empty-text Feature {source_id}")
        attrs = parse_report_attributes(report_objects[object_id])
        if source_id == "adr-10361":
            require("ReqIF.Text" not in attrs,
                    "adr-10361: absent ReqIF.Text was not preserved")
        else:
            require("ReqIF.Text" in attrs and attrs["ReqIF.Text"] == "",
                    "adr-10363: empty XHTML ReqIF.Text was not preserved")
        require(attrs.get("ReqIF.ChapterName", "") != "", f"{source_id}: ReqIF.ChapterName was lost")

    text_count = 0
    for foreign_id in feature_ids:
        attrs = parse_report_attributes(report_objects[source_foreign_ids[foreign_id]])
        if foreign_id != "adr-10361":
            require("ReqIF.Text" in attrs, f"{foreign_id}: ReqIF.Text attribute is missing")
        if attrs.get("ReqIF.Text", "").strip():
            text_count += 1
        elif foreign_id not in EMPTY_TEXT_IDS:
            raise SystemExit(f"FAIL: unexpected empty ReqIF.Text for {foreign_id}")
    require(text_count == 68, f"expected 68 non-empty Feature ReqIF.Text values, found {text_count}")

    for foreign_id, (target, grace_id) in EXPECTED_REFERENCES.items():
        object_id = source_foreign_ids.get(foreign_id)
        require(object_id is not None, f"missing referenced source Feature {foreign_id}")
        item = report_objects[object_id]
        require(item.get("status") == "REFERENCED", f"{foreign_id} was not referenced")
        require(item.get("grace_target") == target, f"{foreign_id} mapped to the wrong GRACE target")
        require(item.get("grace_id") == grace_id, f"{foreign_id} references the wrong GRACE ID")

    for foreign_id, object_id in source_foreign_ids.items():
        if foreign_id not in EXPECTED_REFERENCES:
            require(report_objects[object_id].get("status") == "SKIPPED",
                    f"{foreign_id} received an unapproved GRACE mapping")

    inventory = Path(args.inventory).read_text(encoding="utf-8")
    semantic_model = Path(args.semantic_model).read_text(encoding="utf-8")
    test_scope = Path(args.test_scope).read_text(encoding="utf-8")
    for foreign_id in feature_ids | heading_ids:
        require(foreign_id in inventory, f"{foreign_id} is missing from reqif-inventory.md")
    for foreign_id in feature_ids:
        require(foreign_id in semantic_model, f"{foreign_id} is missing from semantic-model.md")

    declared_cases = set(re.findall(r"^\|\s*(CT-\d{2})\.", test_scope, re.MULTILINE))
    require(declared_cases == {f"CT-{index:02d}" for index in range(1, 14)},
            f"test scope CT groups changed: {sorted(declared_cases)}")

    for case_id, source_ids in CT_CASES.items():
        for foreign_id in source_ids:
            require(foreign_id in feature_ids, f"{case_id}: missing source Feature {foreign_id}")
            attrs = parse_report_attributes(report_objects[source_foreign_ids[foreign_id]])
            if foreign_id == "adr-10361":
                require("ReqIF.Text" not in attrs,
                        f"{case_id}: {foreign_id} absent ReqIF.Text changed")
            elif foreign_id == "adr-10363":
                require("ReqIF.Text" in attrs and attrs["ReqIF.Text"] == "",
                        f"{case_id}: {foreign_id} empty XHTML changed")
            else:
                require(attrs.get("ReqIF.Text", "").strip() != "",
                        f"{case_id}: {foreign_id} has no preserved ReqIF.Text")
        print(f"PASS {case_id}: {len(source_ids)} source Feature records retained without semantic invention")

    source_object_ids = set(source_objects)
    require(set(source_relations) == set(report_relations),
            "source relation IDs differ from the audit report")
    for relation_id, source_relation in source_relations.items():
        report_relation = report_relations[relation_id]
        require(source_relation["type"] == "fulfills",
                f"{relation_id}: expected fulfills, found {source_relation['type']!r}")
        require(report_relation.get("type_name") == source_relation["type"],
                f"{relation_id}: relation type changed")
        require(report_relation.get("source_ref") == source_relation["source"],
                f"{relation_id}: source endpoint changed")
        require(report_relation.get("target_ref") == source_relation["target"],
                f"{relation_id}: target endpoint changed")
        require(report_relation.get("status") == "MISSING_TARGET",
                f"{relation_id}: missing target was not diagnosed")
        require(source_relation["source"] in source_object_ids,
                f"{relation_id}: source endpoint is absent from source corpus")
        require(source_relation["target"] not in source_object_ids,
                f"{relation_id}: target unexpectedly exists in source corpus")
        require(parse_report_attributes(report_relation) == source_relation["attributes"],
                f"{relation_id}: relation attributes changed")
    print("PASS CT-13: all 26 fulfills relations retained with exact endpoints and MISSING_TARGET status")

    hierarchy_report = direct_child(report_root, "SPECIFICATION_HIERARCHY")
    require(hierarchy_report is not None, "report has no specification hierarchy")
    report_hierarchy_nodes = descendants(hierarchy_report, "NODE")
    report_hierarchy_refs = [
        item.get("source_object_ref")
        for item in report_hierarchy_nodes
        if item.get("source_object_ref")
    ]
    require(len(report_hierarchy_nodes) == len(source_hierarchy),
            "specification hierarchy node count changed")
    require(collections.Counter(report_hierarchy_refs) == collections.Counter(source_hierarchy_refs),
            "specification hierarchy references changed")

    before = Path(args.requirements_before).read_bytes()
    after = Path(args.requirements_after).read_bytes()
    require(before == after, "RequirementsAnalysis.xml changed during the audit import")
    check_requirements_analysis(args.requirements_after)

    c1_output = Path(args.c1_output)
    require(c1_output.is_file() and c1_output.stat().st_size > 0,
            "GRACE-ARP did not produce a C1 workspace")
    c1_text = c1_output.read_text(encoding="utf-8")
    require("systemContext " in c1_text, "generated workspace contains no C1 systemContext view")

    print("PASS: accepted source baseline SHA-256 and Git blob SHA verified")
    print("PASS: 70 Feature, 32 Heading, all 102 attribute sets, and all 102 hierarchy nodes retained")
    print("PASS: three existing invariants referenced; 99 source objects skipped without invented GRACE semantics")
    print("PASS: three existing C1 interactions remain traceable")
    print("PASS: RequirementsAnalysis.xml is byte-for-byte unchanged")
    print("PASS: GRACE-ARP generated the C1 workspace")


if __name__ == "__main__":
    main()
