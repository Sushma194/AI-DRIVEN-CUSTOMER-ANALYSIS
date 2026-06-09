import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

st.title("👥 Customer Segmentation Analysis")

try:

    data = pd.read_csv("database/customer_dataset.csv")

    st.subheader("📋 Customer Dataset")
    st.dataframe(data)

    st.write("Available Columns:")
    st.write(data.columns.tolist())

    if st.button("Generate Segmentation"):

        # Select columns automatically
        if "Income" in data.columns and "SpendingScore" in data.columns:
            X = data[["Income", "SpendingScore"]]
            x_col = "Income"
            y_col = "SpendingScore"

        elif "Income" in data.columns and "Tenure" in data.columns:
            X = data[["Income", "Tenure"]]
            x_col = "Income"
            y_col = "Tenure"

        else:
            st.error(
                "Dataset must contain either Income + SpendingScore or Income + Tenure"
            )
            st.stop()

        # KMeans
        kmeans = KMeans(
            n_clusters=3,
            random_state=42,
            n_init=10
        )

        data["Segment"] = kmeans.fit_predict(X)

        st.success(
            "✅ Customer Segmentation Generated Successfully"
        )

        # Segmented Dataset
        st.subheader("📊 Segmented Dataset")
        st.dataframe(data)

        # Segment Counts
        segment_counts = data["Segment"].value_counts().sort_index()

        # Analysis Table
        st.subheader("📑 Segment Analysis")

        analysis_df = pd.DataFrame({
            "Segment": [
                "Segment 0",
                "Segment 1",
                "Segment 2"
            ],
            "Customers": [
                segment_counts.get(0, 0),
                segment_counts.get(1, 0),
                segment_counts.get(2, 0)
            ]
        })

        st.table(analysis_df)

        # Bar Chart
        st.subheader("📈 Segment Distribution")

        st.bar_chart(
            analysis_df.set_index("Segment")
        )

        # Pie Chart
        st.subheader("🥧 Customer Segment Pie Chart")

        fig = px.pie(
            analysis_df,
            names="Segment",
            values="Customers",
            title="Customer Segment Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Scatter Plot
        st.subheader("📉 Customer Segmentation Scatter Plot")

        scatter_fig = px.scatter(
            data,
            x=x_col,
            y=y_col,
            color=data["Segment"].astype(str),
            title="Customer Segmentation"
        )

        st.plotly_chart(
            scatter_fig,
            use_container_width=True
        )

        # Average Statistics
        st.subheader("📊 Average Segment Statistics")

        summary = data.groupby("Segment")[
            [x_col, y_col]
        ].mean()

        st.dataframe(summary)

        # Metrics
        st.subheader("📌 Segment Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Segment 0",
            segment_counts.get(0, 0)
        )

        col2.metric(
            "Segment 1",
            segment_counts.get(1, 0)
        )

        col3.metric(
            "Segment 2",
            segment_counts.get(2, 0)
        )

        # Insights
        st.subheader("💡 Business Insights")

        st.write("""
        ✅ Segment 0 → Low Value Customers

        ✅ Segment 1 → Medium Value Customers

        ✅ Segment 2 → High Value Customers

        ✅ High Value Customers should receive premium offers.

        ✅ Medium Value Customers should receive personalized discounts.

        ✅ Low Value Customers should receive retention campaigns.
        """)

except FileNotFoundError:

    st.error(
        "❌ customer_dataset.csv not found inside database folder"
    )