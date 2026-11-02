# Инвентаризация исходного ReqIF

Статус: SOURCE_ANALYSIS — извлечение фактов из Polarion, не утверждённая модель требований GRACE.

## 1. Источник

| Поле | Значение |
|---|---|
| Файл | `MAG8000-LTE-FeatureSpecReqBL4.reqif` |
| ReqIF version | `1.0` |
| ReqIF tool | `Polarion ReqIF Roundtrip` |
| Source tool | `Polarion` |
| Export title | `MAG8000-LTE-FeatureSpecReqBL4` |
| Specification | `feature specification baseline 4` |
| Creation time | `2022-06-22T11:22:44.868+02:00` |
| Size | `250031` bytes |
| SHA-256 | `19eb5406e59c27417e57c25c097c948e8ab8b5f23d97a0692b51721ecfc8a5c8` |
| Git blob SHA-1 | `fa29d4f0711864350a3c4127ad7be526c2b68628` |

## 2. Структура

| Элемент | Количество |
|---|---:|
| Feature | 70 |
| Heading | 32 |
| Всего SpecObject | 102 |
| Объявлено типов объектов | 3 |
| Объявлено типов связей | 14 |
| SpecRelation | 26 |
| Feature с непустым ReqIF.Text | 68 |
| Feature с пустым ReqIF.Text | 2 |

Пять имён атрибутов: `ReqIF.ChapterName`, `ReqIF.ForeignCreatedBy`, `ReqIF.ForeignCreatedOn`, `ReqIF.ForeignID`, `ReqIF.Text`. `ReqIF.Text` имеет тип XHTML. Полный XML сохранён в `source/`.

## 3. Heading

`Heading` — разделы исходного документа, а не автоматически выделенные требования.

- feature specification baseline 4 — Polarion ID `adr-10312`, ReqIF ID `rmf-a1e7f861-b9fd-4859-95f5-bf6c735115ad`
- Features — Polarion ID `adr-10307`, ReqIF ID `rmf-ebc7aabb-cc04-4ad0-9818-961b0c4d2afc`
- Introduction — Polarion ID `adr-10313`, ReqIF ID `rmf-3525869d-a832-4d42-837c-820441efe2b4`
- The current solution — Polarion ID `adr-10314`, ReqIF ID `rmf-dc680cd6-28cb-45d1-9639-ce1bc814941d`
- Migration to LTE IoT — Polarion ID `adr-10306`, ReqIF ID `rmf-c5dc3abe-8354-4fc6-a863-b273c8ba6d9e`
- Electronic — Polarion ID `adr-10438`, ReqIF ID `rmf-a0ce7ddf-d134-48db-8626-01862c842cc8`
- SIM Card — Polarion ID `adr-10440`, ReqIF ID `rmf-cde6a2d7-9dee-44ad-87c3-1d04962b8f12`
- Mechanic — Polarion ID `adr-10441`, ReqIF ID `rmf-aff71bf4-470c-4520-849a-83b96c5efed0`
- Environment — Polarion ID `adr-10434`, ReqIF ID `rmf-7a89b415-dc4b-4134-8285-c3c9f52f7f73`
- Interface — Polarion ID `adr-10435`, ReqIF ID `rmf-d15a8380-9149-45f3-a850-087e7040a4e4`
- Functionalities — Polarion ID `adr-10436`, ReqIF ID `rmf-d6f394ce-573d-45a7-acf7-e3f362020d2e`
- Sitrans IQ App — Polarion ID `adr-10442`, ReqIF ID `rmf-fd3ad30e-11e7-4ee1-a839-1b17ff5bac1f`
- Use case : — Polarion ID `adr-10444`, ReqIF ID `rmf-43875c5b-0d23-4a26-994b-a473316325de`
- Wireless Specification — Polarion ID `adr-10439`, ReqIF ID `rmf-56b6fbc4-2e91-4d24-b4bd-8545cbc66d76`
- E-mail — Polarion ID `adr-10437`, ReqIF ID `rmf-d4024065-9b4d-4934-b954-ffbef51e1f66`
- FTP — Polarion ID `adr-10423`, ReqIF ID `rmf-87a22934-ad0b-40e0-88c4-d530a2092814`
- MQTT-SN/MQTT — Polarion ID `adr-10431`, ReqIF ID `rmf-cb7085c4-7af0-409a-b53b-7c4285c4f7b3`
- format of process values : — Polarion ID `adr-10430`, ReqIF ID `rmf-27046128-2db1-427e-a706-8f582da14f90`
- CSV file format stored in SD card and to be used by mag8000 Web APP for serve.IQ connectivity. — Polarion ID `adr-10433`, ReqIF ID `rmf-f146a960-f1ba-474f-9c23-9ea855510b08`
- Remote qualification certificate (to be discussed with web APP team) — Polarion ID `adr-10432`, ReqIF ID `rmf-1885525d-6fd0-4ba6-9662-cac2c696d064`
- Voltage input readings (nice to have), to be discussed during MF concept. — Polarion ID `adr-10427`, ReqIF ID `rmf-5305b7be-682e-4f48-beb1-c3d318df85fa`
- First transmission protocol — Polarion ID `adr-10426`, ReqIF ID `rmf-c5b1bf0e-850c-47f3-855b-0145be38090c`
- Data collection and transmission — Polarion ID `adr-10429`, ReqIF ID `rmf-e43cffe2-a0b5-47b3-9c80-ccf0ca074fed`
- 4G module simplified EDD file description — Polarion ID `adr-10428`, ReqIF ID `rmf-4a940292-1486-4791-9b13-01276cb229de`
- Historical data — Polarion ID `adr-10425`, ReqIF ID `rmf-65f9518d-db0d-45ef-afbc-d39c18eef6e0`
- Error handling — Polarion ID `adr-10424`, ReqIF ID `rmf-748121c5-3ef6-4f0a-9cdd-c9f9156f7243`
- Alarm handling — Polarion ID `adr-10449`, ReqIF ID `rmf-59ae68d3-e956-4ea4-9d60-967702b59608`
- Product configuration — Polarion ID `adr-10446`, ReqIF ID `rmf-9b491e27-ceb8-40fc-bab8-dac110dad872`
- Supplementary Functionalities — Polarion ID `adr-10445`, ReqIF ID `rmf-1b313ce9-9e46-49fc-8eb1-80ace9bf3b4c`
- Product Security — Polarion ID `adr-10448`, ReqIF ID `rmf-c175036d-b4be-448d-b450-e46efc0b8abe`
- Usability/commissioning (needs to be discussed) — Polarion ID `adr-10447`, ReqIF ID `rmf-1729ef87-413e-46ed-868c-7858aba0e18b`
- Accessories and spare parts — Polarion ID `adr-10443`, ReqIF ID `rmf-f1b7f322-e634-4a28-8505-996ba326757c`

