import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from components.data_loader import load_data, load_metadata


def metric_card(icon, title, value, sub, color):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon" style="background:{color};">{icon}</div>
            <div>
                <p>{title}</p>
                <h2>{value}</h2>
                <span>{sub}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show():
    df = load_data()
    meta = load_metadata()

    if df.empty:
        st.warning(
            "Dataset not found. Run: py src/generate_sample_data.py and py src/train_model.py"
        )
        return

    avg_yield = (
        f"{df['yield_ton_per_hectare'].mean():.2f}"
        if "yield_ton_per_hectare" in df.columns
        else "-"
    )

    best_r2 = f"{meta.get('yield_r2', 0) * 100:.2f}%"
    health_acc = f"{meta.get('health_accuracy', 0) * 100:.2f}%"

    st.markdown(
        """
        <div class="hero-new">
            <div>
                <h4>Welcome back, Admin! 👋</h4>
                <h1>PrecisionAgri Intelligence Dashboard</h1>
                <p>
                    Crop health monitoring, yield prediction, and geospatial
                    agriculture decision support powered by AI + GIS.
                </p>
            </div>
            <div class="hero-art">🚜 🌱 🌄</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        metric_card("🧪", "Total Samples", f"{len(df):,}", "↑ 120 this month", "#ede9fe")

    with c2:
        crop_count = df["crop"].nunique() if "crop" in df.columns else "-"
        metric_card("🌱", "Crop Types", crop_count, "All monitored", "#dcfce7")

    with c3:
        metric_card("🌾", "Avg Yield (Ton/Ha)", avg_yield, "↑ 0.35 from last month", "#fef3c7")

    with c4:
        metric_card("📈", "Yield R² Score", best_r2, "High accuracy", "#e0f2fe")

    with c5:
        metric_card("🎯", "Health Accuracy", health_acc, "Good performance", "#ffe4e6")

    st.markdown("<br>", unsafe_allow_html=True)

    left, middle, right = st.columns([1.1, 1.1, 1.1])

    with left:
        st.markdown(
            '<div class="chart-card"><h3>🌿 Crop Health Distribution</h3>',
            unsafe_allow_html=True
        )

        if "crop_health_status" in df.columns:
            counts = df["crop_health_status"].value_counts().reset_index()
            counts.columns = ["Health Status", "Samples"]

            fig = px.bar(
                counts,
                x="Health Status",
                y="Samples",
                color="Health Status",
                text="Samples",
                color_discrete_map={
                    "Healthy": "#16a34a",
                    "Moderate": "#facc15",
                    "Poor": "#ef4444",
                    "Unhealthy": "#ef4444",
                }
            )

            fig.update_layout(
                height=300,
                showlegend=False,
                plot_bgcolor="white",
                paper_bgcolor="white",
                margin=dict(l=10, r=10, t=20, b=10),
                font=dict(color="#0f172a")
            )

            st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)

    with middle:
        st.markdown(
            '<div class="chart-card"><h3>📈 Yield Prediction Trend</h3>',
            unsafe_allow_html=True
        )

        fig2 = go.Figure()
        fig2.add_trace(
            go.Scatter(
                x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                y=[5.6, 6.2, 7.1, 6.6, 7.1, 7.7],
                mode="lines+markers",
                fill="tozeroy",
                line=dict(color="#16a34a", width=3)
            )
        )

        fig2.update_layout(
            height=300,
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(l=10, r=10, t=20, b=10),
            font=dict(color="#0f172a")
        )

        st.plotly_chart(fig2, width="stretch")
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown(
            """
            <div class="chart-card map-card">
                <h3>🗺 Field Health Map (NDVI)</h3>
                <div class="fake-map">
                    <div class="farm-grid"></div>
                    <div class="legend">
                        <b>NDVI</b><br>
                        <span class="green"></span> 0.9<br>
                        <span class="yellow"></span> 0.6<br>
                        <span class="red"></span> 0.3
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.markdown("### Dataset Preview")

    show_cols = [
        c for c in [
            "sample_id",
            "state",
            "district",
            "crop",
            "season",
            "soil_type",
            "rainfall_mm",
            "temperature_c",
            "ndvi",
            "yield_ton_per_hectare",
            "crop_health_status"
        ]
        if c in df.columns
    ]

    st.dataframe(
        df[show_cols].head(8),
        width="stretch",
        hide_index=True
    )

    st.markdown("</div>", unsafe_allow_html=True)