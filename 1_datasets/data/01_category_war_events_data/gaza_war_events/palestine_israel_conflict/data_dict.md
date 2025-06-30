# Data Dictionary for ACLED's Palestine-Israel conflict Events Data

| **Variable**         | **Name**                     | **Type**    | **Description**                                                    |
| -------------------- | ---------------------------- | ----------- | ------------------------------------------------------------------ |
| `event_id_cnty`      | Event ID (Country)           | String      | Unique identifier per event, with country prefix (e.g., ISR46155). |
| `event_date`         | Event Date                   | Date        | Date the event occurred (YYYY-MM-DD).                              |
| `year`               | Year                         | Integer     | Year extracted from event\_date.                                   |
| `time_precision`     | Time Precision               | Integer     | Indicates how accurate the date is (1 = day, 2 = week, etc.).      |
| `disorder_type`      | Disorder Type                | Categorical | Type of disorder, e.g., "Political violence".                      |
| `event_type`         | Event Type                   | Categorical | High-level classification, e.g., "Explosions/Remote violence".     |
| `sub_event_type`     | Sub Event Type               | Categorical | Specific action type, e.g., "Shelling/artillery/missile attack".   |
| `actor1`             | Primary Actor 1              | Categorical | Actor initiating the action (e.g., "Military Forces of Iran").     |
| `assoc_actor_1`      | Associated Actor 1           | Categorical | Supporting group for actor1 (if any).                              |
| `inter1`             | Actor 1 Type Code            | Integer     | Code describing actor1’s type, e.g., "3" for external forces.      |
| `actor2`             | Target Actor 2               | Categorical | Targeted group or actor.                                           |
| `assoc_actor_2`      | Associated Actor 2           | Categorical | Supporting group for actor2 (if any).                              |
| `inter2`             | Actor 2 Type Code            | Integer     | Code describing actor2’s type.                                     |
| `interaction`        | Actor Interaction Type       | String      | Interaction between actor1 and actor2 types.                       |
| `civilian_targeting` | Civilian Targeting Indicator | String      | Indicates if civilians were directly targeted.                     |
| `iso`                | ISO Code                     | Integer     | ISO country numeric code (e.g., 376 = Israel).                     |
| `region`             | Region Name                  | String      | Name of the larger region (e.g., Middle East).                     |
| `country`            | Country Name                 | String      | Name of the country where the event occurred.                      |
| `admin1`             | Admin Level 1                | String      | First-level administrative division (e.g., Haifa).                 |
| `admin2`             | Admin Level 2                | String      | Second-level administrative division (e.g., Beer Sheva).           |
| `admin3`             | Admin Level 3                | String      | Third-level administrative division (e.g., Hula Basin).            |
| `location`           | Location                     | String      | Specific named place where event occurred.                         |
| `latitude`           | Latitude                     | Float       | Geographic coordinate (decimal degrees).                           |
| `longitude`          | Longitude                    | Float       | Geographic coordinate (decimal degrees).                           |
| `geo_precision`      | Location Precision           | Integer     | Precision code: 1 = city, 2 = region, 3 = rough area.              |
| `source`             | Information Sources          | String      | List of reporting outlets or platforms.                            |
| `source_scale`       | Source Scale                 | String      | Scope of source (e.g., "National", "Local partner-New media").     |
| `notes`              | Notes                        | Text        | Detailed textual description of the event.                         |
| `fatalities`         | Fatalities Count             | Integer     | Number of deaths caused by the event (0+).                         |
| `tags`               | Tags                         | String      | Optional tags (e.g., classification, theme).                       |
| `timestamp`          | Data Timestamp               | Integer     | UNIX timestamp of last update (e.g., 1750721820).                  |
