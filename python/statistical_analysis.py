import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# ---------------------------------------------
# LOAD DATA
# ---------------------------------------------

file_path = "data/cleaned/marketing_campaign_dataset.xlsx"

df = pd.read_excel(file_path)

print("=" * 50)
print("ADVANCED STATISTICAL ANALYSIS")
print("=" * 50)

print("\nDataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nNumeric Columns:")
print(df.select_dtypes(include=np.number).columns.tolist())

# ---------------------------------------------
# CORRELATION ANALYSIS
# ---------------------------------------------

numeric_df = df.select_dtypes(include=np.number)

correlation_matrix = numeric_df.corr()

print("\n" + "=" * 50)
print("CORRELATION WITH ROI")
print("=" * 50)

roi_correlation = (
    correlation_matrix["ROI"]
    .sort_values(ascending=False)
)

print(roi_correlation)

print("\n" + "=" * 50)
print("CORRELATION WITH REVENUE")
print("=" * 50)

revenue_correlation = (
    correlation_matrix["Revenue"]
    .sort_values(ascending=False)
)

print(revenue_correlation)

# ---------------------------------------------
# CORRELATION SIGNIFICANCE TEST
# ---------------------------------------------

print("\n" + "=" * 50)
print("STATISTICAL SIGNIFICANCE OF KEY CORRELATIONS")
print("=" * 50)

tests = [
    ("Revenue vs ROI", df["Revenue"], df["ROI"]),
    ("Conversions vs Revenue", df["Conversions"], df["Revenue"]),
    ("Leads vs Revenue", df["Leads"], df["Revenue"]),
    ("Clicks vs Revenue", df["Clicks"], df["Revenue"]),
    ("Acquisition Cost vs Revenue",
     df["Acquisition_Cost"], df["Revenue"])
]

for name, x, y in tests:
    r, p_value = pearsonr(x, y)

    print(f"\n{name}")
    print(f"Correlation: {r:.4f}")
    print(f"P-value: {p_value:.6f}")

    if p_value < 0.05:
        print("Result: Statistically Significant")
    else:
        print("Result: Not Statistically Significant")

# ---------------------------------------------
# CORRELATION HEATMAP
# ---------------------------------------------

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))

plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    aspect="auto"
)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix.columns)):
        plt.text(
            j,
            i,
            f"{correlation_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Marketing Metrics Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "reports/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nCorrelation heatmap saved successfully:")
print("reports/correlation_heatmap.png")

# ---------------------------------------------
# OUTLIER ANALYSIS USING IQR
# ---------------------------------------------

print("\n" + "=" * 50)
print("OUTLIER ANALYSIS")
print("=" * 50)

metrics = [
    "Revenue",
    "ROI",
    "Acquisition_Cost",
    "Conversions"
]

for column in metrics:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(f"\n{column}")
    print("Q1:", round(Q1, 2))
    print("Q3:", round(Q3, 2))
    print("Lower Bound:", round(lower_bound, 2))
    print("Upper Bound:", round(upper_bound, 2))
    print("Outliers:", len(outliers))
    print(
        "Outlier Percentage:",
        round(len(outliers) / len(df) * 100, 2),
        "%"
    )

# ---------------------------------------------
# ROI OUTLIERS BY CAMPAIGN TYPE
# ---------------------------------------------

Q1 = df["ROI"].quantile(0.25)
Q3 = df["ROI"].quantile(0.75)

IQR = Q3 - Q1

upper_bound = Q3 + 1.5 * IQR

roi_outliers = df[df["ROI"] > upper_bound]

outlier_summary = (
    roi_outliers
    .groupby("Campaign_Type")
    .agg(
        Outlier_Campaigns=("Campaign_ID", "count"),
        Average_ROI=("ROI", "mean"),
        Total_Revenue=("Revenue", "sum")
    )
    .sort_values(
        "Outlier_Campaigns",
        ascending=False
    )
)

print("\n" + "=" * 50)
print("HIGH-ROI OUTLIERS BY CAMPAIGN TYPE")
print("=" * 50)

print(outlier_summary.round(2))

# ---------------------------------------------
# DISTRIBUTION ANALYSIS
# ---------------------------------------------

print("\n" + "=" * 50)
print("DISTRIBUTION ANALYSIS")
print("=" * 50)

metrics = [
    "Revenue",
    "ROI",
    "Acquisition_Cost",
    "Conversions"
]

for column in metrics:

    skewness = df[column].skew()

    print(f"\n{column}")
    print("Skewness:", round(skewness, 4))

    if skewness > 1:
        print("Distribution: Highly Right-Skewed")
    elif skewness > 0.5:
        print("Distribution: Moderately Right-Skewed")
    elif skewness < -1:
        print("Distribution: Highly Left-Skewed")
    elif skewness < -0.5:
        print("Distribution: Moderately Left-Skewed")
    else:
        print("Distribution: Approximately Symmetric")

# ---------------------------------------------
# FINAL STATISTICAL INSIGHTS
# ---------------------------------------------

print("\n" + "=" * 50)
print("FINAL STATISTICAL INSIGHTS")
print("=" * 50)

print("""
1. Revenue has a strong positive relationship with ROI (r = 0.7857).

2. Conversions have the strongest relationship with Revenue
   (r = 0.8790).

3. Acquisition Cost has a negative relationship with Revenue
   (r = -0.4055).

4. All tested correlations were statistically significant
   (p < 0.05).

5. Revenue, ROI, Acquisition Cost, and Conversions are highly
   right-skewed, indicating the presence of high-performing
   and high-cost campaigns.

6. High-value outliers were retained because they may represent
   legitimate business performance rather than data errors.

7. Paid Ads had the highest average ROI among high-ROI outlier
   campaigns (15.39), but outlier performance alone should not
   determine overall campaign strategy.
""")