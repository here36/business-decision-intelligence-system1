import streamlit as st
import sys
import os
from sidebar import sidebar_filters
from metrics import get_metrics
from insights import business_insights
from charts import sales_by_category_chart
from charts import (
    sales_by_category_chart,
    monthly_revenue_chart,
    sales_by_segment_chart,
    profit_by_region_chart,
    top_products_chart,
    loss_products_chart,
)
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
df = sidebar_filters(df)

(
    total_revenue,
    total_profit,
    total_orders,
    unique_customers,
    loss_products,
) = get_metrics(df)

# ----------------------------
# Dashboard Title
# ----------------------------

st.title("📊 Business Decision Intelligence System")

st.markdown("""
### Interactive Sales Analytics Dashboard
""")

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

col1, col2 = st.columns(2)

with col1:
    sales_by_category_chart(df)

with col2:
    sales_by_segment_chart(df)




col3, col4 = st.columns(2)

with col3:
    monthly_revenue_chart(df)

with col4:
    profit_by_region_chart(df)

col5, col6 = st.columns(2)

with col5:
    top_products_chart(df)

with col6:
    loss_products_chart(df)


business_insights(df)

st.divider()

st.caption(
    "Business Decision Intelligence System | Built using Python, Pandas, SQL, Matplotlib and Streamlit"
)
st.divider()

st.subheader("📋 Filtered Dataset Preview")

st.write("Showing the data after applying the selected filters.")

st.dataframe(df)
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
   label="📥 Download Filtered Dataset (CSV)",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)
