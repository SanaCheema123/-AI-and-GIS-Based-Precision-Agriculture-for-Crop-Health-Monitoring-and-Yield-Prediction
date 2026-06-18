import streamlit as st
from components.data_loader import load_data, load_yield_comparison, load_health_comparison

def show():
    st.markdown("## Reports")

    df = load_data()
    yield_comp = load_yield_comparison()
    health_comp = load_health_comparison()

    if not df.empty:
        st.download_button(
            "Download Processed Dataset",
            data=df.to_csv(index=False),
            file_name="processed_crop_data.csv",
            mime="text/csv"
        )

    if not yield_comp.empty:
        st.download_button(
            "Download Yield Model Report",
            data=yield_comp.to_csv(index=False),
            file_name="yield_model_report.csv",
            mime="text/csv"
        )

    if not health_comp.empty:
        st.download_button(
            "Download Health Model Report",
            data=health_comp.to_csv(index=False),
            file_name="health_model_report.csv",
            mime="text/csv"
        )
