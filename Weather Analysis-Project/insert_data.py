from sqlalchemy import create_engine
import pandas as pd
from data_fetching import fetch_weather

def insert_data():
    engine = create_engine("postgresql://postgres:akks1925%40@localhost/weather_data")

    # Row count before insert
    
    # Just to check how many new rows are inserted each time when i call the sedular via add_seduling.py 
    try:
        before = pd.read_sql("SELECT COUNT(*) FROM weather_update", engine).iloc[0, 0]   # count along horizontal axis(0) 
        print("Rows before insert:", before)
    except Exception as e:
        print("Failed to fetch row count before insert:", e)
        return

    # Fetch data
    try:
        df = fetch_weather()
        print("Weather data fetched, shape:", df.shape)
    except Exception as e:
        print("Failed to fetch weather data:", e)
        return

    # Insert into DB
    try:
        df.to_sql("weather_update", engine, if_exists="append", index=False, method='multi')
        print("Data inserted successfully.")
    except Exception as e:
        print("Error inserting data:", e)
        return
    
    #    moving average 
    try: 
        df['time'] = pd.to_datetime(df['time'])
        df['date'] = df['time'].dt.date

        daily = df.groupby('date').agg({
       'temperature_2m': 'mean',
       'relative_humidity_2m': 'mean',
       'precipitation': 'mean'
   }).reset_index()

        daily['moving_avg_temp'] = daily['temperature_2m'].rolling(window=7).mean()
        daily['moving_avg_humidity'] = daily['relative_humidity_2m'].rolling(window=7).mean()
        daily['moving_avg_precipitation'] = daily['precipitation'].rolling(window=7).mean()

        daily.to_sql("moving_average", engine, if_exists="replace", index=False, method='multi')

    except Exception as e:
        print("Error inserting data:", e)
        return

 
    # Row count after insert
    try:
        after = pd.read_sql("SELECT COUNT(*) FROM weather_update", engine).iloc[0, 0]
        print("Rows after insert:", after)
        print(f"Rows inserted: {after - before}")
    except Exception as e:
        print("Failed to fetch row count after insert:", e)

if __name__ == "__main__":
    insert_data()


