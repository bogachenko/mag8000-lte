# MAG8000-LTE

Проект ведётся по методологии GRACE и профилю GRACE-ARP.

## Источник требований

Единственный источник требований — `source/MAG8000-LTE-FeatureSpecReqBL4.reqif`, Polarion `feature specification baseline 4`.

В работу включены все 70 Feature и все 32 Heading исходного документа. Пометки Release 1/Release 2, nice-to-have и обсуждаемые пункты сохраняются; требования не фильтруются и не дополняются внешними предположениями.

## GRACE

- Основной артефакт требований: `RequirementsAnalysis.xml`
- Инвентаризация исходного ReqIF: `analysis/reqif-inventory.md`
- Правила преобразования и принятый scope: `analysis/requirements-decisions.md`
- GRACE: `docs/`
- GRACE-ARP: `docs/profiles/arp/GRACE-ARP.md`
- Инструкции проекта: `GRACE-ARP-INSTRUCTIONS.md`

В `RequirementsAnalysis.xml` исходные Feature сохранены как отдельный provenance-слой, чтобы не приписывать им неподтверждённую семантику. C1-взаимодействия создаются только при наличии прямого указания в исходном документе.
