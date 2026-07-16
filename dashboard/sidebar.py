import streamlit as st

def sidebar_filters(df):

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

    st.sidebar.markdown("---")
    st.sidebar.caption("Built by Aaditi Salunkhe")

    return df