from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "crop_yield_soil_weather.csv"

def main(n=1500, seed=42):
    np.random.seed(seed)

    states = ["Punjab", "Haryana", "Uttar Pradesh", "Maharashtra", "Karnataka", "Tamil Nadu", "Rajasthan", "Madhya Pradesh"]
    crops = ["Rice", "Wheat", "Maize", "Cotton", "Sugarcane", "Soybean"]
    seasons = ["Kharif", "Rabi", "Zaid"]
    soil_types = ["Clay", "Loam", "Sandy", "Silty", "Black Soil", "Alluvial"]

    df = pd.DataFrame({
        "sample_id": [f"AGRI-{i:04d}" for i in range(1, n + 1)],
        "state": np.random.choice(states, n),
        "district": np.random.choice(["D1", "D2", "D3", "D4", "D5"], n),
        "crop": np.random.choice(crops, n),
        "season": np.random.choice(seasons, n),
        "soil_type": np.random.choice(soil_types, n),
        "rainfall_mm": np.round(np.random.uniform(350, 1450, n), 2),
        "temperature_c": np.round(np.random.uniform(18, 38, n), 2),
        "humidity_percent": np.round(np.random.uniform(35, 90, n), 2),
        "soil_moisture_percent": np.round(np.random.uniform(12, 48, n), 2),
        "nitrogen": np.round(np.random.uniform(20, 130, n), 2),
        "phosphorus": np.round(np.random.uniform(10, 90, n), 2),
        "potassium": np.round(np.random.uniform(20, 160, n), 2),
        "ph": np.round(np.random.uniform(5.0, 8.5, n), 2),
        "ndvi": np.round(np.random.uniform(0.18, 0.88, n), 3),
        "evi": np.round(np.random.uniform(0.10, 0.70, n), 3),
        "latitude": np.round(np.random.uniform(8.0, 32.0, n), 5),
        "longitude": np.round(np.random.uniform(68.0, 88.0, n), 5),
        "area_hectare": np.round(np.random.uniform(0.5, 8.0, n), 2),
    })

    base = (
        1.8
        + df["ndvi"] * 4.5
        + df["soil_moisture_percent"] * 0.035
        + df["rainfall_mm"] * 0.0012
        + df["nitrogen"] * 0.01
        + df["phosphorus"] * 0.006
        + df["potassium"] * 0.004
        - abs(df["temperature_c"] - 27) * 0.08
        - abs(df["ph"] - 6.8) * 0.25
    )

    crop_factor = df["crop"].map({
        "Rice": 1.15,
        "Wheat": 1.00,
        "Maize": 0.95,
        "Cotton": 0.75,
        "Sugarcane": 1.35,
        "Soybean": 0.85
    })

    noise = np.random.normal(0, 0.45, n)
    df["yield_ton_per_hectare"] = np.round(np.maximum(base * crop_factor + noise, 0.5), 2)

    health_score = (
        df["ndvi"] * 45
        + df["soil_moisture_percent"] * 0.45
        + df["humidity_percent"] * 0.12
        + df["nitrogen"] * 0.08
        - abs(df["temperature_c"] - 27) * 1.2
        - abs(df["ph"] - 6.8) * 5
    )

    df["crop_health_status"] = pd.cut(
        health_score,
        bins=[-999, 34, 52, 999],
        labels=["Poor", "Moderate", "Healthy"]
    ).astype(str)

    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(RAW_PATH, index=False)
    print(f"Sample dataset saved: {RAW_PATH}")

if __name__ == "__main__":
    main()
