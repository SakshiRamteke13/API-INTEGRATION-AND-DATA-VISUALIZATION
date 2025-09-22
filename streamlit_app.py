import streamlit as st
from weather_api import fetch_forecast, forecast_to_df

st.set_page_config(page_title="Weather Visualizer", layout="centered")
st.title("Task-1: API Integration & Data Visualization")

with st.form("settings"):
    lat = st.number_input("Latitude", value=19.0760, format="%.6f")
    lon = st.number_input("Longitude", value=72.8777, format="%.6f")
    days = st.slider("Forecast days", min_value=1, max_value=7, value=2)
    submitted = st.form_submit_button("Fetch & Visualize")

if submitted:
    try:
        js = fetch_forecast(latitude=lat, longitude=lon, days=days)
        df = forecast_to_df(js)

        st.subheader("Raw data (first 12 rows)")
        st.dataframe(df.head(12))

        st.subheader("Temperature over time")
        st.line_chart(df.set_index("time")[["temperature_2m"]])

        st.subheader("Summary statistics")
        st.table(df[["temperature_2m","relative_humidity_2m","windspeed_10m"]].describe().round(2))

    except Exception as e:
        st.error(f"Failed to fetch data: {e}")
