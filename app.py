import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="My Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 My First Streamlit Dashboard")
st.write("Welcome to my dashboard deployment assignment!")

# Sample data
data = {
    "Month": ["January", "February", "March", "April", "May"],
    "Sales": [12000, 15000, 11000, 18000, 22000],
    "Orders": [120, 150, 110, 180, 220]
}

df = pd.DataFrame(data)

# Dashboard metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{df['Sales'].sum():,}")
col2.metric("Total Orders", f"{df['Orders'].sum():,}")
col3.metric("Average Sales", f"₹{df['Sales'].mean():,.0f}")

# Interactive chart
st.subheader("Monthly Sales Chart")

fig = px.bar(
    df,
    x="Month",
    y="Sales",
    color="Month",
    title="Sales by Month"
)

st.plotly_chart(fig, use_container_width=True)

# Display table
st.subheader("Sales Details")
st.dataframe(df, use_container_width=True)