## 4. Реестр Feature

Текст `ReqIF.Text` извлечён из XHTML. Орфография и терминология источника не исправлялись. Пустые значения не подменяются автоматически `ReqIF.ChapterName`.

### 01. adr-10370

- ReqIF ID: `rmf-62eea757-2e61-4165-bf27-327c2869c232`
- ReqIF.ChapterName: SPI Flash of 32Mbyte will be present on 4G module.
- ReqIF.Text:

~~~~text
SPI Flash of 32Mbyte will be present on 4G module.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.488+01:00`

### 02. adr-10373

- ReqIF ID: `rmf-99c4a51a-061a-4b5b-b558-f3b92d659d25`
- ReqIF.ChapterName: SMA connector to GSM antenna will be used.
- ReqIF.Text:

~~~~text
SMA connector to GSM antenna will be used.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.644+01:00`

### 03. adr-10372

- ReqIF ID: `rmf-c28d60fd-db58-4a34-a1fa-9d340885cd48`
- ReqIF.ChapterName: A so called "data structure" specific to the device will be stored on the uC fla...
- ReqIF.Text:

~~~~text
A so called "data structure" specific to the device will be stored on the uC flash memory. The size of this structure will be 4 KB. This structure will be updated during Manufacturing.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.597+01:00`

### 04. adr-10367

- ReqIF ID: `rmf-c2345a84-ce17-46a1-9a3b-87db23bdf73c`
- ReqIF.ChapterName: The module will embed SARA R422S module which support release 14
- ReqIF.Text:

~~~~text
The module will embed SARA R422S module which support release 14
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.347+01:00`

### 05. adr-10366

- ReqIF ID: `rmf-2680d1a2-d63f-4842-9e13-d5746df7546a`
- ReqIF.ChapterName: The module will have an interface with SIM
- ReqIF.Text:

~~~~text
The module will have an interface with SIM
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.300+01:00`

### 06. adr-10369

- ReqIF ID: `rmf-4e7cdbb0-bf96-4c6a-96fc-95b546ecac35`
- ReqIF.ChapterName: The module Sara R422S is provided with an embedded esim solution. (release of SARA...
- ReqIF.Text:

~~~~text
The module Sara R422S is provided with an embedded esim solution. (release of SARA R422S with esim option planned for late 2021). Esim is not used for release 1.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.441+01:00`

### 07. adr-10368

- ReqIF ID: `rmf-90467e41-5651-44a8-888a-36c37f9a90a0`
- ReqIF.ChapterName: SIM and esim solution will be supported in the module.
- ReqIF.Text:

~~~~text
SIM and esim solution will be supported in the module.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.394+01:00`

### 08. adr-10387

- ReqIF ID: `rmf-0a669af1-ca6a-474b-9b9b-00d79d0b2be0`
- ReqIF.ChapterName: The module will support 1.8V and 3.0V
- ReqIF.Text:

~~~~text
TheÂ module will support 1.8V and 3.0V
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.331+01:00`

### 09. adr-10389

- ReqIF ID: `rmf-03759471-ed42-457b-9420-902bfd6f1420`
- ReqIF.ChapterName: hot swap should'nt destroy the module, after unplug and plug the module, the mod...
- ReqIF.Text:

~~~~text
hot swap shouldn't destroy the module, after unplug and plug the module, the module should work again.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.441+01:00`

### 10. adr-10388

- ReqIF ID: `rmf-2757d5f2-5180-4c04-99d0-176cb071e6a7`
- ReqIF.ChapterName: The 4G module will be mounted inside all possible configurations of MAG8000 Tran...
- ReqIF.Text:

~~~~text
The 4G module will beÂ mounted inside all possible configurations of MAG8000 Transmitter enclosure : Remote version, compact version, 230V,24V and battery version.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.378+01:00`

### 11. adr-10384

- ReqIF ID: `rmf-6024ded0-603e-4282-93c1-dfd209800c1b`
- ReqIF.ChapterName: The module will work under following conditions -20Â°C up to 60Â°C.
- ReqIF.Text:

~~~~text
The module will work under following conditions -20Â°C up to 60Â°C.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.175+01:00`

### 12. adr-10383

- ReqIF ID: `rmf-55174b6a-289c-42f1-877d-46a8e6f1b4f1`
- ReqIF.ChapterName: The MAG8000 modbus registers defined in document A5E5009542A will be accessible...
- ReqIF.Text:

