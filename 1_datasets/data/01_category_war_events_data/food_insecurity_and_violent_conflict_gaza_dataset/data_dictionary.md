# Data dictionary for OCHA's  FIVC-Gaza Dataset

|Variable|Full Variable Name|Dataset Variable Name|Unit/Format|Type|Possible Value Ranges|Description|Data Origin|
|--------|------------------|---------------------|-----------|----|---------------------|-----------|-----------|
|Event ID|Unique Event Identifier|`ID`|Numeric|Categorical|ranges from (3070-3353)|Identifier|original dataset|
|Event Date|Date of the event|`Date`|Date (e.g.,12/3/2023)|string|(12/3/2023-5/26/2024)|The date the event occurred|original dataset|
|country|country name|`country`|text|Categorical|e.g., Palestine|Country where event occurred|original dataset|
|Admin 1|First Administrative Division|`Admin 1`|text|Categorical|e.g., Gaza|First-level geographic division|Original dataset|
|Admin 2|Second Administrative Division|`Admin 2`|text|Categorical|varies|Second-level geographic division|Original dataset|
|Location|Specific Location|`Location`|text or null|Categorical|varies or null|indicate names of approximate geographic locations of incidents|Original dataset|
|Reported Perpetrator Name|party in charge of the event|`Reported Perpetrator Name`|text|Categorical|varies| Reasonable assumptions were made in the coding of the 'Reported Means of Action' (Column G) employed in given incidents|original dataset|
|Reported Means of Action|Reported Means of Action|`Reported Means of Action`|text|Categorical|varies e.g, Air or Drone Strike|The specific method or instrument reported to have been used in the commission of the act|original dataset|
|Object Affected|type/role of the Object Affected|`Object Affected`|text|Categorical|Varies e.g, Food Supply Chains|the object affected by the action|original dataset|
|Sub-Object Affected|the exact object that was affected|`Sub-Object Affected`|text|Categorical|varies e.g, Bakery|the exact name of the object that was affected by the action|Original dataset|
|Latitude|Geographic Latitude|`Latitude`|Decimal|Numeric (Float)|31. |Latitude of the event's location|Original dataset|
|Longitude|Geographic Longitude|`Longitude`|Decimal|Numeric (Float)|34. |Longitude of the event's location|Original dataset|
|Geo-Precision|Geographic Accuracy Level|`Geo-Precision`|integer/text|string/Numeric (Integer)|varies|Level of geographic location certainty|Original dataset|
