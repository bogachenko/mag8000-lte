# MAG8000-LTE

Проект ведётся по методологии GRACE и профилю GRACE-ARP.

## Текущее состояние

Исходный ReqIF экспорт Polarion сохранён в `source/MAG8000-LTE-FeatureSpecReqBL4.reqif`.
Его структура и содержание проинвентаризированы в `analysis/reqif-inventory.md`.

`RequirementsAnalysis.xml` пока не создан: до фиксации семантического графа необходимо согласовать границу системы, baseline/release scope и два неполных объекта источника. Открытые решения перечислены в `analysis/requirements-decisions.md`.

## GRACE

- Методология: `docs/`
- GRACE-ARP: `docs/profiles/arp/GRACE-ARP.md`
- Инструкции проекта: `GRACE-ARP-INSTRUCTIONS.md`

Не создавай архитектурные факты, акторов, внешние системы, сценарии или связи только по упоминаниям в исходном ReqIF. Сначала согласуй открытые решения и затем формируй утверждаемый `RequirementsAnalysis.xml`.
