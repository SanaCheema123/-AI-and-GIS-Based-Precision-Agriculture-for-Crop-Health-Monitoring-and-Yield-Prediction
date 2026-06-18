import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from components.data_loader import load_yield_comparison, load_health_comparison

ROOT = Path(__file__).resolve().parents[2]
OUTPUTS = ROOT / "outputs"

def show():
    st.markdown("## ML Model Analytics")

    yield_comp = load_yield_comparison()
    health_comp = load_health_comparison()

    st.markdown("### Yield Model Comparison")
    if not yield_comp.empty:
        st.dataframe(yield_comp, width="stretch", hide_index=True)
        st.plotly_chart(px.bar(yield_comp, x="Model", y=["MAE", "RMSE", "R2 Score"], barmode="group"), width="stretch")
    else:
        st.warning("Train the model to view yield analytics.")

    st.markdown("### Crop Health Model Comparison")
    if not health_comp.empty:
        st.dataframe(health_comp, width="stretch", hide_index=True)
        st.plotly_chart(px.bar(health_comp, x="Model", y=["Accuracy", "Precision", "Recall", "F1 Score"], barmode="group"), width="stretch")

    cm_path = OUTPUTS / "health_confusion_matrix.csv"
    if cm_path.exists():
        cm = pd.read_csv(cm_path, index_col=0)
        st.plotly_chart(px.imshow(cm, text_auto=True, aspect="auto", title="Crop Health Confusion Matrix"), width="stretch")
