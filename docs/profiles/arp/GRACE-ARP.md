# GRACE Architecture Representation Profile (GRACE-ARP)

**Status:** HUMAN_APPROVED — approved by the project owner on 2026-10-27 as the complete normative GRACE-ARP profile.

## 1. Purpose and authority

GRACE-ARP defines how the meaning already established by GRACE artifacts is represented as C4 views and emitted as Structurizr DSL.

**GRACE remains the sole source of truth.** C4 and Structurizr are derived representations for human understanding and architectural control. They must not introduce, replace, or silently amend requirements, architectural decisions, responsibilities, or relationships established by GRACE.

GRACE-ARP supplements GRACE only with rules needed to make the derived representation deterministic and verifiable. If a required fact is missing or ambiguous, the tool must report that condition rather than invent the fact.

Before authoring or editing source artifacts for a GRACE-ARP project, authors and AI agents must follow [GRACE-ARP-INSTRUCTIONS.md](../../../GRACE-ARP-INSTRUCTIONS.md). The guide distinguishes base GRACE requirements from mandatory GRACE-ARP conventions and provides a pre-validation checklist.

## 2. Scope

The initial scope is limited to C1, C2, and C3.

C4 Code is outside the initial scope.

### Target-model references

The official C4 documentation defines the target abstractions and diagram scope; Structurizr documentation defines DSL behavior. These references do **not** supply, override, or amend facts from GRACE:

- C1 — System Context: https://c4model.com/diagrams/system-context
- C2 — Container: https://c4model.com/diagrams/container
- C3 — Component diagram: https://c4model.com/diagrams/component
- C4 Component abstraction: https://c4model.com/abstractions/component
- Structurizr implied relationships: https://docs.structurizr.com/dsl/cookbook/implied-relationships/
- Structurizr element styles: https://docs.structurizr.com/dsl/cookbook/element-styles/

The implementation tools for this repository are separate from the normative semantics of this profile. The selected implementation language is Rust.

## 3. Source mapping

**Mandatory normative requirement:** every GRACE-ARP-conforming project, artifact interpretation, validator, and renderer must follow the source mapping below. This mapping is binding, not advisory.

| C4 view | GRACE source | Responsibility of the source |
|---|---|---|
| C1 — System Context | `RequirementsAnalysis.xml` | The system context, people/actors, external systems, and interactions defined by the requirements |
| C2 — Container | `Technology.xml` + `DevelopmentPlan.xml` | The technology stack and upper-level architecture, including architectural boundaries and interactions |
| C3 — Component | Module Contracts | Component-level responsibilities and relationships expressed by Module Contracts |

The source mapping above is mandatory. It must be applied consistently during artifact interpretation, validation, and generation.

- `Technology.xml` and `DevelopmentPlan.xml` must not be used to silently supplement C1. If architecture work reveals an external system or interaction missing from the requirements, the requirements must be resolved through the GRACE process.
- C2 may provide the architectural context in which a C3 view is displayed; the C3 semantics remain those established by the source assigned to C3 in the mapping above.

## 4. C1 — System Context

1. The source for C1 is `RequirementsAnalysis.xml`, as required by the mandatory source mapping in § 3.
2. GRACE § 4.1 establishes that this artifact contains the system goal, actors, Actor–Action–Goal use cases, business processes, entities, states, rules, invariants, error scenarios, boundary cases, result criteria, and links between these elements.
3. The GRACE example explicitly models `ACTOR`, `USE_CASE`, `ACTION`, `GOAL`, and `STARTS_PROCESS`. Base GRACE does not prescribe a dedicated XML element or schema for the C4 software-system element or external software-system participants. This profile adds a specific machine-readable convention for C1 below; that convention is a GRACE-ARP requirement, not a claim that the base GRACE methodology already defines these elements.
4. The generator must not invent people, external systems, or interactions from names, technology choices, vendor mentions, or later-stage artifacts.
5. If an actor is referenced by at least one `USE_CASE/ACTOR` link, generate one aggregated C4 relationship from that `Person` to the software system in scope. Generate no more than one such relationship per actor, regardless of the number of linked use cases.
6. Use a generic description of the actor's interaction with the system; do not enumerate or merge individual use-case descriptions into the relationship label. The individual scenarios remain represented in GRACE and are not replaced by the aggregate relationship.
7. `STARTS_PROCESS` links a use case to a business process; it must not, by itself, be reinterpreted as a direct C4 relationship between a person and the software system.
8. A declared `ACTOR` that is not referenced by any `USE_CASE/ACTOR` link must produce a `Warning` diagnostic. This condition alone does not justify creating a person-to-system relationship.
9. An external software system may be represented in C1 only when it is declared by a top-level `EXTERNAL_SYSTEM` element in `RequirementsAnalysis.xml` and at least one valid top-level `SYSTEM_INTERACTION` references it. The declaration provides its external classification and stable identity; the interaction provides explicit evidence of its interaction with the system in scope. Vendor, product, technology, or later-stage artifact mentions do not substitute for these declarations.
10. The C1 XML convention is mandatory for this profile: the in-scope software system is the single system described by the `REQUIREMENTS_ANALYSIS` artifact; `EXTERNAL_SYSTEM` declares an external system; and `SYSTEM_INTERACTION` declares a directed interaction between the in-scope system and that external system. The exact encoding is specified in the subsection below. This is a GRACE-ARP requirement and does not alter or claim to redefine base GRACE.
11. Use the optional `system_name` attribute on the root `REQUIREMENTS_ANALYSIS` element as the explicit C1 software-system display name when present and non-empty. If it is absent, use the project repository name as a display-only fallback. The repository name does not become a GRACE-defined system identity or architecture fact. If neither name is available, report a diagnostic rather than inventing a name. `System under specification` is not an approved fallback.
12. If a participant, system identity, or relationship required by the selected C1 representation cannot be derived unambiguously from the requirements, the generator must report the gap rather than guess.

### C1 external-system XML convention

This subsection defines a mandatory GRACE-ARP input convention for deterministic C1 generation. It extends the XML representation used by this profile; it does not modify the base GRACE methodology or claim that these elements are already defined by base GRACE.

