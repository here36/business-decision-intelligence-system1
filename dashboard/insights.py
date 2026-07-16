import streamlit as st


def business_insights(df):

    st.divider()

    st.subheader("💡 Business Insights")

    category_sales = df.groupby("Category")["Sales"].sum()
    category_profit = df.groupby("Category")["Profit"].sum()
    region_sales = df.groupby("Region")["Sales"].sum()
    segment_sales = df.groupby("Segment")["Sales"].sum()

    st.success(
        f"Highest Revenue Category: **{category_sales.idxmax()}** "
        f"(₹{category_sales.max():,.2f})"
    )

    st.success(
        f"Most Profitable Category: **{category_profit.idxmax()}** "
        f"(₹{category_profit.max():,.2f})"
    )

    st.info(
        f"Best Performing Region: **{region_sales.idxmax()}** "
        f"(₹{region_sales.max():,.2f})"
    )

    st.info(
        f"Top Customer Segment: **{segment_sales.idxmax()}** "
        f"(₹{segment_sales.max():,.2f})"
    )

    st.warning(
        f"Lowest Profit Category: **{category_profit.idxmin()}** "
        f"(₹{category_profit.min():,.2f})"
    )