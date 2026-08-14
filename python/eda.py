import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# MARKETING CAMPAIGN — EXPLORATORY DATA ANALYSIS
# ============================================================

print("=" * 60)
print("MARKETING CAMPAIGN EXPLORATORY DATA ANALYSIS")
print("=" * 60)


# ============================================================
# 1. PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "cleaned"
    / "marketing_campaign_cleaned.csv"
)

REPORTS_DIR = PROJECT_ROOT / "reports"

REPORTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 2. LOAD DATA
# ============================================================

print("\n" + "=" * 60)
print("LOADING DATA")
print("=" * 60)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Cleaned dataset not found:\n{INPUT_FILE}"
    )

df = pd.read_csv(INPUT_FILE)

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        errors="coerce"
    )

print("\nDataset Shape:", df.shape)


# ============================================================
# 3. DATASET OVERVIEW
# ============================================================

print("\n" + "=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ============================================================
# 4. DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

numeric_columns = df.select_dtypes(
    include=np.number
).columns

print(
    df[numeric_columns]
    .describe()
    .round(2)
)


# ============================================================
# 5. CAMPAIGN TYPE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("CAMPAIGN TYPE ANALYSIS")
print("=" * 60)

campaign_summary = (
    df.groupby("Campaign_Type")
    .agg(
        Campaigns=("Campaign_ID", "count"),
        Revenue=("Revenue", "sum"),
        Average_ROI=("ROI", "mean"),
        Average_Conversions=("Conversions", "mean"),
        Average_Engagement=("Engagement_Score", "mean")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)

print(
    campaign_summary.round(2)
)


# ============================================================
# 6. CUSTOMER SEGMENT ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("CUSTOMER SEGMENT ANALYSIS")
print("=" * 60)

segment_summary = (
    df.groupby("Customer_Segment")
    .agg(
        Campaigns=("Campaign_ID", "count"),
        Revenue=("Revenue", "sum"),
        Average_ROI=("ROI", "mean"),
        Average_Conversions=("Conversions", "mean"),
        Average_Engagement=("Engagement_Score", "mean")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)

print(
    segment_summary.round(2)
)


# ============================================================
# 7. CHANNEL ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("CHANNEL ANALYSIS")
print("=" * 60)

channel_summary = (
    df.groupby("Channel_Used")
    .agg(
        Campaigns=("Campaign_ID", "count"),
        Revenue=("Revenue", "sum"),
        Average_ROI=("ROI", "mean")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)

print("\nTop 10 Channels by Revenue:")

print(
    channel_summary
    .head(10)
    .round(2)
)


# ============================================================
# 8. TOP CAMPAIGNS BY ROI
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 CAMPAIGNS BY ROI")
print("=" * 60)

top_roi_campaigns = (
    df[
        [
            "Campaign_ID",
            "Campaign_Type",
            "Customer_Segment",
            "Revenue",
            "ROI",
            "Conversions"
        ]
    ]
    .sort_values(
        "ROI",
        ascending=False
    )
    .head(10)
)

print(
    top_roi_campaigns.round(2)
)


# ============================================================
# 9. TOP CAMPAIGNS BY REVENUE
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 CAMPAIGNS BY REVENUE")
print("=" * 60)

top_revenue_campaigns = (
    df[
        [
            "Campaign_ID",
            "Campaign_Type",
            "Customer_Segment",
            "Revenue",
            "ROI",
            "Conversions"
        ]
    ]
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(10)
)

print(
    top_revenue_campaigns.round(2)
)


# ============================================================
# 10. CORRELATION ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("CORRELATION WITH ROI")
print("=" * 60)

correlation_matrix = (
    df[numeric_columns]
    .corr()
)

roi_correlation = (
    correlation_matrix["ROI"]
    .sort_values(
        ascending=False
    )
)

print(
    roi_correlation.round(4)
)


# ============================================================
# 11. ROI DISTRIBUTION
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.hist(
    df["ROI"],
    bins=50
)

plt.title(
    "ROI Distribution"
)

plt.xlabel("ROI")

plt.ylabel(
    "Number of Campaigns"
)

plt.tight_layout()

plt.savefig(
    REPORTS_DIR / "roi_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 12. REVENUE DISTRIBUTION
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.hist(
    df["Revenue"],
    bins=50
)

plt.title(
    "Revenue Distribution"
)

plt.xlabel("Revenue")

plt.ylabel(
    "Number of Campaigns"
)

plt.tight_layout()

plt.savefig(
    REPORTS_DIR / "revenue_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 13. REVENUE BY CAMPAIGN TYPE
# ============================================================

campaign_revenue = (
    df.groupby("Campaign_Type")["Revenue"]
    .sum()
    .sort_values(
        ascending=False
    )
)

plt.figure(
    figsize=(10, 6)
)

plt.bar(
    campaign_revenue.index,
    campaign_revenue.values
)

plt.title(
    "Revenue by Campaign Type"
)

plt.xlabel(
    "Campaign Type"
)

plt.ylabel(
    "Total Revenue"
)

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    REPORTS_DIR / "revenue_by_campaign_type.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 14. ROI BY CAMPAIGN TYPE
# ============================================================

campaign_roi = (
    df.groupby("Campaign_Type")["ROI"]
    .mean()
    .sort_values(
        ascending=False
    )
)

plt.figure(
    figsize=(10, 6)
)

plt.bar(
    campaign_roi.index,
    campaign_roi.values
)

plt.title(
    "Average ROI by Campaign Type"
)

plt.xlabel(
    "Campaign Type"
)

plt.ylabel(
    "Average ROI"
)

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    REPORTS_DIR / "roi_by_campaign_type.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 15. REVENUE BY CUSTOMER SEGMENT
# ============================================================

segment_revenue = (
    df.groupby("Customer_Segment")["Revenue"]
    .sum()
    .sort_values(
        ascending=False
    )
)

plt.figure(
    figsize=(10, 6)
)

plt.bar(
    segment_revenue.index,
    segment_revenue.values
)

plt.title(
    "Revenue by Customer Segment"
)

plt.xlabel(
    "Customer Segment"
)

plt.ylabel(
    "Total Revenue"
)

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    REPORTS_DIR / "revenue_by_customer_segment.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 16. FINAL BUSINESS INSIGHTS
# ============================================================

best_campaign_type = (
    campaign_summary["Revenue"]
    .idxmax()
)

best_roi_campaign_type = (
    campaign_summary["Average_ROI"]
    .idxmax()
)

best_segment = (
    segment_summary["Revenue"]
    .idxmax()
)

best_segment_roi = (
    segment_summary["Average_ROI"]
    .idxmax()
)

print("\n" + "=" * 60)
print("KEY BUSINESS INSIGHTS")
print("=" * 60)

print(
    f"\n1. Highest revenue campaign type: "
    f"{best_campaign_type}"
)

print(
    f"2. Highest average ROI campaign type: "
    f"{best_roi_campaign_type}"
)

print(
    f"3. Highest revenue customer segment: "
    f"{best_segment}"
)

print(
    f"4. Highest average ROI customer segment: "
    f"{best_segment_roi}"
)

print(
    f"5. Strongest ROI correlation: "
    f"{roi_correlation.index[1]} "
    f"({roi_correlation.iloc[1]:.4f})"
)


# ============================================================
# 17. COMPLETION
# ============================================================

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated Reports:")

print(
    "reports/roi_distribution.png"
)

print(
    "reports/revenue_distribution.png"
)

print(
    "reports/revenue_by_campaign_type.png"
)

print(
    "reports/roi_by_campaign_type.png"
)

print(
    "reports/revenue_by_customer_segment.png"
)