1. Each `REQUIREMENTS_ANALYSIS` artifact describes exactly one software system in scope. Its existing `id` identifies the requirements artifact, not the software system. The optional root attribute `system_name` supplies the system's explicit display name; if present, it must contain non-whitespace text. If omitted, the project repository name is used as the display-only fallback.
2. `EXTERNAL_SYSTEM` must be a direct child of `REQUIREMENTS_ANALYSIS`. Its required, unique `id` identifies that external system; its non-empty text content is its display name. The element's name explicitly classifies the participant as an external software system.
3. `SYSTEM_INTERACTION` must be a direct child of `REQUIREMENTS_ANALYSIS` and have a required, unique `id`, a required `external_system_ref`, and a required `direction`.
4. `external_system_ref` must resolve to exactly one `EXTERNAL_SYSTEM/@id` declared in the same `REQUIREMENTS_ANALYSIS` artifact. It must not refer to the root artifact, an actor, a use case, or an undeclared participant.
5. `direction` must be exactly one of:
   - `SYSTEM_TO_EXTERNAL` — the described interaction is directed from the in-scope system to the referenced external system.
   - `EXTERNAL_TO_SYSTEM` — the described interaction is directed from the referenced external system to the in-scope system.
   The direction defines the relationship represented in C1; it does not assert that no return traffic exists.
6. Each `SYSTEM_INTERACTION` must contain one non-empty `PURPOSE` describing the interaction. The same external system may be referenced by multiple interactions.
7. If distinct interactions must be represented in both directions, represent them as separate `SYSTEM_INTERACTION` elements with different IDs and the corresponding `direction` values.
8. All `id` values in the artifact must remain unique. An empty `system_name` when present, an empty `EXTERNAL_SYSTEM` display name, an unresolved `external_system_ref`, a missing or invalid `direction`, or a missing/empty `PURPOSE` is a blocking validation error.
9. An `EXTERNAL_SYSTEM` without any valid `SYSTEM_INTERACTION` referencing it does not qualify for rendering in C1. The validator must emit a non-blocking `Warning` for the unused declaration; generation may continue, but the external system must not be rendered. The validator must not invent an interaction.
10. A valid `SYSTEM_INTERACTION` is the evidence for the relationship between the in-scope system and the referenced external system. The renderer must not infer additional relationships from the external system's name, its `PURPOSE`, or other artifact content.

Example:

```xml
<REQUIREMENTS_ANALYSIS id="RA-ORDERFLOW" system_name="OrderFlow">
    <PROJECT_GOAL id="GOAL-001">
        Обеспечить обработку заказов.
    </PROJECT_GOAL>

    <EXTERNAL_SYSTEM id="SYS-PAYMENTS">Платёжный провайдер</EXTERNAL_SYSTEM>

    <SYSTEM_INTERACTION
        id="INT-PAYMENT-AUTH"
        external_system_ref="SYS-PAYMENTS"
        direction="SYSTEM_TO_EXTERNAL">
        <PURPOSE>Авторизация платежа</PURPOSE>
    </SYSTEM_INTERACTION>
</REQUIREMENTS_ANALYSIS>
```

## 5. C2 — Container

In C4, “Container” is terminology of the target representation, not a required GRACE entity or XML tag. The following rules define how GRACE-ARP selects C2 elements from the approved facts in `Technology.xml` and `DevelopmentPlan.xml`. They define a C4 mapping; they do not redefine the native meaning of GRACE modules, classes, or services.

1. Create a C2 element only when the approved `Technology.xml` and `DevelopmentPlan.xml` unambiguously establish that it represents a standalone application or a data store within the system in scope.
2. A GRACE module does not automatically become a C2 element. A class does not automatically become a C2 element. A service may be represented at C2 when the approved architecture establishes it as a standalone application or executable unit.
3. Multiple GRACE modules may be represented within the same C2 element. The generator must not assume that each module requires its own C2 element.
4. A technology entry characterizes an architectural element or an already-established interaction only when the association is supported by the approved GRACE artifacts. A technology entry alone does not establish a C2 element.
5. If the approved artifacts do not establish the required architectural boundary unambiguously, the validator must report the missing or ambiguous mapping. The generator must not infer, merge, or split C2 elements to fill the gap.
6. These rules do **not** mandate a GRACE entity named `Container` or prescribe a particular XML element, attribute, or schema. The required architectural facts may be expressed using GRACE's existing means, provided their meaning is machine-readable and unambiguous.

## 6. C3 — Component

1. Module Contracts are the mandatory GRACE source for C3 component semantics and relationship evidence, as established by the source mapping in § 3.
2. For this profile, each GRACE module represented in a C3 view maps to one C4 Component. This is a GRACE-ARP mapping rule; it does not claim that base GRACE defines a C4 Component entity.
3. A Module Contract is not itself a C4 Component. All Module Contracts explicitly associated with the same GRACE module provide evidence for that module's component; separate contract IDs must not create separate components.
4. C3 relationships are rendered only when Module Contract semantics establish the relationship and both endpoint modules map unambiguously to C3 components under the rules in § 7.1.
5. Each rendered component and relationship must remain traceable to the Module Contract evidence that supports it.

### 6.1. Module identity, C2 placement, and relationship endpoints

GRACE defines the semantic graph `requirement → business process → module → Module Contract → function contract → semantic code block → test → trace → log event` (§§ 3 and 19). GRACE-ARP must use this graph rather than inventing a parallel identity model.

