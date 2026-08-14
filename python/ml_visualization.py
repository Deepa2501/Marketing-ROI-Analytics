import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ============================================================
# MARKETING ROI — ML VISUALIZATION PIPELINE
# ============================================================

print("=" * 65)
print("MARKETING ROI ML VISUALIZATION")
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
        f"Dataset not found:\n{INPUT_FILE}"
    )

df = pd.read_csv(INPUT_FILE)

print("\nDataset Shape:", df.shape)


# ============================================================
# 3. FEATURES FOR EARLY-STAGE MODEL
# ============================================================

target = "ROI"

features = [
    "Campaign_Type",
    "Target_Audience",
    "Duration",
    "Channel_Used",
    "Language",
    "Customer_Segment",
    "Acquisition_Cost"
]

X = df[features].copy()

y = df[target].copy()


categorical_features = [
    "Campaign_Type",
    "Target_Audience",
    "Channel_Used",
    "Language",
    "Customer_Segment"
]

numeric_features = [
    "Duration",
    "Acquisition_Cost"
]


# ============================================================
# 4. PREPROCESSING
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
# 5. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ============================================================
# 6. TRAIN RANDOM FOREST
# ============================================================

print("\n" + "=" * 65)
print("TRAINING RANDOM FOREST")
print("=" * 65)

model = Pipeline(
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

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

print("\nModel trained successfully.")


# ============================================================
# 7. MODEL METRICS
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
print("MODEL PERFORMANCE")
print("=" * 65)

print(f"\nMAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")


# ============================================================
# 8. ACTUAL VS PREDICTED ROI
# ============================================================

print("\nGenerating Actual vs Predicted ROI plot...")

plt.figure(figsize=(9, 6))

plt.scatter(
    y_test,
    predictions,
    alpha=0.35
)

min_value = min(
    y_test.min(),
    predictions.min()
)

max_value = max(
    y_test.max(),
    predictions.max()
)

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--"
)

plt.xlabel("Actual ROI")
plt.ylabel("Predicted ROI")

plt.title(
    "Actual vs Predicted ROI — Random Forest"
)

plt.tight_layout()

actual_predicted_file = (
    REPORTS_DIR
    / "actual_vs_predicted_roi.png"
)

plt.savefig(
    actual_predicted_file,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Saved:",
    actual_predicted_file
)


# ============================================================
# 9. RESIDUAL ANALYSIS
# ============================================================

print("\nGenerating residual plot...")

residuals = (
    y_test.values
    - predictions
)

plt.figure(figsize=(9, 6))

plt.scatter(
    predictions,
    residuals,
    alpha=0.35
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.xlabel("Predicted ROI")
plt.ylabel("Residual")

plt.title(
    "Residual Analysis — Random Forest"
)

plt.tight_layout()

residual_file = (
    REPORTS_DIR
    / "roi_residual_analysis.png"
)

plt.savefig(
    residual_file,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Saved:",
    residual_file
)


# ============================================================
# 10. FEATURE IMPORTANCE
# ============================================================

print("\nGenerating feature importance plot...")

rf_preprocessor = (
    model
    .named_steps["preprocessor"]
)

rf_model = (
    model
    .named_steps["model"]
)

feature_names = (
    rf_preprocessor
    .get_feature_names_out()
)

importances = (
    rf_model
    .feature_importances_
)

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
)

top_features = (
    feature_importance
    .head(15)
    .sort_values(
        "Importance"
    )
)

plt.figure(figsize=(10, 7))

plt.barh(
    top_features["Feature"],
    top_features["Importance"]
)

plt.xlabel("Importance")

plt.ylabel("Feature")

plt.title(
    "Top 15 Features for ROI Prediction"
)

plt.tight_layout()

feature_plot_file = (
    REPORTS_DIR
    / "roi_feature_importance.png"
)

plt.savefig(
    feature_plot_file,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Saved:",
    feature_plot_file
)


# ============================================================
# 11. MODEL COMPARISON
# ============================================================

print("\nGenerating model comparison plot...")

model_names = [
    "Cost-Only RF",
    "Early-Stage RF",
    "Strategy-Only"
]

r2_values = [
    0.7976,
    0.8098,
    -0.0025
]

plt.figure(figsize=(9, 6))

bars = plt.bar(
    model_names,
    r2_values
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.ylabel("R² Score")

plt.title(
    "ROI Prediction Model Comparison"
)

for bar, value in zip(
    bars,
    r2_values
):

    plt.text(
        bar.get_x()
        + bar.get_width() / 2,
        value,
        f"{value:.4f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

comparison_plot_file = (
    REPORTS_DIR
    / "roi_model_comparison.png"
)

plt.savefig(
    comparison_plot_file,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Saved:",
    comparison_plot_file
)


# ============================================================
# 12. PREDICTION ERROR DISTRIBUTION
# ============================================================

print("\nGenerating prediction error distribution...")

plt.figure(figsize=(9, 6))

plt.hist(
    residuals,
    bins=40
)

plt.axvline(
    x=0,
    linestyle="--"
)

plt.xlabel("Prediction Error")

plt.ylabel("Frequency")

plt.title(
    "Distribution of ROI Prediction Errors"
)

plt.tight_layout()

error_distribution_file = (
    REPORTS_DIR
    / "roi_prediction_error_distribution.png"
)

plt.savefig(
    error_distribution_file,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Saved:",
    error_distribution_file
)


# ============================================================
# 13. SAVE PREDICTIONS
# ============================================================

prediction_results = pd.DataFrame(
    {
        "Actual_ROI": y_test.values,
        "Predicted_ROI": predictions,
        "Residual": residuals
    }
)

prediction_file = (
    REPORTS_DIR
    / "roi_predictions.csv"
)

prediction_results.to_csv(
    prediction_file,
    index=False
)

print(
    "\nPrediction results saved:"
)

print(prediction_file)


# ============================================================
# 14. BUSINESS INTERPRETATION
# ============================================================

print("\n" + "=" * 65)
print("BUSINESS INTERPRETATION")
print("=" * 65)

print(
    f"""
Random Forest achieved:

R²   : {r2:.4f}
MAE  : {mae:.4f}
RMSE : {rmse:.4f}

The Actual vs Predicted plot shows how closely model
predictions follow observed ROI.

Residual analysis helps identify systematic prediction
errors and potential model limitations.

Feature importance highlights which variables contribute
most to the model's predictions.
"""
)


# ============================================================
# 15. COMPLETION
# ============================================================

print("\n" + "=" * 65)
print("ML VISUALIZATION PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 65)

print("\nGenerated Reports:")

print(
    "1.",
    actual_predicted_file
)

print(
    "2.",
    residual_file
)

print(
    "3.",
    feature_plot_file
)

print(
    "4.",
    comparison_plot_file
)

print(
    "5.",
    error_distribution_file
)

print(
    "6.",
    prediction_file
)