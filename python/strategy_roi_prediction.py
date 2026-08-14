import pandas as pd
import numpy as np

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ============================================================
# STRATEGY-ONLY ROI PREDICTION
# ============================================================

print("=" * 65)
print("CAMPAIGN STRATEGY-ONLY ROI PREDICTION")
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

REPORTS_DIR = PROJECT_ROOT / "reports"

REPORTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 2. LOAD DATA
# ============================================================

print("\n" + "=" * 65)
print("LOADING DATA")
print("=" * 65)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Cleaned dataset not found:\n{INPUT_FILE}"
    )

df = pd.read_csv(INPUT_FILE)

print("\nDataset Shape:", df.shape)


# ============================================================
# 3. DEFINE STRATEGY FEATURES
# ============================================================

target = "ROI"

# IMPORTANT:
# Acquisition_Cost is intentionally excluded.
# Revenue, Clicks, Leads and Conversions are also excluded
# because they represent campaign performance/outcomes.

features = [
    "Campaign_Type",
    "Target_Audience",
    "Duration",
    "Channel_Used",
    "Language",
    "Customer_Segment"
]

X = df[features].copy()

y = df[target].copy()


print("\nTarget Variable:")
print(target)

print("\nStrategy Features:")

for feature in features:
    print("-", feature)


# ============================================================
# 4. FEATURE TYPES
# ============================================================

categorical_features = [
    "Campaign_Type",
    "Target_Audience",
    "Channel_Used",
    "Language",
    "Customer_Segment"
]

numeric_features = [
    "Duration"
]


# ============================================================
# 5. PREPROCESSING
# ============================================================

numeric_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median")
        )
    ]
)

categorical_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            )
        )
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            numeric_transformer,
            numeric_features
        ),
        (
            "categorical",
            categorical_transformer,
            categorical_features
        )
    ]
)


# ============================================================
# 6. TRAIN / TEST SPLIT
# ============================================================

print("\n" + "=" * 65)
print("TRAIN / TEST SPLIT")
print("=" * 65)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))


# ============================================================
# 7. LINEAR REGRESSION
# ============================================================

print("\n" + "=" * 65)
print("MODEL 1 — LINEAR REGRESSION")
print("=" * 65)

linear_model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            LinearRegression()
        )
    ]
)

linear_model.fit(
    X_train,
    y_train
)

linear_predictions = linear_model.predict(
    X_test
)

linear_mae = mean_absolute_error(
    y_test,
    linear_predictions
)

linear_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        linear_predictions
    )
)

linear_r2 = r2_score(
    y_test,
    linear_predictions
)

print(f"\nMAE: {linear_mae:.4f}")
print(f"RMSE: {linear_rmse:.4f}")
print(f"R²: {linear_r2:.4f}")


# ============================================================
# 8. RANDOM FOREST
# ============================================================

print("\n" + "=" * 65)
print("MODEL 2 — RANDOM FOREST REGRESSION")
print("=" * 65)

random_forest_model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            RandomForestRegressor(
                n_estimators=150,
                max_depth=15,
                min_samples_leaf=3,
                random_state=42,
                n_jobs=-1
            )
        )
    ]
)

print("\nTraining Random Forest...")

random_forest_model.fit(
    X_train,
    y_train
)

print("Random Forest trained successfully.")

rf_predictions = random_forest_model.predict(
    X_test
)

rf_mae = mean_absolute_error(
    y_test,
    rf_predictions
)

rf_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        rf_predictions
    )
)

rf_r2 = r2_score(
    y_test,
    rf_predictions
)

print(f"\nMAE: {rf_mae:.4f}")
print(f"RMSE: {rf_rmse:.4f}")
print(f"R²: {rf_r2:.4f}")


# ============================================================
# 9. MODEL COMPARISON
# ============================================================

print("\n" + "=" * 65)
print("STRATEGY-ONLY MODEL COMPARISON")
print("=" * 65)

