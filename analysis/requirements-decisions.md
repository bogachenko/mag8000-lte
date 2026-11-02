# Открытые решения по RequirementsAnalysis

Статус: OPEN. Ни один пункт ниже не является утверждённым решением.

## D-001. Граница системы

В ReqIF описан 4G communication module для MAG8000 Transmitter, но также упомянуты cloud-based solution, Thingstream, MQTT Broker и Web APP.

Что является системой под спецификацией?

- A. Только 4G communication module, включая embedded firmware.
- B. 4G communication module вместе с MAG8000 Transmitter как единая система.
- C. End-to-end решение: модуль, MAG8000 Transmitter, cloud/Thingstream и Web APP.
- D. Другая граница — требуется описание.

## D-002. Baseline и release scope

В источнике есть пометки `nice to have`, `to be discussed`, `needs to be discussed`, а также функции, отложенные на Release 2 или исключённые из текущего релиза.

Какой объём включать в первую утверждаемую модель?

- A. Все 70 Feature; пометки и release status сохранить как открытые вопросы и ограничения.
- B. Только требования текущего Release 1; отложенные и nice-to-have исключить из текущего scope, сохранив в исходном ReqIF.
- C. Все требования, но статус каждого спорного пункта согласовать отдельно.

## D-003. Два пустых ReqIF.Text

У объектов `adr-10361` и `adr-10363` `ReqIF.Text` пуст, но `ReqIF.ChapterName` содержит предложения, похожие на текст требований.

Можно ли использовать `ReqIF.ChapterName` как содержание этих двух требований, сохранив факт пустого `ReqIF.Text` в provenance?

- A. Да.
- B. Нет, оба пункта остаются неполными до исправленного экспорта или подтверждения.

## D-004. Внешние технические документы

ReqIF ссылается на `A5E5009542A`, `A5E48591235A`, `A5E38431885A` и другие документы, но не включает их.

Нужно ли включить эти документы в анализ? Если да, приложите их в чат или добавьте в репозиторий.

## D-005. Цель и участники

ReqIF не содержит явных `PROJECT_GOAL`, `ACTOR`, `USE_CASE` или `SYSTEM_INTERACTION`. Упоминания customer, Web APP, cloud-based solution и Thingstream недостаточны для создания таких узлов.

Цель и основные участники будут уточняться после решения D-001.
