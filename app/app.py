import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))
sys.path.append(str(Path(__file__).resolve().parent))

from pages import (
    dashboard,
    yield_prediction,
    crop_health,
    gis_visualization,
    ml_analytics,
    reports,
    dataset_insights,
    about,
)

st.set_page_config(
    page_title="PrecisionAgri AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css_path = Path(__file__).resolve().parent / "assets" / "style.css"
with open(css_path, "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

st.markdown(
    """
    <div class="topbar">
        <div class="logo-area">
            <div class="logo">🌿</div>
            <div>
                <h3>PrecisionAgri AI</h3>
                <p>AI + GIS • Smart Agriculture</p>
            </div>
        </div>
        <div class="profile">
            <input placeholder="Search anything..." />
            <span>🔔</span>
            <span>👩‍💼</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

nav_items = [
    "Dashboard",
    "Yield Prediction",
    "Crop Health",
    "GIS Visualization",
    "ML Analytics",
    "Reports",
    "Dataset Insights",
    "About Project",
]

cols = st.columns(len(nav_items))

for col, item in zip(cols, nav_items):
    with col:
        button_type = "primary" if st.session_state.page == item else "secondary"
        if st.button(item, key=item, type=button_type, use_container_width=True):
            st.session_state.page = item
            st.rerun()

page = st.session_state.page

if page == "Dashboard":
    dashboard.show()
elif page == "Yield Prediction":
    yield_prediction.show()
elif page == "Crop Health":
    crop_health.show()
elif page == "GIS Visualization":
    gis_visualization.show()
elif page == "ML Analytics":
    ml_analytics.show()
elif page == "Reports":
    reports.show()
elif page == "Dataset Insights":
    dataset_insights.show()
else:
    about.show()