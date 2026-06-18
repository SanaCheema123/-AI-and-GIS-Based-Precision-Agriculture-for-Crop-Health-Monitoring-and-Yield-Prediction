from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "crop_yield_soil_weather.csv"
PROCESSED_PATH = ROOT / "data" / "processed" / "processed_crop_data.csv"

def load_dataset(path=RAW_PATH):
    path = Path(path)
    if not path.exists():
        from generate_sample_data import main
        main()
    return pd.read_csv(path)

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df = df.drop_duplicates()

    for col in df.columns:
        converted = pd.to_numeric(df[col], errors="coerce")
        if converted.notna().sum() > len(df) * 0.70:
            df[col] = converted.fillna(converted.median())
        else:
            df[col] = df[col].astype(str)
            mode_value = df[col].mode()
            df[col] = df[col].replace("nan", mode_value.iloc[0] if not mode_value.empty else "Unknown")

    return df

def ensure_targets(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "yield_ton_per_hectare" not in df.columns:
        numeric = df.select_dtypes(include="number")
        if numeric.empty:
            raise ValueError("Dataset must contain numeric columns or yield_ton_per_hectare target.")
        score = numeric.apply(lambda s: (s - s.min()) / (s.max() - s.min() + 1e-9)).mean(axis=1)
        df["yield_ton_per_hectare"] = (score * 6 + 1).round(2)

    if "crop_health_status" not in df.columns:
        if "ndvi" in df.columns:
            df["crop_health_status"] = pd.cut(
                df["ndvi"],
                bins=[-1, 0.35, 0.60, 1],
                labels=["Poor", "Moderate", "Healthy"]
            ).astype(str)
        else:
            q1, q2 = df["yield_ton_per_hectare"].quantile([0.33, 0.66])
            df["crop_health_status"] = pd.cut(
                df["yield_ton_per_hectare"],
                bins=[-float("inf"), q1, q2, float("inf")],
                labels=["Poor", "Moderate", "Healthy"]
            ).astype(str)

    return df

def preprocess(path=RAW_PATH):
    df = load_dataset(path)
    df = clean_dataset(df)
    df = ensure_targets(df)

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    return df

if __name__ == "__main__":
    preprocess()
    print(f"Processed data saved: {PROCESSED_PATH}")
