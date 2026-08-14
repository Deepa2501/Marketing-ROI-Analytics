import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load cleaned marketing dataset
file_path = "data/cleaned/marketing_campaign_dataset.xlsx"

df = pd.read_excel(file_path)

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
# ---------------------------------------------
# A/B-STYLE TEST: SOCIAL MEDIA vs PAID ADS
# ---------------------------------------------

group_a = df[df["Campaign_Type"] == "Social Media"]["ROI"].dropna()
group_b = df[df["Campaign_Type"] == "Paid Ads"]["ROI"].dropna()

print("\n" + "=" * 50)
print("A/B-STYLE TEST: ROI COMPARISON")
print("=" * 50)

print("\nGroup A: Social Media")
print("Number of campaigns:", len(group_a))
print("Average ROI:", round(group_a.mean(), 2))
print("Median ROI:", round(group_a.median(), 2))

print("\nGroup B: Paid Ads")
print("Number of campaigns:", len(group_b))
print("Average ROI:", round(group_b.mean(), 2))
print("Median ROI:", round(group_b.median(), 2))

# ---------------------------------------------
# WELCH'S T-TEST
# ---------------------------------------------

t_stat, p_value = ttest_ind(
    group_a,
    group_b,
    equal_var=False
)

print("\n" + "=" * 50)
print("WELCH'S T-TEST RESULT")
print("=" * 50)

print("T-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 6))

alpha = 0.05

if p_value < alpha:
    print("\nResult: Statistically Significant")
    print("We reject the null hypothesis.")
else:
    print("\nResult: Not Statistically Significant")
    print("We fail to reject the null hypothesis.")

# ---------------------------------------------
# ROI DISTRIBUTION VISUALIZATION
# ---------------------------------------------

plt.figure(figsize=(8, 5))

plt.boxplot(
    [group_a, group_b],
    tick_labels=["Social Media", "Paid Ads"]
)

plt.title("ROI Distribution: Social Media vs Paid Ads")
plt.ylabel("ROI")

plt.tight_layout()

# Save chart instead of opening an interactive window
plt.savefig(
    "reports/roi_ab_test_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nBox plot saved successfully:")
print("reports/roi_ab_test_boxplot.png")

# ---------------------------------------------
# EFFECT SIZE - COHEN'S D
# ---------------------------------------------

mean_a = group_a.mean()
mean_b = group_b.mean()

pooled_std = (
    ((len(group_a) - 1) * group_a.std() ** 2 +
     (len(group_b) - 1) * group_b.std() ** 2)
    /
    (len(group_a) + len(group_b) - 2)
) ** 0.5

cohens_d = (mean_a - mean_b) / pooled_std

print("\n" + "=" * 50)
print("EFFECT SIZE")
print("=" * 50)

print("Cohen's d:", round(cohens_d, 4))

if abs(cohens_d) < 0.2:
    print("Effect: Negligible")
elif abs(cohens_d) < 0.5:
    print("Effect: Small")
elif abs(cohens_d) < 0.8:
    print("Effect: Medium")
else:
    print("Effect: Large")

# ---------------------------------------------
# BUSINESS RECOMMENDATION
# ---------------------------------------------

print("\n" + "=" * 50)
print("BUSINESS RECOMMENDATION")
print("=" * 50)

print(
    "\nSocial Media has a slightly higher average ROI "
    f"({mean_a:.2f}) than Paid Ads ({mean_b:.2f})."
)

print(
    f"However, the difference is not statistically significant "
    f"(p = {p_value:.6f}) and the effect size is negligible "
    f"(Cohen's d = {cohens_d:.4f})."
)

print(
    "\nRecommendation: Do not shift marketing investment based "
    "on ROI alone. Evaluate additional metrics such as conversion "
    "rate, customer segment, engagement, and acquisition cost "
    "before reallocating budget."
)