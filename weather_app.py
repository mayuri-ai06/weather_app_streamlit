import streamlit as st 
import requests

api_key = "1550846e2c6a2c15a808066d94e3fa98"

st.title("🌩️ Weather App")
keyword = st.text_input("Enter Your City Name")
is_button_click= st.button("Search")

if is_button_click and keyword:
    url= f"https://api.openweathermap.org/data/2.5/weather?q={keyword}&appid={api_key}&units=metric"
    
    response= requests.get(url)
    status= response.status_code
    
    if status==200:
        data= response.json()
        temp = data["main"] ["temp"]
        humidity= data ["main"]["humidity"]

        st.info (f"Temperature: {temp}")
        st.info(f"Humidity : {humidity}")
    else:
        st.error("Something went wrong ❌")
        
        
        