1. A Module Contract must be associated with its GRACE module through stable IDs and explicit, machine-readable GRACE traceability. Matching ID-name fragments, filenames, prose similarity, or document proximity is insufficient. If ownership cannot be established unambiguously, the validator must report the missing or ambiguous mapping.
2. Each GRACE module included in a C3 view is represented by one C3 component identified from that module's stable identity. Multiple Module Contracts explicitly associated with the same module support the same component and must not be split into components merely because they have separate IDs.
3. Each C3 view is scoped to one selected C2 element. A module component may be placed within that C2 only when the approved architecture explicitly establishes that the functionality represented by the module belongs in, and is executed within, that C2.
4. Placement evidence must follow the explicit traceability path `Module Contract → GRACE module → architectural placement → C2`. Associations must use stable IDs and explicit, machine-readable architectural facts. Module names, dependency links, technology choices, filenames, document proximity, and textual similarity do not by themselves establish placement.
5. A GRACE module may be represented in more than one C2-specific C3 view only when the approved architecture explicitly establishes that the corresponding functionality is executed in each of those C2 elements. The generator must not infer multiple placement from a dependency, a shared name, or a relationship to another element.
6. A module's use of a data store does not place its C3 component inside that data store. A data-access relationship is not placement evidence. Placement within a data store requires separate, explicit architectural evidence that the represented functionality is executed there.
7. If placement is missing or ambiguous, the validator must report the unresolved or ambiguous mapping. The generator must not invent a placement relationship or claim the affected C3 view is complete. Conflicting contract facts must also be reported rather than silently resolved.
8. **Canonical placement encoding (mandatory GRACE-ARP convention):** In `DevelopmentPlan.xml`, each placement of a module within a C2 element must be represented by an empty `PLACEMENT` child of that module, with a required `c2_ref` attribute that identifies the C2 element by its stable ID. The referenced ID must resolve to exactly one C2 element established by the approved architecture under § 5. This convention extends the XML representation for GRACE-ARP; it does not claim that base GRACE already defines the `PLACEMENT` element.
   
   Example:
   
   ```xml
   <DEVELOPMENT_PLAN id="DP-ORDERFLOW">
       <MODULE id="MOD-ORDER">
           <RESPONSIBILITY>Управлять жизненным циклом заказа.</RESPONSIBILITY>
           <PLACEMENT c2_ref="APP-API"/>
       </MODULE>
   </DEVELOPMENT_PLAN>
   ```
   
   The value `APP-API` is the stable ID of a C2 element established by the approved architecture, not a name that the generator may infer. Each `PLACEMENT` records one module-to-C2 placement. A module explicitly executed in multiple C2 elements must have one `PLACEMENT` child for each distinct C2 ID. Repeating the same module/C2 pair is invalid. A missing placement for a module required in the selected C3 view, an empty or unresolved `c2_ref`, a reference that resolves to zero or multiple C2 elements, or a duplicate module/C2 pair is a blocking `Error`. The generator must not infer placement from module names, dependencies, technology choices, or data-store usage.

9. **Canonical Module Contract ownership encoding (mandatory GRACE-ARP convention):** Each `MODULE_CONTRACT` must contain exactly one `GRACE_MODULE ref="MOD-X"` child inside `LINKS`. The referenced ID must resolve to exactly one `MODULE/@id` in `DevelopmentPlan.xml`. This link identifies the GRACE module described by the contract; it does not create a C3 relationship. Missing, empty, unresolved, or multiple `GRACE_MODULE` links are blocking validation errors.

### 6.2. Contract visibility and traceability in C3

1. Module Contracts remain the source of C3 component semantics and relationship evidence under § 3. This rule does not change the mandatory C3 source mapping.
2. Function Contracts refine the approved architecture and Module Contracts. They must not be rendered as separate C3 components or as C4 relationships merely because they have their own IDs.
3. The description of a rendered component must provide access to the Module Contract evidence supporting that component. Where GRACE's explicit links associate Function Contracts with that evidence, those Function Contracts must also be accessible from the component description or through links to their source XML. The renderer may show contract IDs and concise descriptions inline, provide direct source links, or combine both approaches.
4. Contract associations must be based on stable IDs and explicit GRACE links. The renderer must not infer associations from filenames, name fragments, text similarity, or directory layout.
5. Contract descriptions and links provide detail and traceability; they do not create additional C3 nodes or architectural relationships and do not change the module-to-component mapping defined in § 6.1.
6. The source XML remains authoritative. A rendered description must not replace, silently rewrite, or contradict the linked contract.

### 6.3. Mental scenarios and check criteria

GRACE includes mental tests at more than one level. Architecture-level mental tests may be represented in `DevelopmentPlan.xml`; later mental scenarios and check criteria validate the approved contract chain before implementation and during verification.

1. Mental scenarios and check criteria must remain traceable to the requirements, architecture, and relevant Module/Function Contracts that justify them.
2. They verify or challenge the existing graph; they do not independently create or amend C1–C3 elements, responsibilities, or relationships.
3. If a scenario or criterion reveals a defect in requirements, architecture, or a contract, the discrepancy must be escalated to the responsible upstream GRACE artifact and resolved through the GRACE approval process.
4. The generator/validator must preserve the distinction between architecture-level scenarios in `DevelopmentPlan.xml` and downstream contract-derived verification criteria. Their presence in an artifact does not change the mandatory C1–C3 source mapping in § 3.

## 7. Relationship semantics and Structurizr generation

### 7.1. Relationship semantics by view

A relationship may be rendered only when the assigned GRACE source establishes its meaning and its endpoints can be mapped unambiguously to elements in that C4 view. A reference, co-occurrence, shared identifier fragment, or proximity in XML is not sufficient evidence by itself.

#### C1 — System Context

- A `USE_CASE` → `ACTOR` reference establishes actor participation in that use case. If an actor is referenced by at least one use case, generate one aggregated relationship from that `Person` to the software system, regardless of the number of linked use cases. Use a generic interaction description rather than enumerating individual scenarios on the relationship. This is an approved GRACE-ARP mapping rule, not a claim that GRACE itself defines a direct actor-to-system relationship.
- `STARTS_PROCESS` links a use case to a business process. It must not, by itself, be rendered as a C4 relationship between the person and the software system.
- C1 external-system representation uses the mandatory GRACE-ARP convention in § 4: `EXTERNAL_SYSTEM` declares the external system, and `SYSTEM_INTERACTION` references it through `external_system_ref` and establishes direction through `direction`. The interaction must include a non-empty `PURPOSE`; only referenced external-system declarations qualify for rendering.

#### C2 — Container

- Relationships may be derived from architectural relationships described by `DevelopmentPlan.xml`, including dependencies, data flows, and external integrations, only when the approved architecture explicitly establishes the relationship's meaning and direction and both endpoints map unambiguously to elements represented in the selected C2 view.
- The meaning, direction, and endpoint identities must be supported by explicit, machine-readable architectural facts. The generator must not infer direction from names, element order, technology choices, textual proximity, source-code dependencies, or data-store usage.
- For relationships whose two endpoints are internal C2 elements, the allowed `DIRECTION` value is determined by the endpoint types established by the source artifacts:

  | Source endpoint | Target endpoint | Required `DIRECTION` |
  | --- | --- | --- |
  | Application (`APPLICATION` with `TYPE=standalone-application`) | Application (`APPLICATION` with `TYPE=standalone-application`) | `APP_TO_APP` |
  | Application (`APPLICATION` with `TYPE=standalone-application`) | Data store (`DATA_STORE`) | `APP_TO_DATA_STORE` |
  | Data store (`DATA_STORE`) | Application (`APPLICATION` with `TYPE=standalone-application`) | `DATA_STORE_TO_APP` |
  | Data store (`DATA_STORE`) | Data store (`DATA_STORE`) | `DATA_STORE_TO_DATA_STORE` |

