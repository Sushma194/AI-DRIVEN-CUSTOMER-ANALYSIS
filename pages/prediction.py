import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🛒 Purchase Prediction")

# Input Fields
age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=25
)

income = st.number_input(
    "Income",
    min_value=0.0,
    value=30000.0
)

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    value=12
)

if st.button("Predict Purchase"):

    # Prediction Logic
    probability = 0

    if income > 50000:
        probability += 40

    if tenure > 12:
        probability += 40

    if age < 40:
        probability += 20

    probability = min(probability, 100)

    # Prediction Result
    if probability >= 70:
        prediction = "Likely To Purchase"
    else:
        prediction = "Not Likely To Purchase"

    st.success(
        f"Prediction Result: {prediction}"
    )

    st.info(
        f"Purchase Probability: {probability}%"
    )

    st.progress(probability)

    # Result Table
    st.subheader("📋 Prediction Result")

    result_table = pd.DataFrame({
        "Prediction": [prediction],
        "Probability (%)": [probability]
    })

    st.table(result_table)

    # Customer Details Table
    st.subheader("📊 Customer Details")

    customer_table = pd.DataFrame({
        "Attribute": [
            "Age",
            "Income",
            "Tenure"
        ],
        "Value": [
            age,
            income,
            tenure
        ]
    })

    st.table(customer_table)

    # Pie Chart
    st.subheader("🥧 Purchase Prediction Pie Chart")

    pie_data = pd.DataFrame({
        "Status": [
            "Likely To Purchase",
            "Not Likely To Purchase"
        ],
        "Value": [
            probability,
            100 - probability
        ]
    })

    pie_fig = px.pie(
        pie_data,
        names="Status",
        values="Value",
        title="Purchase Prediction Distribution"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

    # Bar Chart
    st.subheader("📈 Purchase Prediction Graph")

    graph_data = pd.DataFrame({
        "Category": [
            "Likely To Purchase",
            "Not Likely To Purchase"
        ],
        "Value": [
            probability,
            100 - probability
        ]
    })

    st.bar_chart(
        graph_data.set_index("Category")
    )