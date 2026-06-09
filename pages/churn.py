import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚠️ Churn Prediction")

# Load Dataset
data = pd.read_csv("database/customer_dataset.csv")

st.subheader("📋 Customer Dataset")
st.dataframe(data)

# Select Customer
customer_id = st.selectbox(
    "Select Customer ID",
    data["CustomerID"]
)

if st.button("Predict Churn"):

    customer = data[
        data["CustomerID"] == customer_id
    ].iloc[0]

    age = customer["Age"]
    income = customer["Income"]
    tenure = customer["Tenure"]
    purchase = customer["Purchase"]

    # Improved Churn Logic
    churn = 0

    if tenure < 6:
        churn += 50

    elif tenure < 12:
        churn += 30

    else:
        churn += 10

    if income < 30000:
        churn += 30

    elif income < 60000:
        churn += 15

    if purchase == 0:
        churn += 20

    churn = min(churn, 100)

    st.error(
        f"⚠️ Churn Risk : {churn}%"
    )

    st.progress(churn)

    # Result Table
    st.subheader("📊 Churn Prediction Result")

    result_table = pd.DataFrame({
        "CustomerID": [customer_id],
        "Age": [age],
        "Income": [income],
        "Tenure": [tenure],
        "Purchase": [purchase],
        "Churn Risk (%)": [churn]
    })

    st.table(result_table)

    # Dynamic Pie Chart
    st.subheader("🥧 Churn Prediction Pie Chart")

    pie_data = pd.DataFrame({
        "Status": [
            "Churn Risk",
            "Customer Retained"
        ],
        "Value": [
            churn,
            100 - churn
        ]
    })

    fig = px.pie(
        pie_data,
        names="Status",
        values="Value",
        title=f"Customer {customer_id} Churn Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Summary Table
    st.subheader("📈 Dataset Summary")

    summary = pd.DataFrame({
        "Metric": [
            "Total Customers",
            "Average Income",
            "Average Tenure"
        ],
        "Value": [
            len(data),
            round(data["Income"].mean(), 2),
            round(data["Tenure"].mean(), 2)
        ]
    })

    st.table(summary)