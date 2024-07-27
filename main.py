import streamlit as st
import pandas as pd


st.title("Weather Forecast")

place = st.text_input("Place:", value="Tirana")

days = st.slider("Forecast Days", min_value=1, max_value=5, value=1, step=1, help="How many days into the future do "
                                                                                  "you want to see?")

option = st.selectbox("Select data to view", ("Temperature", "Sky conditions"))

# weather_data = get_weather_data(place, forecast_days)

if days == 1:
    st.subheader(f"{option} for the next 24 hours in {place}")
else:
    st.subheader(f"{option} for the next {days} days in {place}")


# if data_type == "Temperature":
#     fig = px.line(weather_data, x='date', y='temperature', labels={'date': 'Date', 'temperature': 'Temperature (C)'})
#     st.plotly_chart(fig)