# 11. Log-Driven Development

В LDD ожидаемая трасса проектируется как часть сценария.

```xml
<EXPECTED_TRACE id="TRACE-ORDER-POSTING">
    <STEP order="1" event="ORDER_VALIDATED" />
    <STEP order="2" event="STOCK_RESERVED" />
    <STEP order="3" event="ORDER_SAVED" />

    <FORBIDDEN_EVENT event="UNRELATED_CUSTOMER_CHANGED" />

    <FINAL_STATE>
        order_status=SAVED
        stock_reserved=true
    </FINAL_STATE>
</EXPECTED_TRACE>
```

Проверяется не только конечный результат, но и:

- какие шаги выполнены;
- в каком порядке;
- какие решения приняты;
- какие состояния изменены;
- какие запрещённые события возникли;
- соответствует ли путь контракту.

LLM-оценка трассы является дополнительным семантическим слоем, а не заменой детерминированных гарантий.

---

