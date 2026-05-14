import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Demo App", layout="centered")

st.title("🚀 My First Streamlit App")

st.write("This is a simple demo app to test Streamlit deployment.")

# Load sample data
@st.cache_data
def load_data():
    return pd.read_csv("data/sample_data.csv")

df = load_data()

st.subheader("📊 Sample Data")
st.dataframe(df)

# Simple chart
st.subheader("📈 Chart")
st.line_chart(df["value"])

# User input
st.subheader("🔢 User Input")
number = st.slider("Select a number", 0, 100, 25)

st.write(f"You selected: {number}")
st.write(f"Squared value: {number**2}")

# Text input
name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}! 👋")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
