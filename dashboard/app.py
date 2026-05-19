import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# LOAD DATA


df = pd.read_csv("results.csv")

# LOAD MODEL


model = joblib.load("model.pkl")

# PAGE CONFIG


st.set_page_config(
    page_title="Fraud Detection Dashboard",
    layout="wide"
)

st.title("💳 Fraud Detection Dashboard")

# SIDEBAR FILTER


st.sidebar.header("Filters")

risk_filter = st.sidebar.multiselect(
    "Select Risk Tier",
    options=df['RiskTier'].unique(),
    default=df['RiskTier'].unique()
)

filtered_df = df[
    df['RiskTier'].isin(risk_filter)
]

# OVERVIEW SECTION


st.header("Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Transactions",
    len(filtered_df)
)

col2.metric(
    "Fraud Count",
    int(filtered_df['ActualFraud'].sum())
)

col3.metric(
    "Average Transaction Amount",
    round(
        filtered_df['TransactionAmt'].mean(),
        2
    )
)

# RISK TIER PIE CHART


fig = px.pie(
    filtered_df,
    names='RiskTier',
    title='Risk Tier Distribution',
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)

# TRANSACTION EXPLORER


st.header("Transaction Explorer")

st.dataframe(filtered_df.head(100))

# SEARCH TRANSACTION


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