from pathlib import Path
import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
YIELD_MODEL_PATH = ROOT / "models" / "best_yield_model.pkl"
HEALTH_MODEL_PATH = ROOT / "models" / "best_crop_health_model.pkl"

def predict_agriculture(input_data: dict):
    if not YIELD_MODEL_PATH.exists() or not HEALTH_MODEL_PATH.exists():
        raise FileNotFoundError("Models not found. Run: py src/train_model.py")

    yield_model = joblib.load(YIELD_MODEL_PATH)
    health_model = joblib.load(HEALTH_MODEL_PATH)

    df = pd.DataFrame([input_data])

    predicted_yield = float(yield_model.predict(df)[0])
    health_status = str(health_model.predict(df)[0])

    result = {
        "predicted_yield": round(predicted_yield, 2),
        "crop_health_status": health_status,
    }

    if hasattr(health_model, "predict_proba"):
        proba = health_model.predict_proba(df)[0]
        result["health_confidence"] = round(float(proba.max()) * 100, 2)
    else:
        result["health_confidence"] = None

    return result
