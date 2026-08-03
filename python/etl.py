# ==========================================
# Marketing ROI Analytics - ETL Pipeline
# ==========================================

import pandas as pd
from sqlalchemy import create_engine

# Read Excel File
file_path = r"D:\Marketing-ROI-Analytics\data\cleaned\marketing_campaign_cleaned.xlsx"

df = pd.read_excel(file_path)


# Convert Date column
df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

# Rename columns for PostgreSQL
df.columns = [col.lower() for col in df.columns]
df.columns = df.columns.str.replace(" ", "_")

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Dates:")
print(df["date"].head())

print("\nColumn Names:")
print(df.columns.tolist())

# ==========================================
# PostgreSQL Connection
# ==========================================

engine = create_engine(
    "postgresql+psycopg2://postgres:&hiV1234@localhost:5432/marketing_roi_db"
)

print("\nConnected to PostgreSQL Successfully!")

# ==========================================
# Load Data into PostgreSQL
# ==========================================

df.to_sql(
    name="marketing_campaigns",
    con=engine,
    schema="marketing",
    if_exists="replace",
    index=False
)

print("\nData Loaded Successfully into PostgreSQL!")