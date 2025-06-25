# GazaMaps's Displacement Orders Data Dictionary

| **Variable**               | **Full Variable Name**              | **Dataset Variable Name** | **Unit/Format**        | **Type**          | **Possible Value Ranges** | **Description**                                       | **Data Origin**  |
| -------------------------- | ----------------------------------- | ------------------------- | ---------------------- | ----------------- | ------------------------- | ----------------------------------------------------- | ---------------- |
| ID                         | Unique Displacement Entry ID        | `id`                      | Integer                | Numeric (Integer) | 1 and above               | Unique identifier for the displacement event          | Original dataset |
| Date                       | Date of Displacement Event          | `date`                    | Date (YYYY-MM-DD)      | String            | e.g., "2025-06-20"        | Date the displacement was reported                    | Original dataset |
| Source                     | Source Link                         | `source`                  | URL                    | String (URL)      | Varies                    | Source of the information (e.g., official statements) | Original dataset |
| Link                       | Event Page URL                      | `link`                    | URL                    | String (URL)      | Varies                    | Direct link to detailed event information             | Original dataset |
| Map (IDF)                  | IDF Map URL                         | `map_idf`                 | URL (JPEG image)       | String (URL)      | Varies                    | Map image shared by IDF                               | Original dataset |
| Map (Full)                 | Full Map URL                        | `map_full`                | URL (JPEG image)       | String (URL)      | Varies                    | Full area displacement map                            | Original dataset |
| Map (Zoomed)               | Zoomed Map URL                      | `map_zoom`                | URL (JPEG image)       | String (URL)      | Varies                    | Zoomed-in view of the map                             | Original dataset |
| Displacement Blocks        | Affected Block Numbers              | `displacement_blocks`     | Comma-separated values | String (Text)     | e.g., "606, 607, 719"     | List of block numbers identified for displacement     | Original dataset |
| Labeled Safe Blocks        | Safe Block Numbers                  | `labeled_safe_blocks`     | Comma-separated values | String (Text)     | Varies or empty           | Blocks explicitly marked as safe                      | Original dataset |
| Area of Displacement (km²) | Displacement Area in Sq. Kilometers | `area_sq_km_displacement` | Decimal (e.g., 0.80)   | Numeric (Float)   | ≥ 0.00                    | Total area designated for displacement                | Original dataset |
| Safe Area (km²)            | Labeled Safe Area in Sq. Kilometers | `area_sq_km_labeled_safe` | Decimal (e.g., 0.00)   | Numeric (Float)   | ≥ 0.00                    | Total area labeled safe                               | Original dataset |

---
