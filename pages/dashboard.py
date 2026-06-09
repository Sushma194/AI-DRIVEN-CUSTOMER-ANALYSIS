import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Customer Analytics Dashboard")

# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Customers", "1000")
col2.metric("Revenue", "₹500000")
col3.metric("Orders", "3500")
col4.metric("Retention", "85%")

st.divider()

# Customer Distribution Pie Chart
st.subheader("Customer Distribution Analysis")

customer_data = pd.DataFrame({
    "Category": [
        "Premium",
        "Regular",
        "Budget"
    ],
    "Customers": [
        150,
        500,
        350
    ]
})

fig = px.pie(
    customer_data,
    names="Category",
    values="Customers",
    title="Customer Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("""
### Analysis
- Regular customers represent the largest customer segment.
- Premium customers contribute higher revenue.
- Budget customers can be targeted using discount campaigns.
""")

st.divider()

# Revenue Analysis
st.subheader("Revenue Trend")

revenue_data = pd.DataFrame({
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],
    "Revenue": [
        100000,
        120000,
        150000,
        180000,
        220000,
        260000
    ]
})

st.line_chart(
    revenue_data.set_index("Month")
)

st.write("""
### Revenue Insights
- Revenue is growing consistently.
- Strong customer engagement.
- Positive sales trend.
""")

st.divider()

# Product Category Analysis
st.subheader("Orders by Category")

orders = pd.DataFrame({
    "Category": [
        "Electronics",
        "Fashion",
        "Groceries",
        "Sports"
    ],
    "Orders": [
        800,
        650,
        1200,
        350
    ]
})

fig2 = px.pie(
    orders,
    names="Category",
    values="Orders",
    title="Orders by Product Category"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