~~~~text
The MAG8000 modbus registers defined in document A5E5009542A will be accessible by the module.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.128+01:00`

### 13. adr-10386

- ReqIF ID: `rmf-12297089-eea8-4bde-a866-19fa8e2b7902`
- ReqIF.ChapterName: SMTP/SMTPs communication protocol to send data will be supported by the cloud ba...
- ReqIF.Text:

~~~~text
SMTP/SMTPs communication protocol to send data will be supported by the cloud based solution.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.269+01:00`

### 14. adr-10385

- ReqIF ID: `rmf-f465ea3a-79ef-4fef-bc13-88c8f98b84a5`
- ReqIF.ChapterName: E-mail sent will be compliant to following format : Subject: "Prefix: [IDENTIFIE...
- ReqIF.Text:

~~~~text
E-mail sent will be compliant to following format : Subject: "Prefix: [IDENTIFIER]" where [IDENTIFIER] is one of the below, controlled by a parameter. - Meter Serial Number (6:00248) [STRING][12] - ApplicationID (8:00656) [STRING][16] - ApplicationLocation (8:00664) [STRING][16] Meter Serial number, Application ID and Application Location are read from the host device. The default value of Prefix is "MAG8000".
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.222+01:00`

### 15. adr-10381

- ReqIF ID: `rmf-39b5cd09-37f9-42dc-95f4-c7f5e28b67c4`
- ReqIF.ChapterName: FTP/FTPs (implicit and explicit will be supported) communication protocol to sen...
- ReqIF.Text:

~~~~text
FTP/FTPs (implicit and explicit will be supported) communication protocol to send data will be supported by the cloud based solution
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.035+01:00`

### 16. adr-10380

- ReqIF ID: `rmf-9f568401-5b3d-4621-b1a8-4d7f78d5cf42`
- ReqIF.ChapterName: The measurmeent data will be sent in "CSV file format"
- ReqIF.Text:

~~~~text
The measurement data will be sent in "CSV file format"
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.988+01:00`

### 17. adr-10382

- ReqIF ID: `rmf-42ba9181-38c9-47c7-b949-c7227bd14c9f`
- ReqIF.ChapterName: Process values will be sent out in binaries format (see MQTT commands descriptio...
- ReqIF.Text:

~~~~text
Process values will be sent out in binaries format (see MQTT commands description A5E48591235A).
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.081+01:00`

### 18. adr-10352

- ReqIF ID: `rmf-48e30a43-bdb8-4a07-8bea-8805a0a07572`
- ReqIF.ChapterName: Serial flash memory will be used to buffer process values.
- ReqIF.Text:

~~~~text
Serial flash memory will be used to buffer process values.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.644+01:00`

### 19. adr-10351

- ReqIF ID: `rmf-9dec5683-7721-4809-a204-7b9777f991ae`
- ReqIF.ChapterName: The measurement data collected from the host device will be saved in csv format....
- ReqIF.Text:

~~~~text
The measurement data collected from the host device will be saved in csv format. The filename of the csv file will be composed of Prefix_[identifier]_[timestamp].csv Prefix: ordinary text strings, configurable by a parameter; Timestamp: YYYYMMDD_HHmm; Identifier: read from the modbus register of the host device -> " MeterSerialNo" (248)
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.597+01:00`

### 20. adr-10354

- ReqIF ID: `rmf-92216a53-a63e-4fee-a531-5d6b20a5037d`
- ReqIF.ChapterName: The measurement data read from the host device (TRN) will be compiled in the csv...
- ReqIF.Text:

~~~~text
The measurement data read from the host device (TRN) will be compiled in the csv file. The format of the measurement data stored in the csv file will be : [timestamp];[FL];[FL unit];[TOT1];[TOT2];[TOT3];[TOT unit];[V1];[V2];[BT];[AL] timestamp = YYYY-MM-DD HH:MM FL value = Flow rate value FL unit = unit of Flow rate TOT1 = Totalizer 1 value TOT2 = Totalizer 2 value TOT3 = Totalizer 3 value TOT unit = Totalizer unit V1 = the converted process value from voltage input 1 V2 = the converted process value from voltage input 2 BT = remaining battery capacity (integer value from 0 to 100, i.e. BT%), Transmitter battery capacity wil be used (3030). AL = alarms in decimal value (host device alarm) For example, the measurement data stored in the csv file shall as below 2018-01-01 05:02;0.000;m3/h;1.199;0.732;1.199;m3;0.0;0.0;96;5176 2018-01-01 05:03;0.000;m3/h;1.199;0.732;1.199;m3;0.0;0.0;96;5176 2018-01-01 05:04;0.000;m3/h;1.199;0.732;1.199;m3;0.0;0.0;96;5176
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.738+01:00`

### 21. adr-10353

- ReqIF ID: `rmf-79ad8814-5de1-4c9f-a97f-607e5880cf06`
- ReqIF.ChapterName: Mag8000 web APP will trigger GET_PARAMETER command in order to get all needed pa...
- ReqIF.Text:

~~~~text
Mag8000 web APP will trigger GET_PARAMETER command in order to get all needed parameter.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.691+01:00`

### 22. adr-10348

- ReqIF ID: `rmf-facd3a8f-34d1-4336-8f5e-84442cf3d4a5`
- ReqIF.ChapterName: Certificate will be generated by web APP and will be available in PDF format.
- ReqIF.Text:

~~~~text
Certificate will be generated by web APP and will be available in PDF format.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.456+01:00`

### 23. adr-10347

- ReqIF ID: `rmf-d075d01b-2bcc-448e-a8f6-2d96b507c99b`
- ReqIF.ChapterName: certification process will be triggered by customer through Web APP.
- ReqIF.Text:

~~~~text
certification process will be triggered by customer through Web APP.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.410+01:00`

