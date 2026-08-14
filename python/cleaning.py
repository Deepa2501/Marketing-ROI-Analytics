import pandas as pd
from pathlib import Path


# ============================================================
# MARKETING DATA CLEANING PIPELINE
# ============================================================

print("=" * 60)
print("MARKETING DATA CLEANING PIPELINE")
print("=" * 60)


# ============================================================
# 1. PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "marketing_campaign_raw.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "cleaned"
    / "marketing_campaign_cleaned.csv"
)

print("\nProject Root:")
print(PROJECT_ROOT)

print("\nInput File:")
print(INPUT_FILE)

print("\nOutput File:")
print(OUTPUT_FILE)


# ============================================================
# 2. CHECK INPUT FILE
# ============================================================

if not INPUT_FILE.exists():

    raise FileNotFoundError(
        f"\nInput dataset not found:\n{INPUT_FILE}"
    )


# ============================================================
# 3. LOAD DATA
# ============================================================

print("\n" + "=" * 60)
print("LOADING DATA")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

initial_shape = df.shape

print("\nInitial Dataset Shape:", initial_shape)


# ============================================================
# 4. CLEAN COLUMN NAMES
# ============================================================

print("\n" + "=" * 60)
print("CLEANING COLUMN NAMES")
print("=" * 60)

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_", regex=False)
)

print("\nColumns:")
print(df.columns.tolist())


# ============================================================
# 5. REMOVE DUPLICATES
# ============================================================

print("\n" + "=" * 60)
print("DUPLICATE ANALYSIS")
print("=" * 60)

duplicate_count = df.duplicated().sum()

print("\nDuplicate Rows Found:", duplicate_count)

if duplicate_count > 0:

    df = df.drop_duplicates()

    print(
        "Duplicates Removed:",
        duplicate_count
    )

else:

    print("No duplicate rows found.")


print(
    "Shape After Duplicate Removal:",
    df.shape
)


# ============================================================
# 6. MISSING VALUE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUE ANALYSIS")
print("=" * 60)

missing_before = df.isnull().sum()

total_missing = missing_before.sum()

print("\nTotal Missing Values:", total_missing)

if total_missing > 0:

    print("\nColumns with Missing Values:")

    print(
        missing_before[
            missing_before > 0
        ]
    )

    # Numeric columns → median
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    for column in numeric_columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(
                df[column].median()
            )

    # Categorical columns → Unknown
    categorical_columns = df.select_dtypes(
        include="object"
    ).columns

    for column in categorical_columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(
                "Unknown"
            )

print("\nMissing-value handling completed.")


# ============================================================
# 7. DATE CONVERSION
# ============================================================

print("\n" + "=" * 60)
print("DATE PROCESSING")
print("=" * 60)

if "Date" in df.columns:

    df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

    invalid_dates = df["Date"].isnull().sum()

    print(
        "Invalid Dates:",
        invalid_dates
    )


# ============================================================
# 8. NUMERIC DATA TYPE CONVERSION
# ============================================================

print("\n" + "=" * 60)
print("NUMERIC DATA TYPE CONVERSION")
print("=" * 60)

numeric_columns = [
    "Duration",
    "Impressions",
    "Clicks",
    "Leads",
    "Conversions",
    "Revenue",
    "Acquisition_Cost",
    "ROI",
    "Engagement_Score"
]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

print("\nNumeric columns converted successfully.")


# ============================================================
# 9. HANDLE NUMERIC CONVERSION MISSING VALUES
# ============================================================

for column in numeric_columns:

    if column in df.columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(
                df[column].median()
            )


# ============================================================
# 10. DATA VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("DATA VALIDATION")
print("=" * 60)

validation_columns = {
    "Revenue": "Negative Revenue",
    "Acquisition_Cost": "Negative Acquisition Cost",
    "Conversions": "Negative Conversions",
    "Clicks": "Negative Clicks",
    "Leads": "Negative Leads",
    "Impressions": "Negative Impressions",
    "Duration": "Negative Duration",
    "ROI": "Negative ROI"
}

for column, label in validation_columns.items():

    if column in df.columns:

        count = (
            df[column] < 0
        ).sum()

        print(
            f"{label}: {count}"
        )


# ============================================================
# 11. LOGICAL CONSISTENCY CHECKS
# ============================================================

print("\n" + "=" * 60)
print("LOGICAL CONSISTENCY CHECKS")
print("=" * 60)

if (
    "Conversions" in df.columns
    and "Leads" in df.columns
):

    invalid_conversions = (
        df["Conversions"] > df["Leads"]
    ).sum()

    print(
        "Conversions > Leads:",
        invalid_conversions
    )


if (
    "Clicks" in df.columns
    and "Impressions" in df.columns
):

    invalid_clicks = (
        df["Clicks"] > df["Impressions"]
    ).sum()

    print(
        "Clicks > Impressions:",
        invalid_clicks
    )


if (
    "Leads" in df.columns
    and "Clicks" in df.columns
):

    invalid_leads = (
        df["Leads"] > df["Clicks"]
    ).sum()

    print(
        "Leads > Clicks:",
        invalid_leads
    )


# ============================================================
# 12. FINAL QUALITY CHECK
# ============================================================

print("\n" + "=" * 60)
print("FINAL QUALITY CHECK")
print("=" * 60)

final_missing = df.isnull().sum().sum()

final_duplicates = df.duplicated().sum()

print(
    "\nRemaining Missing Values:",
    final_missing
)

print(
    "Remaining Duplicate Rows:",
    final_duplicates
)


# ============================================================
# 13. FINAL DATASET SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("FINAL DATASET SUMMARY")
print("=" * 60)

print(
    "\nInitial Shape:",
    initial_shape
)

print(
    "Final Shape:",
    df.shape
)

print(
    "Rows Removed:",
    initial_shape[0] - df.shape[0]
)

print(
    "Columns:",
    df.shape[1]
)


# ============================================================
# 14. SAVE CLEANED DATASET
# ============================================================

print("\n" + "=" * 60)
print("SAVING CLEANED DATA")
print("=" * 60)

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print(
    "\nCleaned dataset saved successfully:"
)

print(OUTPUT_FILE)


# ============================================================
# 15. FINAL SUCCESS
# ============================================================

print("\n" + "=" * 60)
print("CLEANING PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)

print(
    "\nFinal Dataset Shape:",
    df.shape
)

print(
    "Missing Values:",
    df.isnull().sum().sum()
)

print(
    "Duplicate Rows:",
    df.duplicated().sum()
)

print("\nOutput File:")
print(OUTPUT_FILE)

print("\n" + "=" * 60)