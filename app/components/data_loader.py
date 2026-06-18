from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PROCESSED_PATH = ROOT / "data" / "processed" / "processed_crop_data.csv"
RAW_PATH = ROOT / "data" / "raw" / "crop_yield_soil_weather.csv"
OUTPUTS = ROOT / "outputs"

def load_data():
    if PROCESSED_PATH.exists():
        return pd.read_csv(PROCESSED_PATH)
    if RAW_PATH.exists():
        return pd.read_csv(RAW_PATH)
    return pd.DataFrame()

def load_yield_comparison():
    path = OUTPUTS / "yield_model_comparison.csv"
    return pd.read_csv(path) if path.exists() else pd.DataFrame()

def load_health_comparison():
    path = OUTPUTS / "health_model_comparison.csv"
    return pd.read_csv(path) if path.exists() else pd.DataFrame()

def load_metadata():
    path = OUTPUTS / "training_metadata.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}