### 24. adr-10350

- ReqIF ID: `rmf-f16446cf-fe6f-479b-9109-367797ec9d45`
- ReqIF.ChapterName: Maximum error of this voltage input will be 3% accross temperature range.
- ReqIF.Text:

~~~~text
Maximum error of this voltage input will be 3% accross temperature range.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.550+01:00`

### 25. adr-10349

- ReqIF ID: `rmf-3eab865c-e4a2-4107-9487-ba25f41e292f`
- ReqIF.ChapterName: The activation of the two Voltage input can be activated through "AnalogInputsAc...
- ReqIF.Text:

~~~~text
The activation of the two Voltage input can be activated through "AnalogInputsAcquisitionControl"
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.503+01:00`

### 26. adr-10346

- ReqIF ID: `rmf-3c9c3fbb-3052-4d49-9b44-bfdd6b787090`
- ReqIF.ChapterName: The product will support two voltage input :Supply voltage range provided by the...
- ReqIF.Text:

~~~~text
The product will support two voltage input :Supply voltage range provided by the product: 5 VDC +/- 50 mV Supply current range: max. 5 mA Input range: 0 ... 5 VDC Typical ON time (sample time) during measurement: 100ms
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.363+01:00`

### 27. adr-10345

- ReqIF ID: `rmf-501465ef-7d85-43b6-9e05-a7853a07e234`
- ReqIF.ChapterName: The product will have four settable conversion factors
- ReqIF.Text:

~~~~text
The product will have four settable conversion factors, "slopeAnalogInput1 " , "slopeAnalogInput2"; "OffsetAnalogInput1"; "OffsetAnalogInput2".
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.316+01:00`

### 28. adr-10364

- ReqIF ID: `rmf-d1595c05-1c79-4476-83dc-88626c8babec`
- ReqIF.ChapterName: 12 bits resolution will be implemented, for voltage input measurement.
- ReqIF.Text:

~~~~text
12 bits resolution will be implemented, for voltage input measurement.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.206+01:00`

### 29. adr-10361

- ReqIF ID: `rmf-a6657080-701a-40cc-a054-9d104614eeb1`
- ReqIF.ChapterName: the calculated value (taking into account slopeAnalogInput and OffsetAnalogInput) should be saved in measurement data.
- ReqIF.Text: **пусто**
- `ReqIF.ChapterName` содержит текст, похожий на требование; подстановка не выполнялась.
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.066+01:00`

### 30. adr-10360

- ReqIF ID: `rmf-ff5c2933-051a-4dcd-afc1-aafcee078464`
- ReqIF.ChapterName: Calculated value (with the customer factor) , rounded three digit after decimal...
- ReqIF.Text:

~~~~text
Calculated value (with the customer factor) , rounded three digit after decimal will be displayed.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.019+01:00`

### 31. adr-10363

- ReqIF ID: `rmf-487d4049-f3ee-4aca-b92a-d93959c9b3e8`
- ReqIF.ChapterName: In case the AnalogInputsAcquisitionControl is disabled following parameters should exhibit 0 value in SD card and in sent measurements : AnalogValue1 and AnalogValue2.
- ReqIF.Text: **пусто**
- `ReqIF.ChapterName` содержит текст, похожий на требование; подстановка не выполнялась.
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.160+01:00`

### 32. adr-10362

- ReqIF ID: `rmf-e79cadd7-219e-4cca-acf6-3d81a049fe5e`
- ReqIF.ChapterName: A screening procedure over the MNO (mobile network operator profile) will be pre...
- ReqIF.Text:

~~~~text
A screening procedure over the MNO (mobile network operator profile) will be present on the 4G module for connectivity purposes (different regions codes). This functionnality will be handle by the com module library. In order to harvest power the radio access technology priority should be following 4G NB IoT > 4G Cat M1 > 2G.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:22.113+01:00`

### 33. adr-10357

- ReqIF ID: `rmf-e09775fb-33c1-4860-8b89-41124a686a45`
- ReqIF.ChapterName: The module will have a configurable data collection and is continuous ( 60 to 86400) "DataCollectionInterval"
- ReqIF.Text:

~~~~text
The module will have a configurable data collection and is continuous ( 60 to 86400). " DataCollectionInterval ". Default value is 600.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.878+01:00`

### 34. adr-10356

- ReqIF ID: `rmf-78385236-1e95-4fc3-b73a-413e8014ec20`
- ReqIF.ChapterName: The module will have a configurable data transmission and is continuous
- ReqIF.Text:

~~~~text
The module will have a configurable data transmission and is continuous (60 to 2678400 seconds)."TransmissionInterval". Default value should be 10800 seconds.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.831+01:00`

### 35. adr-10359

- ReqIF ID: `rmf-a39c3d94-45cc-473b-96d1-b5afa7ebfd53`
- ReqIF.ChapterName: In case configurable parameter "AutoAdaptiveControl" is enable, the transmission interval...
- ReqIF.Text:

~~~~text
In case configurable parameter " AutoAdaptiveControl " is enable, the transmission interval will go automatically to 30 min if parameter "PowerSupply" (power supply) is set up to 1. In case this parameter is set to 0 this features will not work. In case the data transmission interval is below 30 min the autoadaptive features will not be enabled.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.972+01:00`

### 36. adr-10358

- ReqIF ID: `rmf-9634e0e6-cd37-45eb-ac1c-98205d0600ec`
- ReqIF.ChapterName: In case the data transmission interval is below 15 min the autoadaptive features...
- ReqIF.Text:

