from pathlib import Path
import json
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier

from data_preprocessing import preprocess

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
OUTPUTS = ROOT / "outputs"

YIELD_TARGET = "yield_ton_per_hectare"
HEALTH_TARGET = "crop_health_status"

DROP_COLS = ["sample_id", YIELD_TARGET, HEALTH_TARGET]

def build_preprocessor(X):
    num_cols = X.select_dtypes(include="number").columns.tolist()
    cat_cols = X.select_dtypes(exclude="number").columns.tolist()

    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
        ]
    )

def train():
    df = preprocess()

    X = df.drop(columns=[c for c in DROP_COLS if c in df.columns])
    y_yield = df[YIELD_TARGET]
    y_health = df[HEALTH_TARGET]

    X_train, X_test, yy_train, yy_test, yh_train, yh_test = train_test_split(
        X, y_yield, y_health, test_size=0.2, random_state=42, stratify=y_health
    )

    preprocessor = build_preprocessor(X)

    yield_models = {
        "Random Forest Regressor": RandomForestRegressor(n_estimators=180, random_state=42),
        "Decision Tree Regressor": DecisionTreeRegressor(random_state=42),
    }

    yield_results = []
    best_yield_name = None
    best_yield_score = -999
    best_yield_pipeline = None

    for name, model in yield_models.items():
        pipe = Pipeline([("preprocessor", preprocessor), ("model", model)])
        pipe.fit(X_train, yy_train)
        preds = pipe.predict(X_test)

        mae = mean_absolute_error(yy_test, preds)
        rmse = mean_squared_error(yy_test, preds) ** 0.5
        r2 = r2_score(yy_test, preds)

        yield_results.append({"Model": name, "MAE": mae, "RMSE": rmse, "R2 Score": r2})

        if r2 > best_yield_score:
            best_yield_score = r2
            best_yield_name = name
            best_yield_pipeline = pipe

    health_models = {
        "Random Forest Classifier": RandomForestClassifier(n_estimators=180, random_state=42),
        "Decision Tree Classifier": DecisionTreeClassifier(random_state=42),
    }

    health_results = []
    best_health_name = None
    best_health_score = -999
    best_health_pipeline = None
    best_health_cm = None

    for name, model in health_models.items():
        pipe = Pipeline([("preprocessor", preprocessor), ("model", model)])
        pipe.fit(X_train, yh_train)
        preds = pipe.predict(X_test)

        acc = accuracy_score(yh_test, preds)
        precision = precision_score(yh_test, preds, average="weighted", zero_division=0)
        recall = recall_score(yh_test, preds, average="weighted", zero_division=0)
        f1 = f1_score(yh_test, preds, average="weighted", zero_division=0)

        health_results.append({"Model": name, "Accuracy": acc, "Precision": precision, "Recall": recall, "F1 Score": f1})

        if acc > best_health_score:
            best_health_score = acc
            best_health_name = name
            best_health_pipeline = pipe
            best_health_cm = confusion_matrix(yh_test, preds, labels=sorted(y_health.unique()))

    MODELS.mkdir(exist_ok=True)
    OUTPUTS.mkdir(exist_ok=True)

    joblib.dump(best_yield_pipeline, MODELS / "best_yield_model.pkl")
    joblib.dump(best_health_pipeline, MODELS / "best_crop_health_model.pkl")

    pd.DataFrame(yield_results).to_csv(OUTPUTS / "yield_model_comparison.csv", index=False)
    pd.DataFrame(health_results).to_csv(OUTPUTS / "health_model_comparison.csv", index=False)

    labels = sorted(y_health.unique())
    pd.DataFrame(best_health_cm, index=labels, columns=labels).to_csv(OUTPUTS / "health_confusion_matrix.csv")

    metadata = {
        "best_yield_model": best_yield_name,
        "yield_r2": round(float(best_yield_score), 4),
        "best_health_model": best_health_name,
        "health_accuracy": round(float(best_health_score), 4),
        "feature_columns": X.columns.tolist()
    }
    (OUTPUTS / "training_metadata.json").write_text(json.dumps(metadata, indent=4), encoding="utf-8")

    print(f"Best yield model: {best_yield_name} | R2: {best_yield_score:.4f}")
    print(f"Best health model: {best_health_name} | Accuracy: {best_health_score:.4f}")
    print(f"Models saved in: {MODELS}")

if __name__ == "__main__":
    train()
