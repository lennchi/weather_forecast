import streamlit as st
import plotly.express as px

import requests
import pandas as pd
from backend import get_data


st.title("Weather Forecast")


place = st.text_input("Place:", value="Prague")

days = st.slider("Forecast Days", min_value=1, max_value=5, value=1, step=1, help="How many days into the future do "
                                                                                  "you want to see?")

option = st.selectbox("Select data to view", ("Temperature", "Sky conditions"))

if place:
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
    elif option == "Sky conditions":
        sky_images = {"Clear": "img/clear.png", "Clouds": "img/cloud.png", "Rain": "img/rain.png",
                      "Snow": "img/snow.png"}
    #
    #     icons = [sky_images[condition] for condition in weather_data_points]
    #
    #     st.image(icons, width=88)

        # Iterate over dt_points and weather_data_points in chunks of icons_per_row
        icons_per_row = 8
        nr_data_points = len(weather_data_points)

        for i in range(0, nr_data_points, icons_per_row):
            cols = st.columns(icons_per_row)
            for col, dt_point, condition in zip(cols, dt_points[i:i + icons_per_row], weather_data_points[i:i + icons_per_row]):
                icon = sky_images.get(condition)
                with col:
                    st.image(icon, width=88, caption=dt_point[:-3])