~~~~text
In case the data transmission interval is below 15 min the autoadaptive features will not be enabled.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.925+01:00`

### 37. adr-10355

- ReqIF ID: `rmf-6ad1a3af-bfb6-4c79-94c5-5f845e3daca4`
- ReqIF.ChapterName: The module will have a configurable paging interval and is continuous
- ReqIF.Text:

~~~~text
The module will have a configurable paging interval and is continuous (60 to 2678400 seconds) "PagingInterval", this interval will be valid only if it less than data transmission interval. A parameter "pagingcontrol" will enable/disable the paging interval functionnality. Default value should be 3600 seconds.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.785+01:00`

### 38. adr-10334

- ReqIF ID: `rmf-4b9b8e9e-c110-4ed5-89c1-ab3e6ad47592`
- ReqIF.ChapterName: The paging interval feature shall not work if the auto-adaptive transmission fea...
- ReqIF.Text:

~~~~text
The paging interval feature shall not work if the auto-adaptive transmission feature is activated.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.800+01:00`

### 39. adr-10333

- ReqIF ID: `rmf-c2a7cd19-13c5-4866-8be9-e4d56be43066`
- ReqIF.ChapterName: IntervalSynchronisationTime parameter will be used to set up synchronisation time
- ReqIF.Text:

~~~~text
IntervalSynchronisationTime parameter will be used to set up synchronisation time. Unix UTC time stamp will be used. Default value will be 0xFFFFFFFF.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.753+01:00`

### 40. adr-10330

- ReqIF ID: `rmf-3688c7c4-8e39-4315-bc46-9544fc92f80c`
- ReqIF.ChapterName: EDD file will describe the 4G module specific parameter accessible as described...
- ReqIF.Text:

~~~~text
EDD file will describe the 4G module specific parameter accessible as described in the parameter list A5EA5E5009542A
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.613+01:00`

### 41. adr-10329

- ReqIF ID: `rmf-ff6fcce5-6e3e-47e6-93d5-609e3843171c`
- ReqIF.ChapterName: EDD file will stored inside the Uc internal flash memory
- ReqIF.Text:

~~~~text
EDD file will be integrated into application firmware
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.566+01:00`

### 42. adr-10332

- ReqIF ID: `rmf-eae6affa-a63a-43f3-a558-86a73104adf4`
- ReqIF.ChapterName: EDD file will be flashed during MF process
- ReqIF.Text:

~~~~text
EDD file will be flashed during MF process
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.706+01:00`

### 43. adr-10331

- ReqIF ID: `rmf-407be4d3-3308-446d-86e1-24639d115eeb`
- ReqIF.ChapterName: EDD file will contain a version number "EDDFileVersion" Parameter (5000).
- ReqIF.Text:

~~~~text
EDD version will be integrated into the "firmwareversion"
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.659+01:00`

### 44. adr-10326

- ReqIF ID: `rmf-358c354c-7925-4ac6-8dce-1229e396aaee`
- ReqIF.ChapterName: EDD file mapping will be done through parameter name.
- ReqIF.Text:

~~~~text
EDD file mapping will be done through parameter name.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.441+01:00`

### 45. adr-10325

- ReqIF ID: `rmf-38e09f0b-ed02-4141-92aa-0b2692d27ca0`
- ReqIF.ChapterName: The module will support a micro SD card.
- ReqIF.Text:

~~~~text
The module will support a micro SD card.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.269+01:00`

### 46. adr-10328

- ReqIF ID: `rmf-c5e7f5e0-7ab2-4b5a-a288-2969298dffca`
- ReqIF.ChapterName: Data will be stored based on data collection interval "DataCollectionInterval", e...
- ReqIF.Text:

~~~~text
Data will be stored based on data collection interval " DataCollectionInterval ", earliest data shall overwritte the oldest data in case of full memory.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.519+01:00`

### 47. adr-10327

- ReqIF ID: `rmf-29de3010-a096-4242-a329-385674b07814`
- ReqIF.ChapterName: the module should be able to run without SDcard. storage of CSV file will be drop...
- ReqIF.Text:

~~~~text
the module should be able to run without SDcard storage of CSV file will be dropped in that case.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.488+01:00`

### 48. adr-10342

- ReqIF ID: `rmf-925ceba4-cd00-43a7-9b0b-ebe5e4c19a76`
- ReqIF.ChapterName: User Manual will indicate that SD card shouldn't be removed without using functi...
- ReqIF.Text:

~~~~text
User Manual will indicate that SD card shouldn't be removed without using function button.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.175+01:00`

### 49. adr-10344

- ReqIF ID: `rmf-1a709544-245c-48e3-82ef-da5305606472`
- ReqIF.ChapterName: retry mechanism: done internally by Thingstream SDK.
- ReqIF.Text:

~~~~text
retry mechanism: done internally by Thingstream SDK.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.269+01:00`

### 50. adr-10343

- ReqIF ID: `rmf-910ec745-300a-4379-b888-8809e91b6b18`
- ReqIF.ChapterName: The module will log all failed data transmission by date in SD card if its plugg...
- ReqIF.Text:

~~~~text
The module will log all failed data transmission by date in SD card if its plugged in.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.222+01:00`

### 51. adr-10339

- ReqIF ID: `rmf-a0478337-09a4-4626-afd4-491956514ad8`
- ReqIF.ChapterName: If SD card is not present the logging data will be saved in external SPI Flash M...
- ReqIF.Text:

