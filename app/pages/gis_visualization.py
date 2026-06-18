import streamlit as st
import plotly.express as px
from components.data_loader import load_data

def show():
    st.markdown("## GIS Visualization")

    df = load_data()
    if df.empty:
        st.warning("Dataset not available.")
        return

    if {"latitude", "longitude", "crop_health_status"}.issubset(df.columns):
        fig = px.scatter_map(
            df,
            lat="latitude",
            lon="longitude",
            color="crop_health_status",
            size="yield_ton_per_hectare" if "yield_ton_per_hectare" in df.columns else None,
            zoom=4,
            height=520,
            title="Crop Health and Yield Geospatial Map"
        )
        st.plotly_chart(fig, width="stretch")

    if {"rainfall_mm", "ndvi", "yield_ton_per_hectare"}.issubset(df.columns):
        fig = px.scatter(
            df,
            x="rainfall_mm",
            y="ndvi",
            color="crop_health_status",
            size="yield_ton_per_hectare",
            title="Rainfall vs NDVI with Yield"
        )
        st.plotly_chart(fig, width="stretch")
