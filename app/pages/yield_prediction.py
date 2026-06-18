import streamlit as st
from src.predict import predict_agriculture

def show():
    st.markdown(
        '''
        <div class="hero-box">
            <span class="hero-badge">Yield Prediction Module</span>
            <h1>Crop Yield Prediction</h1>
            <p>Enter soil, weather, and vegetation parameters to predict crop yield and health status.</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        state = st.selectbox("State", ["Punjab", "Haryana", "Uttar Pradesh", "Maharashtra", "Karnataka", "Tamil Nadu", "Rajasthan", "Madhya Pradesh"])
        district = st.selectbox("District", ["D1", "D2", "D3", "D4", "D5"])
        crop = st.selectbox("Crop", ["Rice", "Wheat", "Maize", "Cotton", "Sugarcane", "Soybean"])
        season = st.selectbox("Season", ["Kharif", "Rabi", "Zaid"])

    with c2:
        rainfall_mm = st.number_input("Rainfall (mm)", value=850.0)
        temperature_c = st.number_input("Temperature (°C)", value=28.0)
        humidity_percent = st.number_input("Humidity (%)", value=65.0)
        soil_moisture_percent = st.number_input("Soil Moisture (%)", value=30.0)

    with c3:
        soil_type = st.selectbox("Soil Type", ["Clay", "Loam", "Sandy", "Silty", "Black Soil", "Alluvial"])
        nitrogen = st.number_input("Nitrogen", value=75.0)
        phosphorus = st.number_input("Phosphorus", value=45.0)
        potassium = st.number_input("Potassium", value=85.0)

    c4, c5, c6 = st.columns(3)
    with c4:
        ph = st.number_input("pH", value=6.8)
        ndvi = st.number_input("NDVI", value=0.62)
    with c5:
        evi = st.number_input("EVI", value=0.42)
        latitude = st.number_input("Latitude", value=30.50)
    with c6:
        longitude = st.number_input("Longitude", value=75.50)
        area_hectare = st.number_input("Area (hectare)", value=2.5)

    input_data = {
        "state": state,
        "district": district,
        "crop": crop,
        "season": season,
        "soil_type": soil_type,
        "rainfall_mm": rainfall_mm,
        "temperature_c": temperature_c,
        "humidity_percent": humidity_percent,
        "soil_moisture_percent": soil_moisture_percent,
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
        "ph": ph,
        "ndvi": ndvi,
        "evi": evi,
        "latitude": latitude,
        "longitude": longitude,
        "area_hectare": area_hectare,
    }

    if st.button("Predict Crop Yield"):
        try:
            result = predict_agriculture(input_data)
            st.success(f"Predicted Yield: {result['predicted_yield']} ton/hectare")
            st.info(f"Crop Health Status: {result['crop_health_status']} | Confidence: {result['health_confidence']}%")
        except Exception as e:
            st.error(str(e))