~~~~text
If SD card is not present the logging data will be saved in external SPI Flash Memory.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.035+01:00`

### 52. adr-10338

- ReqIF ID: `rmf-9eaa02e9-e629-4f2c-92e8-228822dc24ab`
- ReqIF.ChapterName: The signal network errors will be trigered through "NetworkSignalStrengthAlarmThreshold"
- ReqIF.Text:

~~~~text
If The signal strenght network is below" NetworkSignalStrengthAlarmThreshold ", then AL01 " Network signal strength below limit" would be sent.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.988+01:00`

### 53. adr-10341

- ReqIF ID: `rmf-6f14b2a3-a202-4728-8015-f41625a9a4fc`
- ReqIF.ChapterName: The module will send the alarms to MQTT Broker in case errors are detected with...
- ReqIF.Text:

~~~~text
The module will send the alarms to MQTT Broker in case errors are detected with the time stamp. Refer to chapter "Real time alarm message format." of document MQTT Interface .
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.128+01:00`

### 54. adr-10340

- ReqIF ID: `rmf-c3244f4d-7bc3-4b18-a416-1941ab9f4527`
- ReqIF.ChapterName: flag will be sent with all timestamps where the alarm occured.
- ReqIF.Text:

~~~~text
flag will be sent with all timestamps where the alarm occured.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:21.081+01:00`

### 55. adr-10336

- ReqIF ID: `rmf-bb56d680-7337-4a0e-84d4-2dbccc3c9d1d`
- ReqIF.ChapterName: The module will include in the last column of measurement line of CSV file param...
- ReqIF.Text:

~~~~text
The module will include in the last column of measurement line of CSV file parameter "faultstatus". Please note it's host device only.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.894+01:00`

### 56. adr-10335

- ReqIF ID: `rmf-2856f118-bd11-4caf-80b6-6a2de9c88b86`
- ReqIF.ChapterName: The module will send a real time alarm through MQTT communication channel in cas...
- ReqIF.Text:

~~~~text
The module will send a real time alarm through MQTT communication channel in case parameter "faultstatus" is different from previous reading.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.847+01:00`

### 57. adr-10337

- ReqIF ID: `rmf-32649e4a-df00-4fa0-87dd-308ce5c15221`
- ReqIF.ChapterName: A "ModuleAlarmMask" will be supported for the customer to select what alarms of the...
- ReqIF.Text:

~~~~text
A " ModuleAlarmMask " will be supported for the customer to select what alarms of the module shall trigger the real-time alarm, i.e. the real-time alarm is activated if the corresponding bit of the alarm mask is set to 1. The alarm mask functions shall not disable the real-time alarms of the host device.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:20.941+01:00`

### 58. adr-10407

- ReqIF ID: `rmf-d3245649-d6e4-4593-8c9b-ada52016b158`
- ReqIF.ChapterName: Parameters as define in 4Gmodule parameters list (A5E38431885A) will be configur...
- ReqIF.Text:

~~~~text
Parameters as define in 4Gmodule parameters list (A5E38431885A) will be configurable through MQTT configuration channel.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.347+01:00`

### 59. adr-10406

- ReqIF ID: `rmf-689669e5-e5eb-4aac-84a2-0818ac76198b`
- ReqIF.ChapterName: Clock synchronization of the module will be done through synchronisation in UNIX...
- ReqIF.Text:

~~~~text
Clock synchronization of the module will be done through synchronisation in UNIX-UTC timing provided by thingstream server. . This clock will be synchronized regularly.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.300+01:00`

### 60. adr-10409

