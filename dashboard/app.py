import streamlit as st
import sys
import os

st.set_page_config(
    page_title="Business Decision Intelligence System",
    page_icon="📊",
    layout="wide"
)

# Allow Streamlit to access the python folder
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "python"))

from data_loader import load_data

# Load data
df = load_data()
st.sidebar.title("📊 Dashboard Filters")

st.sidebar.markdown("---")

st.sidebar.write("Use the filters below to analyze specific data.")

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

if selected_region != "All":
    df = df[df["Region"] == selected_region]

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

if selected_category != "All":
    df = df[df["Category"] == selected_category]
# ----------------------------
# Calculate KPIs
# ----------------------------

total_revenue = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = len(df)

unique_customers = df["Customer ID"].nunique()

loss_products = df[df["Profit"] < 0]["Product Name"].nunique()

# ----------------------------
# Dashboard Title
# ----------------------------

st.title("📊 Business Decision Intelligence System")

st.write("A Data Analytics Dashboard built using Python and Streamlit")

# ----------------------------
# KPI Cards
# ----------------------------

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"₹{total_revenue:,.2f}")

col2.metric("📈 Total Profit", f"₹{total_profit:,.2f}")

col3.metric("📦 Total Orders", total_orders)

col4, col5 = st.columns(2)

col4.metric("👥 Unique Customers", unique_customers)

col5.metric("❌ Loss Products", loss_products)

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
st.divider()

st.caption(
    "Business Decision Intelligence System | Built using Python, Pandas, SQL, Matplotlib and Streamlit"
)
st.divider()

st.subheader("📋 Dataset Preview")

st.dataframe(df)
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)