- For a relationship between an in-scope application and an external system, `APP_TO_EXTERNAL` means the application is the source and external system the target; `EXTERNAL_TO_APP` means the external system is the source and application the target.
- Relationships between a data store and an external system, in either direction, are not mapped by this profile and must be rejected as blocking errors. Relationships between two external systems are also not rendered in C2 because they do not connect to an in-scope C2 element.
- A `KIND=external-integration` relationship must have an explicitly declared external-system endpoint and an in-scope application endpoint; it cannot describe a relationship between two internal C2 elements or a data-store/external-system pair.
- The `DIRECTION` value must exactly match the endpoint types and orientation. A missing, unknown, incompatible, or ambiguous direction is a blocking error, and the relationship must not be rendered.
- The presence of a module, dependency, data flow, or integration in the architecture graph does not by itself prove that its endpoints are elements represented in C2. If the relationship meaning, direction, or either endpoint is missing, ambiguous, or conflicting, the validator must diagnose the issue and the relationship must not be rendered.
- A technology listed in `Technology.xml` may characterize an element or an already-established interaction, but a technology entry alone does not establish a relationship.

#### C3 — Component

- Module Contracts are the source of C3 relationship semantics, as required by § 3.
- A `USES ref="MOD-X"` relationship in a Module Contract produces a directed C3 relationship from the C3 component for the GRACE module explicitly associated with that contract to the C3 component for `MOD-X`, provided both module identities resolve unambiguously.
- The `USES` target must resolve to a GRACE module for the relationship to be rendered in C3. A `USES` reference to a technology or other non-module element, such as `PostgreSQL-18`, does not by itself produce a C3 component relationship.
- Repeated `USES` declarations for the same ordered source-module/target-module pair produce one C3 relationship. The generated relationship must retain provenance to all Module Contracts that support it.
- Links such as `IMPLEMENTS` to a business process, `PRESERVES` to an invariant, references to requirements/processes/invariants, and Function Contract links to Module Contracts are semantic or traceability links, not C3 architectural arrows.
- If the source contract's owning module or the target module cannot be mapped unambiguously, the validator must report the missing or ambiguous mapping and the renderer must not invent a relationship. Filenames, matching name fragments, and dependencies found only in source code are not substitutes for explicit GRACE links.

#### GRACE semantic and traceability links

- A `STEP ref="..."` inside a business-process definition expresses process structure; it does not by itself establish a C1, C2, or C3 architectural relationship.
- `IMPLEMENTS` links to business processes, `PRESERVES` links to invariants, and references to requirements, business processes, invariants, Function Contracts, Module Contracts, tests, scenarios, functions, semantic blocks, stages, traces, and log events preserve GRACE semantics and traceability. They must not be rendered as C1–C3 architectural relationships solely because the reference exists.
- These links must not be discarded from the GRACE semantic graph or treated as unknown when their meaning is established; they remain traceability evidence where relevant to the generated element descriptions and provenance.

#### General rule

- Every relationship type rendered as a C1–C3 architectural relationship must have an explicit mapping rule in this section.
- If a relationship type is not covered by an approved mapping rule for the selected view, the validator must diagnose it as an unmapped relationship type and the renderer must not emit a C4 relationship for it. The generator must not silently classify an unmapped type as traceability or reinterpret it as an architectural interaction.
- If an otherwise mapped relationship lacks an unambiguous meaning, direction, or endpoint for the relevant view, the validator must report the missing or ambiguous information and the relationship must not be rendered.
- New or otherwise uncovered relationship types may be rendered only after an explicit mapping rule is approved and added to this profile.

### 7.2. Structurizr generation rules

1. Generated Structurizr DSL must disable implied relationships with `!impliedRelationships false`.
2. Every emitted relationship must be explicitly generated from GRACE evidence under an approved mapping rule.
3. The generator must not create unsupported elements or relationships, infer missing responsibilities, or silently repair contradictory source artifacts.
4. Each generated element and relationship must retain provenance to the GRACE artifact(s) supporting it.
5. **Reproducible generation is mandatory.** Given identical GRACE source artifacts, the same configuration, the same generator/tool version, and the same GRACE-ARP mapping-rule version, the generated Structurizr DSL and validation diagnostics must be byte-for-byte identical across runs. Element and relationship ordering, diagnostic ordering, and any generated identifiers must be deterministic. The generator must not let filesystem enumeration order, locale, timezone, current time, randomness, or process scheduling affect the output. Any generated identifier must be a deterministic function of stable source identity and the approved mapping rules. This is an additional mandatory GRACE-ARP requirement; it is not claimed to be an explicit requirement of base GRACE.
6. The workspace must apply visually distinguishable styles to the standard C4 tags `Person`, `Software System`, `Container`, and `Component`. At minimum, the visual treatment must distinguish these element kinds by shape, colour, or both; the `Person` tag must use the Person shape, and `Container` and `Component` must be distinguishable from `Software System` and from each other. This is a presentation rule and must not change the semantic meaning or classification of any GRACE element.
7. Styling must use Structurizr's tag-based element styles. Additional tags such as `ExternalSystem` may be assigned only when the external classification is supported by GRACE under an approved mapping rule; styling must not be used to infer or create that classification.
8. The exact colour palette is not fixed by this profile. The styles must remain consistent across generated C1–C3 views; differences in support by downstream export formats must not change the source model's semantics.

## 8. Validation requirements

The validator must distinguish at least:

- malformed source artifacts;
- unresolved references;
- missing information required for a C4 view;
- ambiguous semantic mappings;
- conflicting source facts;
- unsupported generated elements or relationships.

For the C1 external-system convention, the validator must verify that `EXTERNAL_SYSTEM` and `SYSTEM_INTERACTION` are direct children of `REQUIREMENTS_ANALYSIS`, all artifact IDs are unique, each declared external system has a non-empty display name, each interaction has a valid `external_system_ref`, an allowed `direction`, and a non-empty `PURPOSE`, and any supplied `system_name` is non-empty. Unresolved references and malformed or incomplete required interaction fields are blocking errors. An external-system declaration with no valid interaction must produce a non-blocking `Warning` and must not be rendered.

