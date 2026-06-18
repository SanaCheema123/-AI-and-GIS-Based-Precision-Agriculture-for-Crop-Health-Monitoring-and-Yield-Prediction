import streamlit as st
import subprocess
import sys


def sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div class="brand-box">
                <div class="brand-icon">🌱</div>
                <div>
                    <div class="brand-title">PrecisionAgri AI</div>
                    <div class="brand-sub">
                        AI + GIS Smart Agriculture
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="sidebar-section">
                <div class="sidebar-heading">
                    Navigation
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        page = st.radio(
            "",
            [
                "🏠 Dashboard",
                "📈 Yield Prediction",
                "🌾 Crop Health",
                "🗺️ GIS Visualization",
                "🤖 ML Analytics",
                "📊 Dataset Insights",
                "📑 Reports",
                "ℹ️ About Project",
            ],
            label_visibility="collapsed"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🚀 Train / Retrain Model", use_container_width=True):

            with st.spinner("Training Models..."):
                subprocess.run(
                    [sys.executable, "src/train_model.py"]
                )

            st.success("Model Training Completed")

        st.markdown("<hr>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="sidebar-tip">
                <b>Dataset Path</b><br><br>

                data/raw/<br>
                crop_yield_soil_weather.csv

                <br><br>

                Replace with your Kaggle dataset
                and click Retrain Model.
            </div>
            """,
            unsafe_allow_html=True
        )

        return page.replace("🏠 ", "") \
                   .replace("📈 ", "") \
                   .replace("🌾 ", "") \
                   .replace("🗺️ ", "") \
                   .replace("🤖 ", "") \
                   .replace("📊 ", "") \
                   .replace("📑 ", "") \
                   .replace("ℹ️ ", "")