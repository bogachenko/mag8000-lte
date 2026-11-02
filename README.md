# MAG8000-LTE

Проект ведётся по методологии GRACE и профилю GRACE-ARP.

## Источник требований

Единственный источник требований — `source/MAG8000-LTE-FeatureSpecReqBL4.reqif`, Polarion `feature specification baseline 4`.

В работу включены все 70 Feature и все 32 Heading исходного документа. Пометки Release 1/Release 2, nice-to-have и обсуждаемые пункты сохраняются; требования не фильтруются и не дополняются внешними предположениями.

## GRACE

- Основной артефакт требований: `RequirementsAnalysis.xml`
- Полный реестр исходных Feature, Heading и связей: `analysis/reqif-inventory.md`
- Матрица испытаний конвертера ReqIF → GRACE с приоритетным стресс-набором: `analysis/converter-test-scope.md`
- Зафиксированная основа и правила преобразования: `analysis/requirements-decisions.md`
- Предварительная семантическая классификация всех 70 Feature: `analysis/semantic-model.md`
- Оригинальный ReqIF: `source/MAG8000-LTE-FeatureSpecReqBL4.reqif`
- Методология GRACE: `docs/`
- Профиль GRACE-ARP: `docs/profiles/arp/GRACE-ARP.md`
- Инструкции проекта: `GRACE-ARP-INSTRUCTIONS.md`

`RequirementsAnalysis.xml` содержит только семантику, которую можно подтвердить исходным документом и выразить конструкциями GRACE/GRACE-ARP. Полный набор Polarion Feature сохраняется в реестре без искусственного преобразования типов.