For C3 placement, the validator must verify that each `PLACEMENT` is an empty child of a `MODULE` in `DevelopmentPlan.xml`, has a non-empty `c2_ref`, resolves to exactly one C2 element established under § 5, and does not duplicate another placement for the same module/C2 pair. A module required in a selected C3 view without a valid placement must produce a blocking `Error`.

A declared `ACTOR` that is not referenced by any `USE_CASE/ACTOR` link must produce a `Warning` diagnostic. Under the approved CI validation rules, a warning alone does not make validation fail.

A relationship type with no approved mapping for the selected C1–C3 view must be diagnosed as unmapped and must not be rendered as an architectural relationship. When such a type is not explicitly classified in § 7.1 as a known semantic or traceability link, it is a blocking `Error`. A known semantic or traceability link explicitly classified in § 7.1 is not an unmapped relationship merely because it is not rendered as a C4 arrow.

### 8.1. Diagnostic severity

- `Error` is blocking. At minimum, malformed source artifacts; duplicate IDs; unresolved references required by a selected view; missing facts required for an approved mapping; ambiguous or conflicting semantic mappings; invalid or unsupported generated elements or architectural relationships; an architectural relationship type with no approved mapping; missing required provenance; and failed Structurizr DSL validation must be reported as `Error`.
- `Warning` is non-blocking and may be used only where this profile explicitly prescribes it or another approved rule defines it. A declared `ACTOR` not referenced by any `USE_CASE/ACTOR` link is a `Warning`; by itself it neither causes validation failure nor makes the view incomplete, because that actor does not qualify for the approved actor-to-system relationship. An `EXTERNAL_SYSTEM` with no valid referencing `SYSTEM_INTERACTION` is also a `Warning`; it is excluded from C1, but generation may continue.
- A diagnostic must not be downgraded from `Error` to `Warning` merely to allow generation to proceed. Known semantic or traceability links explicitly classified in § 7.1 are not errors simply because they are not rendered as C4 relationships.

### 8.2. Strict generation behavior

- Validation must run before publishing any generated C1–C3 output for the requested set of views. It must validate the source artifacts and mapping rules required by those views.
- If any blocking `Error` occurs during validation or generated-DSL validation, the entire generation run for the requested view set must fail. No generated C1–C3 DSL or diagrams from that run may be published, saved as final output, or presented as a partial result.
- The renderer may stage output internally for validation, but it must discard that staged output if any blocking `Error` occurs. It must not publish only the views or elements that happened to be generated successfully.
- If validation produces only `Warning` diagnostics and no `Error`, generation may proceed. The warnings must remain visible in the validation result.
- Successful parsing or validation of XML or Structurizr DSL is necessary but does not by itself prove semantic correctness or view completeness.

### 8.3. View-completeness criteria

Completeness is evaluated relative to the approved GRACE source artifacts, the selected view, and the mapping rules in this profile. It is not a claim that the real-world system or its documentation is globally complete.

A C1, C2, or C3 view is complete only when all of the following hold:

1. Every source element eligible for representation in the selected view under an approved mapping rule is accounted for by the resulting view, including the explicit aggregation and deduplication rules in §§ 4, 6, and 7. An element that the approved rules explicitly exclude from the view is not a missing element.
2. Every architectural relationship eligible for the view has an approved mapping, unambiguous meaning and direction where applicable, and endpoints mapped unambiguously to represented elements. All eligible relationships are represented according to the approved mapping, aggregation, and deduplication rules; no relationship is invented.
3. Every required reference, module-to-contract association, C3 placement, and relationship endpoint is resolved without ambiguity or conflict.
4. Every generated element and relationship has provenance to the GRACE artifact or artifacts that support it.
5. No applicable architectural relationship type remains unmapped, and no unsupported element or relationship is emitted.
6. The generated Structurizr DSL passes its applicable validation, including the requirement to disable implied relationships.

If any criterion fails, the affected view is incomplete and the strict generation run must fail with a blocking `Error`; partial views must not be published. A warning explicitly designated as non-blocking by this profile, including an unreferenced `ACTOR`, does not by itself fail completeness.

## 8.4. DevelopmentPlan semantic validation

The validator must check the architecture semantics encoded by DevelopmentPlan.xml using the parsed XML tree, exact element names, parent-child relationships, attributes, and explicit references. These checks must not use regular expressions, fuzzy matching, name-based inference, or interpretation of free-text descriptions. Text is inspected only to establish whether a required description is empty.

When DevelopmentPlan.xml is in scope, the MODULES container and each of the five sections below must occur exactly once. MODULES must contain at least one direct MODULE child. DATA_FLOWS must contain at least one DATA_FLOW; STATE_MODEL must contain at least one STATE_MACHINE; and IMPLEMENTATION_SEQUENCE must contain at least one PHASE. RISKS may be empty, which means that no risks are recorded. An empty MODULE_DEPENDENCIES section is valid.

All violations in this section are blocking Error diagnostics. The validator must report the source path, XML line and column when available, stable diagnostic code, and the owning stable ID when available.

### 8.4.1. MODULE_DEPENDENCIES

- Each MODULE is a direct child of the single MODULES container and must have a non-empty, globally unique id.
- Each DEPENDENCY must have a non-empty id, non-empty source_ref and target_ref, and exactly one non-empty PURPOSE.
- Both endpoints must resolve to exactly one MODULE declared in MODULES. A reference to another element type is invalid even if that element has the same ID.
- source_ref and target_ref describe the directed dependency/data handoff from the source module to the target module. The direction is not inferred from names or prose.
- A module cannot depend on itself. Multiple DEPENDENCY records may share the same source/target pair when they represent distinct dependency facts. Each record retains its own stable id and PURPOSE; cycle detection uses the unique directed endpoint pairs.
- The directed module dependency graph must be acyclic. Any directed cycle is a blocking error.
- APPLIES_TO is optional and may occur at most once; when present, its trimmed value must be exactly generate or validate. If absent, the dependency applies to both modes.
- CONDITION is optional and may occur at most once; when present, it must contain non-empty text.

### 8.4.2. DATA_FLOWS

