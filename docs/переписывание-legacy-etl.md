# 16. Переписывание legacy-ETL

Для сложного ETL недостаточно нескольких example-based тестов.

Нужны:

- инварианты схемы;
- контроль количества записей;
- уникальность ключей;
- ссылочная целостность;
- контрольные суммы;
- идемпотентность;
- независимость от порядка строк;
- независимость от разбиения файла;
- сравнение старой и новой реализации;
- метаморфные проверки;
- property-based тесты;
- агентное исследование;
- семантические traces.

Схема:

```text
Legacy ETL
→ зафиксированное фактическое поведение
→ согласованные бизнес-контракты
→ новая реализация
→ двойной запуск на одинаковых данных
→ детерминированные проверки
→ агентный анализ расхождений
→ структурированный пакет ошибки
→ исправление
→ полная регрессия
```

Расхождения классифицируются:

```text
REGRESSION
— новая реализация нарушила требуемое поведение.

APPROVED_CHANGE
— поведение изменено утверждённым контрактом.

LEGACY_DEFECT
— новая реализация исправила подтверждённый дефект.

UNRESOLVED
— требуется решение предметного специалиста.
```

Пример пакета ошибки:

```xml
<ETL_TEST_FAILURE id="ETF-2026-0041">
    <SCENARIO ref="SCN-CUSTOMER-MERGE-017" />
    <CONTRACT ref="CONTRACT-CUSTOMER-MERGE" />
    <TRACE ref="TRACE-82FA1" />

    <FAILED_PROPERTY ref="INV-UNIQUE-CUSTOMER-ID">
        После объединения customer_id должен оставаться уникальным.
    </FAILED_PROPERTY>

    <EXPECTED>duplicate_customer_ids=0</EXPECTED>
    <ACTUAL>duplicate_customer_ids=3</ACTUAL>

    <FIRST_DIVERGENCE>
        <STAGE ref="STAGE-IDENTITY-NORMALIZATION" />
        <FUNCTION ref="normalize_external_id" />
    </FIRST_DIVERGENCE>
</ETL_TEST_FAILURE>
```

---

