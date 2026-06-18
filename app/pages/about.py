import streamlit as st

def show():
    st.markdown(
        '''
        <div class="hero-box">
            <span class="hero-badge">About Project</span>
            <h1>AI and GIS-Based Precision Agriculture</h1>
            <p>Crop health monitoring and yield prediction using satellite-inspired vegetation indices, weather, soil, and machine learning.</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown("### Project Title")
    st.write("AI and GIS-Based Precision Agriculture for Crop Health Monitoring and Yield Prediction")

    st.markdown("### Main Goal")
    st.write("Develop an intelligent decision support system to monitor crop health, predict yield, and optimize agricultural resource utilization.")

    st.markdown("### Dataset")
    st.write("Recommended Kaggle dataset: Crop Yield Data with Soil and Weather Dataset")

    st.markdown("### Main Technologies")
    st.write("Python, Streamlit, Scikit-learn, Pandas, Plotly, GIS concepts, Remote Sensing indicators.")
