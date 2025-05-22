import requests
import pandas as pd

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 28.61, 
        "longitude": 77.23,
        "hourly": "temperature_2m,relative_humidity_2m,precipitation",
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data['hourly'])
    df['time'] = pd.to_datetime(df['time'])
 
   
    df = df.dropna()
    df = df.drop_duplicates()
    return df
