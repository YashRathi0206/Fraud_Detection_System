# Real-Time Fraud Detection System

## Project Overview

This project presents an end-to-end Real-Time Fraud Detection System built using machine learning, explainable AI, and an interactive Streamlit dashboard. The system detects fraudulent financial transactions using advanced classification algorithms and provides risk-based transaction analysis.

The project uses the IEEE-CIS Fraud Detection dataset and applies preprocessing, feature engineering, imbalance handling, explainable AI, and dashboard deployment techniques.

---

# Features

- Fraud detection using LightGBM and XGBoost
- Data preprocessing and feature engineering
- Handling class imbalance using SMOTE
- Explainable AI using SHAP
- Risk segmentation system
- Interactive Streamlit dashboard
- Fraud analytics and visualization

---

# Dataset

Dataset Used:
- IEEE-CIS Fraud Detection Dataset

Files:
- train_transaction.csv
- train_identity.csv

The datasets were merged using:
- TransactionID

---

# Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python | Main programming language |
| Pandas / NumPy | Data manipulation |
| Scikit-learn | ML utilities |
| LightGBM | Primary classification model |
| XGBoost | Comparison model |
| imbalanced-learn | SMOTE imbalance handling |
| SHAP | Explainable AI |
| Plotly | Interactive charts |
| Streamlit | Dashboard deployment |
| Matplotlib / Seaborn | Data visualization |

---

# Machine Learning Workflow

1. Data Loading & Merging
2. Exploratory Data Analysis
3. Missing Value Handling
4. Feature Engineering
5. Label Encoding
6. SMOTE Oversampling
7. Model Training
8. SHAP Explainability
9. Risk Segmentation
10. Dashboard Deployment

---

# Models Used

- LightGBM
- XGBoost
- Isolation Forest

Among all models, LightGBM achieved the best performance due to strong recall and PR-AUC scores.

---

# Explainable AI

SHAP was used to explain model predictions and identify important fraud indicators such as:
- Transaction Amount
- HourOfDay
- AmtToMeanRatio

---

# Dashboard Features

The Streamlit dashboard provides:
- Fraud overview metrics
- Risk tier filtering
- Transaction explorer
- Interactive visualizations
- Fraud probability analysis

---

# Run the Dashboard
[streamlit run dashboard/app.py](https://frauddetectionsystem-j8xa3fo3pbr7bxgumrtge2.streamlit.app/)
```


# Results

- Successfully detected fraudulent transactions
- Built explainable fraud detection system
- Developed risk segmentation pipeline
- Created live dashboard for fraud analytics

---

# Future Improvements

- Real-time API integration
- Deep learning fraud detection
- Behavioral analytics
- Geolocation-based anomaly detection
- Live transaction monitoring
