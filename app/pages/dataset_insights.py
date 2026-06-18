import streamlit as st
import plotly.express as px
from components.data_loader import load_data

def show():
    st.markdown("## Dataset Insights")

    df = load_data()
    if df.empty:
        st.warning("Dataset not available.")
        return

    num_cols = df.select_dtypes(include="number").columns.tolist()

    if num_cols:
        col = st.selectbox("Select Numeric Feature", num_cols)
        st.plotly_chart(px.histogram(df, x=col, color="crop_health_status", nbins=35), width="stretch")

    if "crop" in df.columns:
        st.plotly_chart(px.bar(df.groupby("crop")["yield_ton_per_hectare"].mean().reset_index(), x="crop", y="yield_ton_per_hectare", title="Average Yield by Crop"), width="stretch")

    if len(num_cols) > 1:
        st.plotly_chart(px.imshow(df[num_cols].corr(), text_auto=".2f", aspect="auto", title="Correlation Heatmap"), width="stretch")

    st.dataframe(df, width="stretch", hide_index=True)
