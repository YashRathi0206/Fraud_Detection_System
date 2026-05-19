import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Load data
df = pd.read_csv("results.csv")

# Load model
model = joblib.load("model.pkl")

st.set_page_config(
    page_title="Fraud Detection Dashboard",
    layout="wide"
)

st.title("💳 Fraud Detection Dashboard")

# SIDEBAR
st.sidebar.header("Filters")

risk_filter = st.sidebar.multiselect(
    "Select Risk Tier",
    options=df['RiskTier'].unique(),
    default=df['RiskTier'].unique()
)

filtered_df = df[
    df['RiskTier'].isin(risk_filter)
]

# PAGE 1 — OVERVIEW


st.header("Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Transactions",
    len(filtered_df)
)

col2.metric(
    "Fraud Count",
    filtered_df['ActualFraud'].sum()
)

col3.metric(
    "Average Fraud Amount",
    round(
        filtered_df['TransactionAmt'].mean(),
        2
    )
)

# RISK TIER CHART

fig = px.pie(
    filtered_df,
    names='RiskTier',
    title='Risk Tier Distribution',
    hole=0.4
)

st.plotly_chart(fig)

# TRANSACTION EXPLORER

st.header("Transaction Explorer")

st.dataframe(filtered_df.head(100))

# SEARCH BY TRANSACTION ID

st.header("Search Transaction")

transaction_id = st.number_input(
    "Enter TransactionID",
    step=1
)

if transaction_id:

    row = filtered_df[
        filtered_df['TransactionID'] == transaction_id
    ]

    st.write(row)