comparison = pd.DataFrame(
    {
        "Model": [
            "Linear Regression",
            "Random Forest"
        ],
        "MAE": [
            linear_mae,
            rf_mae
        ],
        "RMSE": [
            linear_rmse,
            rf_rmse
        ],
        "R2": [
            linear_r2,
            rf_r2
        ]
    }
)

print(
    comparison.round(4).to_string(
        index=False
    )
)


# ============================================================
# 10. BEST MODEL
# ============================================================

best_model_row = comparison.loc[
    comparison["R2"].idxmax()
]

best_model = best_model_row["Model"]
best_r2 = best_model_row["R2"]
best_mae = best_model_row["MAE"]
best_rmse = best_model_row["RMSE"]

print("\n" + "=" * 65)
print("BEST STRATEGY-ONLY MODEL")
print("=" * 65)

print(f"\nBest Model: {best_model}")
print(f"R²: {best_r2:.4f}")
print(f"MAE: {best_mae:.4f}")
print(f"RMSE: {best_rmse:.4f}")


# ============================================================
# 11. SAVE COMPARISON
# ============================================================

comparison_file = (
    REPORTS_DIR
    / "strategy_roi_model_comparison.csv"
)

comparison.to_csv(
    comparison_file,
    index=False
)

print(
    "\nModel comparison saved:"
)

print(comparison_file)


# ============================================================
# 12. FEATURE IMPORTANCE
# ============================================================

print("\n" + "=" * 65)
print("STRATEGY FEATURE IMPORTANCE")
print("=" * 65)

rf_preprocessor = (
    random_forest_model
    .named_steps["preprocessor"]
)

rf_model = (
    random_forest_model
    .named_steps["model"]
)

feature_names = (
    rf_preprocessor
    .get_feature_names_out()
)

importances = rf_model.feature_importances_

feature_importance = pd.DataFrame(
    {
        "Feature": feature_names,
        "Importance": importances
    }
)

feature_importance = (
    feature_importance
    .sort_values(
        "Importance",
        ascending=False
    )
    .reset_index(drop=True)
)

print("\nTop 15 Strategy Features:")

print(
    feature_importance
    .head(15)
    .round(4)
    .to_string(index=False)
)


# ============================================================
# 13. SAVE FEATURE IMPORTANCE
# ============================================================

importance_file = (
    REPORTS_DIR
    / "strategy_roi_feature_importance.csv"
)

feature_importance.to_csv(
    importance_file,
    index=False
)

print(
    "\nFeature importance saved:"
)

print(importance_file)


# ============================================================
# 14. COMPARE AGAINST COST-ONLY MODEL
# ============================================================

cost_only_r2 = 0.7976
full_early_stage_r2 = 0.8098

print("\n" + "=" * 65)
print("OVERALL ROI MODEL COMPARISON")
print("=" * 65)

overall_comparison = pd.DataFrame(
    {
        "Model": [
            "Cost-Only Random Forest",
            "Early-Stage Random Forest",
            "Strategy-Only Random Forest"
        ],
        "R2": [
            cost_only_r2,
            full_early_stage_r2,
            rf_r2
        ]
    }
)

print(
    overall_comparison
    .round(4)
    .to_string(index=False)
)


# ============================================================
# 15. BUSINESS INTERPRETATION
# ============================================================

print("\n" + "=" * 65)
print("BUSINESS INTERPRETATION")
print("=" * 65)

print(
    f"""
The strategy-only model predicts ROI using campaign
characteristics without Acquisition Cost or campaign
performance outcomes.

Best Strategy Model: {best_model}

R²: {best_r2:.4f}
MAE: {best_mae:.4f}
RMSE: {best_rmse:.4f}

This provides a more conservative estimate of how much
ROI can be predicted from campaign strategy alone.

The comparison with the cost-only model helps identify
whether ROI predictability is primarily financial or
strategy-driven.
"""
)


# ============================================================
# 16. COMPLETION
# ============================================================

print("\n" + "=" * 65)
print("STRATEGY-ONLY ROI ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 65)