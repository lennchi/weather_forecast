import streamlit as st
import plotly.express as px

import requests
import pandas as pd
from backend import get_data


st.title("Weather Forecast")


place = st.text_input("Place:", value="Tirana")

days = st.slider("Forecast Days", min_value=1, max_value=5, value=1, step=1, help="How many days into the future do "
                                                                                  "you want to see?")

option = st.selectbox("Select data to view", ("Temperature", "Sky conditions"))

# Load weather data from the Openweather API
weather_data = get_data(place, days, option)

# Chart title
if days == 1:
    st.subheader(f"{option} for the next 24 hours in {place}")
else:
    st.subheader(f"{option} for the next {days} days in {place}")

# Date and time, weather data points
dt_points = weather_data[0]
weather_data_points = weather_data[1]

# Temperature chart
if option == "Temperature":
    fig = px.line(x=dt_points, y=weather_data_points, labels={"x": "Date/time ", "y": "Temperature (°C) "})
    st.plotly_chart(fig)

# Sky conditions chart
else:
    st.image(weather_data_points)

