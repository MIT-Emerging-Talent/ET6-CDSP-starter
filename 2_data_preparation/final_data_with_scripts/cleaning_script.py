import pandas as pd

"""
This dataset was mostly clean. We removed some irrelevant columns to focus on useful features.  
We also confirmed there are no missing values or duplicate rows.  
The data is now ready for analysis.

"""

# loading the data
df = pd.read_csv("dynamic_supply_chain_logistics_dataset.csv")

# print("Data loaded successfully." , df)

# clearing the data

# removing some of the whole columns
df = df.drop(
    columns=[
        "vehicle_gps_latitude",
        "vehicle_gps_longitude",
        "fuel_consumption_rate",
    ]
)

# print("Columns removed successfully." ,df)
# # Now we have only 23 columns left in the dataframe


# let check if there are any null values in the dataframe
if df.isnull().values.any():
    print("There are null values in the dataframe.")
else:
    print("There are no null values in the dataframe.")

# Now, let's check if there are any diq duplicates in the dataframe
if df.duplicated().any():
    print("There are duplicates in the dataframe.")
else:
    print("There are no duplicates in the dataframe.")

# Now let's make the changes to the CSV file

df.to_csv("cleaned_data.csv", index=False)

print("Data cleared and saved to cleaned_data.csv")
