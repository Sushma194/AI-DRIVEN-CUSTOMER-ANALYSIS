import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎁 Product Recommendations")

score = st.number_input(
    "Customer Score",
    min_value=0,
    max_value=100,
    value=50
)

if st.button("Generate Recommendations"):

    if score > 70:

        products = [
            "Premium Membership",
            "Luxury Products",
            "Cashback Offers"
        ]

        counts = [40, 35, 25]

        customer_type = "Premium Customer"

    else:

        products = [
            "Discount Coupons",
            "Budget Products",
            "Special Offers"
        ]

        counts = [50, 30, 20]

        customer_type = "Regular Customer"

    st.success(
        "✅ Recommendations Generated Successfully"
    )

    # Customer Type
    st.subheader("👤 Customer Type")
    st.write(customer_type)

    # Recommendations Table
    st.subheader("📋 Recommended Products")

    recommendation_table = pd.DataFrame({
        "Recommended Products": products
    })

    st.table(recommendation_table)

    # Customer Score Table
    st.subheader("📊 Customer Score")

    score_table = pd.DataFrame({
        "Metric": ["Customer Score"],
        "Value": [score]
    })

    st.table(score_table)

    # Pie Chart
    st.subheader("🥧 Product Recommendation Distribution")

    pie_data = pd.DataFrame({
        "Product": products,
        "Count": counts
    })

    fig = px.pie(
        pie_data,
        names="Product",
        values="Count",
        title="Recommended Products Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Bar Chart
    st.subheader("📈 Recommendation Analysis")

    st.bar_chart(
        pie_data.set_index("Product")
    )