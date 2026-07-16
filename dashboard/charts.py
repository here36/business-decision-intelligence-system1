import streamlit as st
import matplotlib.pyplot as plt


def sales_by_category_chart(df):

    st.divider()

    st.subheader("📊 Sales by Category")

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    st.bar_chart(
        category_sales,
        x="Category",
        y="Sales"
    )


def monthly_revenue_chart(df):

    st.divider()

    st.subheader("📈 Monthly Revenue Trend")

    monthly_sales = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
        .reset_index()
    )

    monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

    st.line_chart(
        monthly_sales,
        x="Order Date",
        y="Sales"
    )


def sales_by_segment_chart(df):

    st.divider()

    st.subheader("🥧 Sales by Customer Segment")

    segment_sales = (
        df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
    )

    st.bar_chart(
        segment_sales,
        x="Segment",
        y="Sales"
    )


def profit_by_region_chart(df):

    st.divider()

    st.subheader("📊 Profit by Region")

    region_profit = (
        df.groupby("Region")["Profit"]
        .sum()
        .reset_index()
    )

    st.bar_chart(
        region_profit,
        x="Region",
        y="Profit"
    )


def top_products_chart(df):

    st.divider()

    st.subheader("🏆 Top 10 Products by Sales")

    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    st.dataframe(
        top_products,
        use_container_width=True,
        hide_index=True
    )


def loss_products_chart(df):

    st.divider()

    st.subheader("📉 Top 10 Loss-Making Products")

    loss_products = (
        df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values()
        .head(10)
        .reset_index()
    )

    st.dataframe(
        loss_products,
        use_container_width=True,
        hide_index=True
    )
   