- Every DATA_FLOW must have a non-empty id, exactly one non-empty PURPOSE, exactly one non-empty SUCCESS_RESULT, and exactly one non-empty FAILURE_RESULT.
- A DATA_FLOW must contain at least two direct STEP children.
- Every STEP must have a positive integer order and a non-empty module_ref. The order values must be unique and form the complete sequence 1..N, where N is the number of steps.
- Every module_ref must resolve to exactly one MODULE in MODULES.
- A module may occur more than once in one flow. Repeated module references are valid and represent repeated execution or participation; they must not be deduplicated.
- EXCLUDED_MODULES is optional and may occur at most once per flow. Each direct MODULE_REF inside it must resolve to exactly one declared MODULE, must be unique within that exclusion list, and must not also occur in the flow's STEP elements.
- A flow's ordered steps and the dependency graph are independently declared structures. The validator must not infer a missing MODULE_DEPENDENCIES edge merely because two modules are adjacent in a DATA_FLOW, nor infer execution order from dependency edges.

### 8.4.3. STATE_MODEL

- STATE_MODEL must contain at least one STATE_MACHINE. Each machine must have a non-empty, globally unique id.
- A machine's local STATE elements are direct children of that STATE_MACHINE. Each local state must have a non-empty, globally unique id and a non-empty description.
- Each USES_STATE must have a non-empty ref resolving to exactly one STATE declared under RequirementsAnalysis.xml/STATES/STATE_MODEL/STATE. A reference to an element with the same ID but a different element type or location is invalid.
- Within one machine, the combined set of local state IDs and USES_STATE references must contain no duplicates.
- Every machine must define or reference at least one state and contain at least one TRANSITION.
- Every TRANSITION must have non-empty from and to attributes and a non-empty description. Both endpoints must resolve to a state in the same machine's combined local/external state set.
- The same directed from/to pair may be declared only once within a machine. Self-transitions are valid.
- Every state declared or referenced by a machine must occur as the from or to endpoint of at least one transition. A state with no transition incidence is invalid.
- The current XML convention does not identify an initial state or provide machine-readable event/guard selectors. Therefore, the validator must not claim to prove transition reachability or deterministic transition selection, and must not infer either property from transition descriptions. Such guarantees require an explicit future schema extension.

### 8.4.4. IMPLEMENTATION_SEQUENCE

- IMPLEMENTATION_SEQUENCE must contain at least one PHASE.
- Every phase must have a non-empty, globally unique id, a positive integer order, and exactly one non-empty GOAL, DELIVERABLES, and CHECKS.
- Phase order values must be unique and form the complete sequence 1..N, where N is the number of phases.
- DEPENDS_ON is optional and may occur zero or more times inside a phase. Each element must have a non-empty ref resolving to exactly one PHASE; duplicate prerequisites and self-dependencies are invalid. Every prerequisite must have a lower order than the phase that depends on it.
- APPROVAL_GATE is optional and may occur at most once per phase. When present, it must contain non-empty text and a status whose trimmed value is exactly SATISFIED, PENDING, or BLOCKED.
- Phase order is the declared implementation order. The validator must not infer phase dependencies from the prose in GOAL, DELIVERABLES, or CHECKS. If a prerequisite must be machine-checked, it must be represented explicitly with DEPENDS_ON.

### 8.4.5. RISKS

- Each RISK must have a non-empty, globally unique id.
- severity is required and its trimmed value must be exactly one of BLOCKING, HIGH, MEDIUM, or LOW.
- status is optional. When present, its trimmed value must be exactly one of OPEN, MITIGATED, ACCEPTED, or RESOLVED. An omitted status is interpreted as OPEN; the source XML is not modified.
- Each risk must contain a non-empty description as text directly inside RISK, outside child elements, and exactly one non-empty MITIGATION child.
- Risk severity classifies the potential impact of the risk; it does not itself create a validation error or change the severity of unrelated diagnostics. The validator must not infer risk severity, status, or mitigation from descriptive prose.

### 8.4.6. Execution and determinism

The same semantic rules must run in the shared source-validation pipeline for project-wide validate and for generate whenever C2 or C3 is selected. C1-only generation does not load or validate DevelopmentPlan.xml.

The implementation must use the XML document tree and typed references. Numeric order attributes are parsed as integers; graph and duplicate checks operate on explicit IDs and directed edges. Ordered collections and the common diagnostic sorter must make the result independent of filesystem traversal order, hash iteration order, and XML declaration order wherever declaration order is not semantically significant. No regular expressions, textual heuristics, or automatic source corrections are permitted.

## 9. Decisions recorded in this profile

