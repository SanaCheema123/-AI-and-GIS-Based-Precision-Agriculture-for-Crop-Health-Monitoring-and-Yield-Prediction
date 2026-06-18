import streamlit as st
import plotly.express as px
from components.data_loader import load_data

def show():
    st.markdown("## Crop Health Monitoring")

    df = load_data()
    if df.empty:
        st.warning("Dataset not available.")
        return

    c1, c2 = st.columns(2)

    with c1:
        if "ndvi" in df.columns and "crop_health_status" in df.columns:
            fig = px.box(df, x="crop_health_status", y="ndvi", color="crop_health_status", title="NDVI by Crop Health Status")
            st.plotly_chart(fig, width="stretch")

    with c2:
        if "soil_moisture_percent" in df.columns and "crop_health_status" in df.columns:
            fig = px.box(df, x="crop_health_status", y="soil_moisture_percent", color="crop_health_status", title="Soil Moisture by Crop Health")
            st.plotly_chart(fig, width="stretch")

    st.markdown("### Health Rule Interpretation")
    st.write("Higher NDVI, balanced soil moisture, suitable temperature, and balanced soil pH generally indicate healthier crop conditions.")
