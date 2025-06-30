import os

import pandas as pd

# Define file paths
RAW_DATA_PATH = "../1_datasets/raw_data/FRBNY-SCE-Credit-Access-complete_microdata.xlsx"
OUTPUT_DIR = "../1_datasets/processed_datasets"
OUTPUT_FILE = f"{OUTPUT_DIR}/FRBNY_SCE_Credit_Access_cleaned.csv"

# Load the raw Excel data (no header)
excel_data = pd.read_excel(
    RAW_DATA_PATH,
    sheet_name="Data",
    header=None,
)

# Extract column names from the second row (index 1)
column_names = excel_data.iloc[1].tolist()
# Extract the actual data, starting from the third row
survey_data = excel_data.iloc[2:].reset_index(drop=True)
survey_data.columns = column_names

# Remove completely empty rows and columns
survey_data = survey_data.dropna(how="all")
survey_data = survey_data.dropna(axis=1, how="all")

# Remove duplicate rows
survey_data = survey_data.drop_duplicates()

# Clean column names: replace spaces with underscores, remove special characters, lowercase
cleaned_column_names = []
for col in survey_data.columns:
    if pd.isna(col):
        cleaned_column_names.append("unnamed_column")
    else:
        col_str = str(col).strip().replace(" ", "_").replace("-", "_")
        col_str = "".join(c for c in col_str if c.isalnum() or c == "_")
        if col_str and not col_str[0].isalpha():
            col_str = "col_" + col_str
        cleaned_column_names.append(col_str.lower())
survey_data.columns = cleaned_column_names

# Rename columns using the provided mapping
column_rename_map = {
    "userid": "respondent_id",
    "date": "survey_date",
    "weight": "sampling_weight",
    "n1_1": "has_credit_card",
    "n1_2": "has_mortgage",
    "n1_3": "has_student_loan",
    "n1_4": "has_home_based_loan",
    "n1_5": "has_auto_loan",
    "n1_6": "has_other_personal_loan",
    "n1_7": "has_no_credit_products",
    "n2_1": "balance_credit_card_usd",
    "n2_2": "balance_mortgage_usd",
    "n2_3": "balance_student_loan_usd",
    "n2_4": "balance_home_loan_usd",
    "n2_5": "balance_auto_loan_usd",
    "n2_6": "balance_other_loans_usd",
    "n2b_1": "balance_credit_card_category",
    "n2b_2": "balance_mortgage_category",
    "n2b_3": "balance_student_loan_category",
    "n2b_4": "balance_home_loan_category",
    "n2b_5": "balance_auto_loan_category",
    "n2b_6": "balance_other_loan_category",
    "n3": "maxed_out_credit_card_past_year",
    "n4_1": "applied_credit_card_past_year",
    "n4_2": "applied_mortgage_past_year",
    "n4_3": "applied_auto_loan_past_year",
    "n4_4": "requested_credit_card_limit_increase",
    "n4_5": "requested_existing_loan_limit_increase",
    "n4_6": "requested_mortgage_refinance",
    "n4_7": "applied_student_loan_past_year",
    "n5_1": "did_not_apply_satisfied_financial",
    "n5_2": "did_not_apply_time_consuming",
    "n5_3": "did_not_apply_rates_too_high",
    "n5_4": "did_not_apply_dont_know_how",
    "n5_5": "did_not_apply_expected_denial",
    "n6_1": "did_not_apply_credit_card_expected_denial",
    "n6_2": "did_not_apply_mortgage_expected_denial",
    "n6_3": "did_not_apply_auto_loan_expected_denial",
    "n6_4": "did_not_apply_cc_limit_increase_expected_denial",
    "n6_5": "did_not_apply_loan_limit_increase_expected_denial",
    "n6_6": "did_not_apply_refinance_expected_denial",
    "n6_7": "did_not_apply_student_loan_expected_denial",
    "n6_8": "none_n6_options_applicable",
    "n7_1": "redundant_did_not_apply_cc_expected_denial",
    "n7_2": "redundant_did_not_apply_mortgage_expected_denial",
    "n7_3": "redundant_did_not_apply_auto_loan_expected_denial",
    "n7_4": "redundant_did_not_apply_cc_limit_increase_expected_denial",
    "n7_5": "redundant_did_not_apply_loan_limit_increase_expected_denial",
    "n7_6": "redundant_did_not_apply_refinance_expected_denial",
    "n7_7": "redundant_did_not_apply_student_loan_expected_denial",
}
survey_data = survey_data.rename(columns=column_rename_map)

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)
# Save cleaned data to CSV
survey_data.to_csv(OUTPUT_FILE, index=False)
