import pandas as pd
import numpy as np

from pathlib import Path
from scipy.stats import pearsonr


# ============================================================
# ROI TARGET LEAKAGE CHECK
# ============================================================

print("=" * 65)
print("ROI TARGET LEAKAGE & FORMULA ANALYSIS")
print("=" * 65)


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


# ============================================================
# 2. LOAD DATA
# ============================================================

print("\n" + "=" * 65)
print("LOADING DATA")
print("=" * 65)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Dataset not found:\n{INPUT_FILE}"
    )

df = pd.read_csv(INPUT_FILE)

print("\nDataset Shape:", df.shape)


# ============================================================
# 3. CORRELATION WITH ROI
# ============================================================

print("\n" + "=" * 65)
print("CORRELATION WITH ROI")
print("=" * 65)

numeric_columns = [
    "Revenue",
    "Acquisition_Cost",
    "Conversions",
    "Leads",
    "Clicks",
    "Impressions",
    "Engagement_Score",
    "Duration"
]

for column in numeric_columns:

    if column in df.columns:

        correlation, p_value = pearsonr(
            df[column],
            df["ROI"]
        )

        print(
            f"\n{column}"
        )

        print(
            f"Correlation: {correlation:.4f}"
        )

        print(
            f"P-value: {p_value:.6f}"
        )


# ============================================================
# 4. TEST COMMON ROI FORMULAS
# ============================================================

print("\n" + "=" * 65)
print("ROI FORMULA INVESTIGATION")
print("=" * 65)


# Formula 1:
# ROI = (Revenue - Cost) / Cost

if (
    "Revenue" in df.columns
    and "Acquisition_Cost" in df.columns
):

    calculated_roi_1 = (
        df["Revenue"] - df["Acquisition_Cost"]
    ) / df["Acquisition_Cost"]

    correlation_1 = (
        calculated_roi_1
        .corr(df["ROI"])
    )

    mae_1 = np.mean(
        np.abs(
            calculated_roi_1 - df["ROI"]
        )
    )

    print(
        "\nFormula 1:"
    )

    print(
        "ROI = (Revenue - Acquisition_Cost) / Acquisition_Cost"
    )

    print(
        f"Correlation with actual ROI: {correlation_1:.6f}"
    )

    print(
        f"Mean Absolute Difference: {mae_1:.6f}"
    )


# Formula 2:
# ROI = Revenue / Cost

calculated_roi_2 = (
    df["Revenue"]
    / df["Acquisition_Cost"]
)

correlation_2 = (
    calculated_roi_2
    .corr(df["ROI"])
)

mae_2 = np.mean(
    np.abs(
        calculated_roi_2 - df["ROI"]
    )
)

print(
    "\nFormula 2:"
)

print(
    "ROI = Revenue / Acquisition_Cost"
)

print(
    f"Correlation with actual ROI: {correlation_2:.6f}"
)

print(
    f"Mean Absolute Difference: {mae_2:.6f}"
)


# ============================================================
# 5. IDENTIFY POSSIBLE LEAKAGE
# ============================================================

print("\n" + "=" * 65)
print("LEAKAGE ASSESSMENT")
print("=" * 65)


if correlation_1 > 0.95 or correlation_2 > 0.95:

    print(
        "\nWARNING: ROI appears to be directly derived "
        "from Revenue and/or Acquisition_Cost."
    )

    print(
        "\nAcquisition_Cost and Revenue should be treated "
        "carefully when building a predictive ROI model."
    )

    print(
        "\nThe current Random Forest model may be benefiting "
        "from target leakage."
    )

else:

    print(
        "\nNo strong direct formula relationship was detected."
    )


# ============================================================
# 6. BUSINESS INTERPRETATION
# ============================================================

print("\n" + "=" * 65)
print("BUSINESS INTERPRETATION")
print("=" * 65)

print(
    """
Target leakage occurs when a predictive model receives
information that would not realistically be available
at the time a prediction is made.

For ROI prediction, Revenue and Acquisition_Cost may be
especially important to investigate because ROI is often
calculated using financial outcomes.

If ROI is directly calculated from these variables, using
them as predictive features would make the model appear
stronger than it actually is.
"""
)


# ============================================================
# 7. COMPLETION
# ============================================================

print("\n" + "=" * 65)
print("LEAKAGE CHECK COMPLETED")
print("=" * 65)