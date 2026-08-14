import pandas as pd
import numpy as np

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ============================================================
# ACQUISITION COST DOMINANCE TEST
# ============================================================

print("=" * 65)
print("ACQUISITION COST DOMINANCE TEST")
print("=" * 65)


# ============================================================
# 1. PATHS
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

df = pd.read_csv(INPUT_FILE)

print("\nDataset Shape:", df.shape)


# ============================================================
# 3. COST-ONLY MODEL
# ============================================================

X = df[["Acquisition_Cost"]]

y = df["ROI"]


# ============================================================
# 4. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ============================================================
# 5. RANDOM FOREST
# ============================================================

print("\n" + "=" * 65)
print("TRAINING COST-ONLY RANDOM FOREST")
print("=" * 65)

model = RandomForestRegressor(
    n_estimators=150,
    max_depth=15,
    min_samples_leaf=3,
    random_state=42,
    n_jobs=-1
)

model.fit(
    X_train,
    y_train
)

print("\nModel trained successfully.")


# ============================================================
# 6. PREDICTIONS
# ============================================================

predictions = model.predict(
    X_test
)


# ============================================================
# 7. EVALUATION
# ============================================================

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        predictions
    )
)

r2 = r2_score(
    y_test,
    predictions
)


print("\n" + "=" * 65)
print("COST-ONLY MODEL RESULTS")
print("=" * 65)

print(f"\nMAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")


# ============================================================
# 8. COMPARE WITH FULL EARLY-STAGE MODEL
# ============================================================

early_stage_r2 = 0.8098

print("\n" + "=" * 65)
print("MODEL COMPARISON")
print("=" * 65)

print(
    f"\nCost-Only Model R²: "
    f"{r2:.4f}"
)

print(
    f"Full Early-Stage Model R²: "
    f"{early_stage_r2:.4f}"
)

improvement = (
    early_stage_r2 - r2
)

print(
    f"\nAdditional R² explained by other features: "
    f"{improvement:.4f}"
)


# ============================================================
# 9. INTERPRETATION
# ============================================================

print("\n" + "=" * 65)
print("INTERPRETATION")
print("=" * 65)

if r2 >= early_stage_r2 * 0.90:

    print(
        """
Acquisition Cost alone explains most of the predictive
performance of the early-stage model.

This indicates that ROI has a strong mathematical or
structural relationship with Acquisition Cost.

The full model should therefore NOT be interpreted as
proving that campaign characteristics independently
drive ROI.
"""
    )

else:

    print(
        """
Acquisition Cost alone does not explain most of the
performance of the full early-stage model.

Other campaign characteristics contribute meaningful
predictive information.
"""
    )


# ============================================================
# 10. COMPLETION
# ============================================================

print("\n" + "=" * 65)
print("COST DOMINANCE TEST COMPLETED")
print("=" * 65)