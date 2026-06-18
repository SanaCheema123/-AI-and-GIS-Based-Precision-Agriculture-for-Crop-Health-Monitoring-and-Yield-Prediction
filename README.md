# 🌱 PrecisionAgri AI

## AI and GIS-Based Precision Agriculture for Crop Health Monitoring and Yield Prediction

### Overview

PrecisionAgri AI is an intelligent agriculture decision-support system that combines Artificial Intelligence (AI), Geographic Information Systems (GIS), Machine Learning, and Precision Agriculture techniques to monitor crop health, predict agricultural yield, and support data-driven farming decisions.

The system analyzes environmental, soil, weather, and crop-related parameters to provide valuable insights for farmers, researchers, and agricultural planners.

---

# Project Objectives

* Predict crop yield using machine learning models.
* Monitor crop health status using environmental indicators.
* Analyze agricultural datasets using GIS concepts.
* Support precision agriculture and resource optimization.
* Provide an interactive dashboard for agricultural decision-making.

---

# Dataset

### Dataset Name

Crop Yield Data with Soil and Weather Dataset

### Source

Kaggle Dataset

### Dataset Features

| Feature            | Description                  |
| ------------------ | ---------------------------- |
| State              | Agricultural region          |
| District           | District information         |
| Crop               | Crop type                    |
| Season             | Crop growing season          |
| Soil Type          | Soil classification          |
| Rainfall (mm)      | Annual rainfall              |
| Temperature (°C)   | Average temperature          |
| Humidity (%)       | Atmospheric humidity         |
| NDVI               | Vegetation index             |
| Yield Ton/Ha       | Crop yield output            |
| Crop Health Status | Healthy, Moderate, Unhealthy |

---

# Machine Learning Pipeline

## Step 1: Data Collection

Dataset collected from Kaggle containing:

* Crop Information
* Weather Data
* Soil Data
* Yield Information

---

## Step 2: Data Preprocessing

Performed:

* Missing value handling
* Duplicate removal
* Feature encoding
* Data normalization
* Data validation

---

## Step 3: Feature Engineering

Generated:

* Crop Health Index
* Environmental Score
* Soil Fertility Indicators
* Yield-related features

---

## Step 4: Yield Prediction Model

Models Tested:

* Random Forest Regressor
* Decision Tree Regressor
* Gradient Boosting Regressor
* XGBoost Regressor

Evaluation Metrics:

* R² Score
* MAE
* RMSE

---

## Step 5: Crop Health Classification

Models Tested:

* Random Forest Classifier
* Decision Tree Classifier
* XGBoost Classifier

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score

---

## Step 6: Dashboard Analytics

Interactive dashboard provides:

* Dataset Overview
* Crop Health Distribution
* Yield Prediction Trends
* GIS Visualizations
* Machine Learning Performance
* Agricultural Reports

---

# Dashboard Modules

## Dashboard

Displays:

* Total Samples
* Crop Types
* Average Yield
* Yield Prediction Score
* Health Classification Accuracy

---

## Yield Prediction

User Inputs:

* Rainfall
* Temperature
* Soil Type
* Crop Type
* NDVI

Output:

* Predicted Yield (Ton/Ha)

---

## Crop Health Monitoring

Predicts:

* Healthy
* Moderate
* Unhealthy

based on environmental indicators.

---

## GIS Visualization

Displays:

* NDVI Maps
* Agricultural Spatial Analysis
* Environmental Insights

---

## Dataset Insights

Provides:

* Statistical Summary
* Correlation Analysis
* Distribution Analysis

---

## ML Analytics

Displays:

* Model Comparison
* Accuracy Metrics
* Feature Importance
* Performance Visualization

---

## Reports

Generates:

* Crop Health Reports
* Yield Reports
* Agricultural Analytics Reports

---

# Project Structure

```text
precision_agriculture_ai_gis_project/

├── app/
│   ├── app.py
│   ├── assets/
│   │   └── style.css
│   ├── components/
│   └── pages/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── outputs/
│
├── notebooks/
│
├── src/
│   ├── generate_sample_data.py
│   ├── data_preprocessing.py
│   ├── train_model.py
│   └── evaluation.py
│
├── requirements.txt
├── README.md
└── run_app.bat
```

# Technologies Used

### Programming

* Python 3.11

### Machine Learning

* Scikit-Learn
* XGBoost

### Dashboard

* Streamlit

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib

### GIS & Geospatial

* GeoPandas
* Folium

---

# Installation

## Clone Project

```bash
git clone <repository-url>
cd precision_agriculture_ai_gis_project
```

## Install Dependencies

```bash
py -m pip install -r requirements.txt
```

## Train Models

```bash
py src/train_model.py
```

## Launch Dashboard

```bash
py -m streamlit run app/app.py
```

---

# Expected Results

* Crop Yield Prediction
* Crop Health Classification
* Agricultural Insights
* GIS-Based Visualization
* Precision Farming Decision Support

---

# Future Improvements

* Real-Time Satellite Data Integration
* Drone-Based Crop Monitoring
* Deep Learning Models
* IoT Sensor Integration
* Advanced GIS Mapping
* Multi-Crop Recommendation System

---

# Author

PrecisionAgri AI Development Project

AI + GIS + Precision Agriculture Analytics Platform
