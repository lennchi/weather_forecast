import requests
import streamlit as st
import os
from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv('API_KEY')

api_key = st.secrets["api_key"]

def get_data(place, days, data_type):
    api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(api_url)
    response = response.json()

    # Extract date/time and data points (temp or sky conditions) for specified number of days
    dt_points = []
    data = []
    for i in range(days * 8):
        # Add datetime points
        dt = response['list'][i]['dt_txt']
        dt_points.append(dt)

        # Add temp or sky condition points
        if data_type == "Temperature":
            temp_raw = response['list'][i]['main']['temp']
            temp_point = round(temp_raw / 10, 1)
            data.append(temp_point)
        else:
            sky_point = response['list'][i]['weather'][0]['main']
            data.append(sky_point)

    return dt_points, data


if __name__ == "__main__":
    data = get_data("Liberec", 1, "Sky Conditions")
    weather_data = data[1]
    print(weather_data)
    sky_images = {"Clear": "img/clear.png", "Clouds": "img/cloud.png", "Rain": "img/rain.png",
                  "Snow": "img/snow.png"}
    icons = [sky_images[condition] for condition in weather_data]
    print(icons)