- GRACE is the sole source of truth.
- The initial representation scope is C1–C3; C4 Code is deferred.
- C1 is sourced from `RequirementsAnalysis.xml`.
- The C1 external-system XML convention is approved and mandatory for this profile: top-level `EXTERNAL_SYSTEM` and `SYSTEM_INTERACTION` elements, explicit `external_system_ref`, direction values `SYSTEM_TO_EXTERNAL` / `EXTERNAL_TO_SYSTEM`, and a non-empty `PURPOSE`; this is a GRACE-ARP extension and does not change base GRACE.
- A declared actor with no use-case reference must produce a `Warning` diagnostic.
- The standard C4 tags `Person`, `Software System`, `Container`, and `Component` must have visually distinguishable Structurizr styles.
- The C1 display-name rule is approved: use the non-empty root `system_name` attribute when present, otherwise the project repository name as a display-only fallback; if neither is available, report a diagnostic. The actor-to-system aggregation rule is approved: one generic `Person → Software System` relationship per actor linked to at least one use case.
- C2 is sourced from `Technology.xml` and `DevelopmentPlan.xml`.
- The source mapping in § 3 is mandatory for all C1–C3 generation and validation.
- Each GRACE module represented in a C3 view maps to one C3 component. All Module Contracts explicitly associated with that module support the same component; contracts are not separate components.
- C3 placement within a selected C2 is governed by § 6.1: a module component is placed only when approved architectural facts explicitly establish its execution within that C2; placement follows the stable-ID traceability path from Module Contract through GRACE module and architectural placement to C2; a module may appear in multiple C2-specific C3 views only with explicit evidence for each; data-store usage does not imply component placement inside the store; missing or ambiguous placement is diagnosed; no fixed XML schema is required.
- A module may have multiple Module Contracts; contract count is not component count.
- C3 relationship mapping is approved for the GRACE relationship types covered in § 7.1: a module-owned `USES ref="MOD-X"` to another GRACE module creates a directed component relationship; repeated declarations for the same ordered module pair collapse into one relationship while retaining provenance to all supporting contracts. `IMPLEMENTS`, `PRESERVES`, and requirement/process/invariant/function-contract links remain traceability or semantic links, not C3 architectural arrows. References to non-module elements do not create C3 relationships. Missing or ambiguous endpoint mappings are diagnosed rather than guessed.
- C1–C3 relationship classification is approved for the GRACE relationship forms covered in § 7.1: C2 architectural dependencies, data flows, and external integrations require explicit meaning, direction, and unambiguous endpoint mappings; business-process structure and requirement/process/invariant/contract/test/trace/log references remain semantic or traceability links rather than architectural arrows; relationship types without an approved mapping are diagnosed and not rendered until a mapping rule is approved.
- C3 components must expose traceability to their supporting Module Contracts and, where explicit GRACE links establish the association, to related Function Contracts. These contracts are accessible through the component description and/or links to source XML; they are not rendered as separate C3 nodes or relationships.
- The approved C2 selection rule: create a C2 element only when `Technology.xml` and `DevelopmentPlan.xml` unambiguously establish a standalone application or data store within the system in scope. A module or class is not automatically a C2 element; a service qualifies only when the architecture establishes it as a standalone application or executable unit. Multiple modules may be represented within one C2 element. A technology entry alone does not establish a C2 element. Missing or ambiguous boundaries must be diagnosed. No GRACE entity named `Container` or fixed XML shape is required.
- Strict validation is mandatory: any blocking `Error` during validation or generated-DSL validation aborts the generation run for the requested view set, and no partial or final C1–C3 output from that run may be published. `Warning` diagnostics alone do not block generation.
- View completeness is assessed against the approved source artifacts and mappings: all eligible elements and relationships must be accounted for; required mappings, references, endpoints, and C3 placements must be unambiguous and non-conflicting; all generated elements and relationships must retain provenance; and the generated DSL must pass validation with implied relationships disabled.
- Structurizr implied relationships are disabled by default.
- Rust is the selected implementation language for the tooling in this repository.

## 10. Normative traceability audit and approved mapping decisions

### 10.1. Status of the current rules

This table separates what GRACE itself establishes from the mapping rules explicitly approved for GRACE-ARP and records their normative basis.

| Topic | Basis | Status |
|---|---|---|
| Stable IDs and explicit links across the semantic graph | GRACE §§ 3, 19, 25 | Direct GRACE requirement |
| Requirements content: system goal, actors, use cases, business processes, entities, states, rules, invariants, errors, boundary cases, result criteria, and links | GRACE § 4.1 | Direct GRACE definition |
| Architecture content: modules, classes or services, responsibilities, data flows, dependencies, states, external integrations, process links, implementation sequence, risks, and mental checks | GRACE § 4.3 | Direct GRACE definition |
| Module Contract content and links to requirements/processes and other modules | GRACE § 5, stage 4 | Direct GRACE definition |
| Function Contracts refine the architecture and Module Contracts; mental tests precede implementation and do not prove execution | GRACE § 5, stages 5–6; § 12 | Direct GRACE requirement |
| C1 ← `RequirementsAnalysis.xml`; C2 ← `Technology.xml` + `DevelopmentPlan.xml`; C3 ← Module Contracts | Explicitly agreed source mapping in GRACE-ARP § 3 | Mandatory GRACE-ARP rule; not a claim that GRACE itself names C4 levels |
| C2 element selection | Explicitly approved GRACE-ARP mapping rule: require unambiguous evidence in `Technology.xml` and `DevelopmentPlan.xml` of a standalone application or data store; modules and classes are not C2 elements automatically; a service qualifies only when established as a standalone application or executable unit; multiple modules may be represented within one C2 element; technology entries alone do not establish C2 elements | Approved and mandatory; no `Container` entity or fixed XML shape required |
| Structurizr implied relationships disabled | Explicitly agreed for this project; Structurizr DSL behavior documented in the official reference linked in § 2 | Mandatory generation rule for this profile |
| C1 software-system display name | Explicitly approved mapping rule: use the non-empty root `system_name` attribute when present; otherwise use the repository name as a display-only fallback; if neither exists, diagnose | Approved |
| C1 actor-to-system relationship aggregation | Explicitly approved mapping rule: one generic relationship per actor referenced by one or more use cases | Approved |
| C1 external software-system representation | Explicitly approved GRACE-ARP XML convention in § 4: `EXTERNAL_SYSTEM`, `SYSTEM_INTERACTION`, `external_system_ref`, `direction`, and `PURPOSE` | Approved and mandatory for this profile; base GRACE unchanged |
| Warning for an actor not referenced by any use case | Explicitly approved for the validator | Mandatory `Warning` diagnostic |
| Visual distinction of standard C4 tags | Structurizr tag-based element styles; official reference in § 2 | Mandatory presentation rule |
| GRACE module to C3 component mapping | Explicitly approved GRACE-ARP mapping rule: each GRACE module represented in a C3 view maps to one component; all Module Contracts explicitly associated with that module support the same component | Approved and mandatory for this profile |
| Contract visibility and traceability in C3 | Explicitly approved GRACE-ARP rule in § 6.2: expose supporting Module Contract evidence and explicitly linked Function Contracts through component descriptions and/or source XML links; contract links do not create C3 nodes or architectural relationships | Approved |
| C3 placement within a selected C2 view | Explicitly approved GRACE-ARP rule in § 6.1: require explicit architecture-backed placement through Module Contract → GRACE module → architectural placement → C2; `DevelopmentPlan.xml` encodes each placement as a `PLACEMENT c2_ref="C2-ID"` child of `MODULE`; multiple C2 placement requires one child per distinct C2 ID; data-store use is not placement evidence; unresolved or duplicate placement is diagnosed | Approved; the XML element is a GRACE-ARP convention, not a base GRACE requirement |
| Mapping of GRACE relationship types to C1–C3 | Explicitly approved GRACE-ARP rules in § 7.1: actor participation and external-system interactions map to C1 under their specified conventions; C2 dependencies, data flows, and external integrations require explicit meaning, direction, and unambiguous endpoint mappings; module-owned `USES` to another GRACE module maps to a directed C3 relationship; business-process structure and requirement/process/invariant/contract/test/trace/log references remain semantic or traceability links; unmapped relationship types are diagnosed and not rendered | Approved for the relationship forms covered in § 7.1; new or otherwise uncovered types require an explicit approved mapping before rendering |
| Validator error categories and view-completeness criteria | Explicitly approved GRACE-ARP rules in § 8: blocking `Error` versus non-blocking `Warning`; strict generation aborts on any blocking error without publishing partial output; completeness is measured against the selected view, approved sources, and mappings, including endpoint/placement resolution, relationship coverage, provenance, and Structurizr DSL validation | Approved GRACE-ARP rule |
| Semantic integrity of `MODULE_DEPENDENCIES`, `DATA_FLOWS`, `STATE_MODEL`, `IMPLEMENTATION_SEQUENCE`, and `RISKS` | Explicitly approved GRACE-ARP rules in § 8.4: typed module/state references, acyclic dependency graph, ordered flow/phase sequences, transition endpoint integrity, and finite risk/gate classifiers | Approved GRACE-ARP rule; profile convention, base GRACE unchanged |
| Source-of-truth and no-invention constraints | GRACE §§ 1, 3, 25 require approved upstream intent, explicit semantic links, traceability, and prohibit silently deriving intent from implementation; GRACE-ARP applies these constraints to C1–C3 generation | Direct GRACE requirement |
| C1 participant and interaction eligibility | GRACE defines actors and use cases in § 4.1; the stricter C1 rules for actor aggregation, external-system declarations, direction, and display names are explicit approved mappings in §§ 4 and 7.1 | Approved GRACE-ARP mapping; not a claim that base GRACE defines C4 participants |
| C1 `STARTS_PROCESS` handling | GRACE defines `STARTS_PROCESS` as a use-case-to-business-process link in § 4.1; excluding it as a direct person-to-system C4 relationship is part of the approved C1 mapping in § 7.1 | Approved GRACE-ARP mapping |
| C2 boundary and relationship eligibility | GRACE § 4.3 defines modules, classes/services, data flows, dependencies, and integrations; the standalone-application/data-store selection rule and explicit relationship direction/endpoint requirements are approved mapping rules in §§ 5 and 7.1 | Approved GRACE-ARP mapping |
| C3 module identity and relationship mapping | GRACE §§ 3, 5, 19 establish modules, contracts, `USES` links, stable IDs, and traceability; mapping a module to one C3 component and mapping module-owned `USES` links to directed C3 arrows are approved GRACE-ARP rules | Direct GRACE graph semantics plus approved GRACE-ARP mapping |
| Mental scenarios and check criteria | GRACE §§ 5 and 12 treat mental tests as validation of a plan, not evidence of execution; limiting C1–C3 element/relationship creation to the approved source mapping follows the profile's approved mapping rules | Direct GRACE principle plus approved GRACE-ARP source mapping |
| C3 placement encoding | Approved GRACE-ARP convention in § 6.1: a `PLACEMENT c2_ref="C2-ID"` child of a `MODULE` in `DevelopmentPlan.xml` explicitly maps the module to a stable C2 ID; multiple placements require one child per distinct C2 ID; missing, duplicate, empty, or unresolved placement is a blocking error | Approved GRACE-ARP mapping; not a claim that base GRACE defines `PLACEMENT` |
| Unused `EXTERNAL_SYSTEM` diagnostic severity | Approved GRACE-ARP rule in §§ 4 and 8: an unused external-system declaration produces a non-blocking `Warning` and is not rendered | Approved GRACE-ARP rule |
| Reproducible generation (§ 7.2.5) | Approved additional GRACE-ARP requirement: identical source artifacts, configuration, tool version, and mapping-rule version must produce byte-for-byte identical Structurizr DSL and diagnostics, with deterministic ordering and generated IDs | Approved GRACE-ARP rule; not an explicit base GRACE requirement |
| Rust implementation language | This identifies the repository's tooling choice; GRACE does not mandate Rust and the statement does not change GRACE semantics | Repository implementation decision; not a GRACE requirement |