- ReqIF ID: `rmf-dc9db2ad-0c44-4534-9cbd-93efd9418210`
- ReqIF.ChapterName: the firmware of the module will be over the air updatable (postpone to release 2...
- ReqIF.Text:

~~~~text
the firmware of the module will be over the air updatable (postpone to release 2).
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.441+01:00`

### 61. adr-10408

- ReqIF ID: `rmf-4f8b7e55-24db-4115-b2fb-b94077f4043a`
- ReqIF.ChapterName: Battery capacity in the process values wil be read out from following TRN modbus...
- ReqIF.Text:

~~~~text
Battery capacity in the process values wil be read out from following TRN modbus register "BatteryCapacity" (3030)
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.394+01:00`

### 62. adr-10403

- ReqIF ID: `rmf-c487986b-59d9-4b7f-a665-784a63373cd4`
- ReqIF.ChapterName: a leakage detection test will be launched on demand. Three parameters will be used...
- ReqIF.Text:

~~~~text
a leakage detection test will be launched on demand. Three parameters will be used to start this test. Start parameter and period parameter. There is a parameter "LeakageWindowssControl" to enable this functionnality , if period parameter is set to a valid period it will be repeated each 24h hours. at 15 sec interval if the actual excitation freq (reg 238) = 1/15Hz, 1/5Hz, 1.5625Hz, 3.125Hz, 6.25Hz, orÂ at 30 sec interval if the actual excitation freq (reg 238) = 1/30Hz, orÂ at 60 sec interval if the actual excitation freq (reg 238) = 1/60Hz. Mapping values of ExcitationFreqNo (238) areÂ : 0= 1/15Hz 1= 1/5Hz 2= 1.5625Hz 3= 3.125Hz 4= 6.25Hz 5= 1/30Hz 6= 1/60Hz
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.144+01:00`

### 63. adr-10402

- ReqIF ID: `rmf-a8ed9633-a8f4-489e-8be3-f5d2ed8c5cb0`
- ReqIF.ChapterName: Firmware over the air (FOTA) of the uC and the cellular modem are not foreseen i...
- ReqIF.Text:

~~~~text
Firmware over the air (FOTA) of the uC and the cellular modem are not foreseen in this release.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.097+01:00`

### 64. adr-10405

- ReqIF ID: `rmf-a9d0e326-2bb1-414a-b47b-fbcf0290ca4b`
- ReqIF.ChapterName: SD card data are unencrypted.
- ReqIF.Text:

~~~~text
SD card data are unencrypted.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.238+01:00`

### 65. adr-10404

- ReqIF ID: `rmf-3a8f10a2-d09c-4c0b-b8c9-8952b70d5515`
- ReqIF.ChapterName: Commissioning is defined as the action of plugging the 4g module on the host dev...
- ReqIF.Text:

~~~~text
Commissioning is defined as the action of plugging the 4g module on the host device for the first time. Communication module shall communicate by default.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.191+01:00`

### 66. adr-10399

- ReqIF ID: `rmf-e656fa5e-618f-4e1f-9e91-839c771c83e4`
- ReqIF.ChapterName: During each power up a LED placed on the module and visible when the enclosure i...
- ReqIF.Text:

~~~~text
During each power up a LED placed on the module and visible when the enclosure is not on the transmitter will give following status : module on/off (green); module connected to thingstream (blue LED); both LED on for 5 min.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.956+01:00`

### 67. adr-10397

- ReqIF ID: `rmf-854899f5-deae-427f-92db-740fe556ab49`
- ReqIF.ChapterName: The module will be hot swappable without damaging the Transmitter. Perennity of...
- ReqIF.Text:

~~~~text
The module will be hot swappable without damaging the Transmitter. Perennity of data on the module is not guaranteed in case the FunctionButton is not used properly.
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:23.847+01:00`

### 68. adr-10415

- ReqIF ID: `rmf-65e40220-f4bb-4376-a305-2873a4ebd0d7`
- ReqIF.ChapterName: The communication module will be available as spare part
- ReqIF.Text:

~~~~text
The communication module will be available as spare part
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.738+01:00`

### 69. adr-10417

- ReqIF ID: `rmf-70be84df-d4a0-4a6d-9dbb-9c88bcd86425`
- ReqIF.ChapterName: Antenna will be available as spare part
- ReqIF.Text:

~~~~text
Antenna will be available as spare part
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.832+01:00`

### 70. adr-10412

- ReqIF ID: `rmf-c7f5cd23-1665-48a2-960f-8c76c966ea9a`
- ReqIF.ChapterName: The voltage input cable will be available as spare part
- ReqIF.Text:

~~~~text
The voltage input cable will be available as spare part
~~~~
- Created by: `Z00407EJ`
- Created on: `2021-01-26T16:28:24.597+01:00`

## 5. Связи

Все 26 отношений имеют тип `fulfills`. SOURCE существует; TARGET отсутствует среди экспортированных SpecObject. Оригинальные записи остаются в ReqIF, но не создают связи GRACE с фиктивными концами.

| № | Relation ID | SOURCE | Отсутствующий TARGET |
|---:|---|---|---|
| 1 | `rmf-dcba3a5a-d1fb-4047-accd-cc5430ba9508` | `rmf-c2345a84-ce17-46a1-9a3b-87db23bdf73c` | `rmf-d05859e8-cbb1-4d44-a5c9-f1302d84356b` |
| 2 | `rmf-30316e4f-0ccf-449f-9338-40898d26cde4` | `rmf-90467e41-5651-44a8-888a-36c37f9a90a0` | `rmf-fe3aa783-f231-439b-9ac0-b8a4a12faa28` |
| 3 | `rmf-8e304b49-d386-4071-a65b-96d2fdc51279` | `rmf-2757d5f2-5180-4c04-99d0-176cb071e6a7` | `rmf-60c855fd-14a9-4421-909b-31fbcbc03f60` |
| 4 | `rmf-e0144d9a-7a44-4d72-b5e3-dec7d1d1bd01` | `rmf-6024ded0-603e-4282-93c1-dfd209800c1b` | `rmf-85ec44fe-1d22-4bb6-956a-029ea077ff2e` |
| 5 | `rmf-48b1445d-dab1-4c63-8cf7-c897c6ae4f02` | `rmf-55174b6a-289c-42f1-877d-46a8e6f1b4f1` | `rmf-33ea43d6-195f-4c98-88b4-a1b1a9442552` |
| 6 | `rmf-a0b763d9-7f82-4c13-8f40-1db484340d6b` | `rmf-12297089-eea8-4bde-a866-19fa8e2b7902` | `rmf-0fc68cc5-bd97-4b9a-aa8e-c2c0ace00aca` |
| 7 | `rmf-baa87900-f954-4665-9a2c-e95f877a51fc` | `rmf-f465ea3a-79ef-4fef-bc13-88c8f98b84a5` | `rmf-2d3f8c46-36b7-4a8a-9a4c-939bdadcb0f5` |
| 8 | `rmf-e1af12cb-d767-4186-a803-ac7d44b3e2ba` | `rmf-39b5cd09-37f9-42dc-95f4-c7f5e28b67c4` | `rmf-9fd75be9-da83-4a08-9142-b7d64edeb3a1` |
| 9 | `rmf-45b7e55c-1d60-4fbc-a70c-82670852835d` | `rmf-39b5cd09-37f9-42dc-95f4-c7f5e28b67c4` | `rmf-03287a36-554c-4748-81bb-688f8ec78f72` |
| 10 | `rmf-0ebc9fa1-1e26-400d-bbdf-b27dbb91e3a0` | `rmf-9f568401-5b3d-4621-b1a8-4d7f78d5cf42` | `rmf-e70fe503-6699-46ae-b640-4d8392f9fc13` |
| 11 | `rmf-0de96ec1-f202-4198-aa48-8663a3bf3233` | `rmf-42ba9181-38c9-47c7-b949-c7227bd14c9f` | `rmf-39ab40bd-933f-48cb-a4d8-313dcc7c885d` |
| 12 | `rmf-87f98145-209e-4dc7-89c2-5be2b2adb619` | `rmf-48e30a43-bdb8-4a07-8bea-8805a0a07572` | `rmf-25f71507-382b-466a-a2bd-f1993a658200` |
| 13 | `rmf-b3038ecf-087a-4582-9dd2-54278fe3bda6` | `rmf-9dec5683-7721-4809-a204-7b9777f991ae` | `rmf-f3df1e27-7269-4142-8b9c-117be64b62a3` |
| 14 | `rmf-563e75ab-5d6d-4e32-85ce-fc7eb0661490` | `rmf-92216a53-a63e-4fee-a531-5d6b20a5037d` | `rmf-f5a558ae-5ee9-4964-b0b3-befc8d04f64d` |
| 15 | `rmf-df049325-9af8-480b-9b33-64bba0672cd7` | `rmf-79ad8814-5de1-4c9f-a97f-607e5880cf06` | `rmf-a41849a2-0846-436e-a653-9b54d4838e01` |
| 16 | `rmf-944c55e7-40fd-498d-89a8-fc66730ff72b` | `rmf-facd3a8f-34d1-4336-8f5e-84442cf3d4a5` | `rmf-82074d06-923d-49be-b264-40e0cec2747e` |
| 17 | `rmf-a71dc021-04a2-451f-bb9a-9ef33e96730d` | `rmf-d075d01b-2bcc-448e-a8f6-2d96b507c99b` | `rmf-391ccc15-5fc9-433e-8536-8c46fa85c2bf` |
| 18 | `rmf-1895cb52-9cab-4b42-9fb7-0794a40147d8` | `rmf-3c9c3fbb-3052-4d49-9b44-bfdd6b787090` | `rmf-c293bd25-498e-459c-b8a2-cad58876e8e1` |
| 19 | `rmf-dd7384f0-d341-4c21-98d7-b5b385f37ef6` | `rmf-e09775fb-33c1-4860-8b89-41124a686a45` | `rmf-14aef2f4-ae11-42a6-8196-9c86ced12f97` |
| 20 | `rmf-38e5cc1a-4d38-4347-b0b2-13ef99b4d7ab` | `rmf-78385236-1e95-4fc3-b73a-413e8014ec20` | `rmf-1e522700-7ba4-4a52-9432-77bebe108f0a` |
| 21 | `rmf-27a66efc-b82a-4178-ace2-3993976bacbf` | `rmf-a39c3d94-45cc-473b-96d1-b5afa7ebfd53` | `rmf-00f3e84a-251e-4d1c-ba54-4f26c768ca2b` |
| 22 | `rmf-0470b801-7181-4cff-962c-4945b5d624d1` | `rmf-9634e0e6-cd37-45eb-ac1c-98205d0600ec` | `rmf-00f3e84a-251e-4d1c-ba54-4f26c768ca2b` |
| 23 | `rmf-c458b485-abf1-49b3-a73e-56b54b4a1e0e` | `rmf-6ad1a3af-bfb6-4c79-94c5-5f845e3daca4` | `rmf-228d7a55-2dca-4531-8e44-e473dc2ea51c` |
| 24 | `rmf-519b1f9b-cfb8-4889-b40d-3ccc07fde0d9` | `rmf-38e09f0b-ed02-4141-92aa-0b2692d27ca0` | `rmf-62b981de-6d5e-42c2-8fb8-37c52310d67d` |
| 25 | `rmf-06c60b6a-bc40-4211-bb97-9b5966ace60f` | `rmf-29de3010-a096-4242-a329-385674b07814` | `rmf-5fc6151d-a88d-45af-9f74-968daea2ff9e` |
| 26 | `rmf-81085895-dcd7-4db2-b238-57b2275bbe5f` | `rmf-925ceba4-cd00-43a7-9b0b-ebe5e4c19a76` | `rmf-f0e7b409-602a-479b-b529-1e617a488f1b` |

## 6. Пометки статуса из источника

- `Remote qualification certificate (to be discussed with web APP team)`.
- `Voltage input readings (nice to have), to be discussed during MF concept`.
- `Usability/commissioning (needs to be discussed)`.
- `adr-10369`: eSIM option is not used for release 1.
- `adr-10409`: firmware over-the-air update postponed to release 2.
- `adr-10402`: FOTA of the microcontroller and cellular modem is not foreseen in this release.

Упоминаются внешние документы `A5E5009542A`, `A5E48591235A`, `A5E38431885A` и другие; их содержимое не вложено в ReqIF.

## 7. Недостающие сведения для GRACE

ReqIF не объявляет явно цель системы, акторов, AAG use cases, бизнес-процессы, предметные сущности, состояния, инварианты, ошибки, критерии результата, внешние системы и направления взаимодействия в терминах GRACE/GRACE-ARP.

Упоминания `customer`, `Web APP`, `cloud based solution`, `Thingstream`, `MQTT Broker`, `MNO`, `MAG8000 Transmitter` и `Modbus` сами по себе не устанавливают границу системы, роль участника или направление взаимодействия.

## 8. Открытые решения

1. Определить границу системы.
2. Определить baseline/release scope, включая nice-to-have, обсуждаемые и отложенные функции.
3. Решить, можно ли использовать `ReqIF.ChapterName` как содержание двух Feature с пустым `ReqIF.Text`.
4. Предоставить или исключить из анализа упомянутые технические документы.
5. Подтвердить цель, акторов, внешние системы и сценарии.

До согласования этих пунктов GRACE-классификация не назначается автоматически по ключевым словам или по типу Polarion `Feature`.