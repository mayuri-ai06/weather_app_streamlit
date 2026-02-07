import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

st.title("🌩️ Weather App")
keyword = st.text_input("Enter Your City Name")
is_button_click = st.button("Search")

if is_button_click and keyword:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={keyword}&appid={api_key}&units=metric"

    response = requests.get(url)
    status = response.status_code

    if status == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        st.info(f"Temperature: {temp} °C")
        st.info(f"Humidity: {humidity}%")
    else:
        st.error("City not found or API key inactive ❌")