### 10.2. Approval record

The three decisions previously listed as open have been resolved and recorded as approved GRACE-ARP rules:

1. **C3 placement encoding:** `DevelopmentPlan.xml` uses a `PLACEMENT c2_ref="C2-ID"` child inside each `MODULE` to identify each C2 in which that module is explicitly executed.
2. **Unused external-system severity:** an `EXTERNAL_SYSTEM` without a valid referencing `SYSTEM_INTERACTION` produces a non-blocking `Warning`; it is not rendered.
3. **Reproducible generation:** identical source artifacts, configuration, generator/tool version, and mapping-rule version must produce byte-for-byte identical Structurizr DSL and validation diagnostics, with deterministic ordering and generated identifiers.

The complete normative profile was approved by the project owner on 2026-10-27. The rules above are binding for GRACE-ARP. They do not claim that base GRACE defines the `PLACEMENT` XML element or mandates byte-for-byte reproducibility; those are GRACE-ARP conventions. Relationship mappings and validation/completeness rules are specified in §§ 7–8. Mapping types not covered by the approved profile require separate approval before implementation.

On 2026-11-01, the project owner explicitly approved adding the DevelopmentPlan semantic rules in § 8.4. These rules are binding GRACE-ARP conventions for the five named sections. They formalize the architecture checks without changing `grace_source/GRACE.md` or claiming that the base methodology defines these exact XML encodings.


## 11. Authoring requirements and AI-agent handoff

The compact project-level authoring instructions for people and AI agents are maintained in [GRACE-ARP-INSTRUCTIONS.md](../../../GRACE-ARP-INSTRUCTIONS.md). Run `make install-docs PROJECT_DIR=/path/to/project` from the GRACE repository to install the project README, GRACE documentation, this profile, and the authoring guide without overwriting existing files. Use `make update-docs` to refresh unchanged managed files. The guide is an operational checklist derived from this profile and the base GRACE documentation; it does not create new mapping rules or supersede either normative source.

Authors must read the relevant GRACE sections and this profile before creating or editing artifacts. In particular, the guide calls out the mandatory GRACE-ARP conventions for C1 external systems and interactions, C2 direction and module placement, and C3 Module Contract ownership. These conventions are profile requirements, not claims that base GRACE defines the same XML elements.

AI agents must preserve approved intent, use stable IDs and explicit references, and report missing or ambiguous facts instead of inventing elements, interactions, directions, endpoints, ownership, or placements. Artifacts must be validated and warnings reviewed before views are treated as complete.
