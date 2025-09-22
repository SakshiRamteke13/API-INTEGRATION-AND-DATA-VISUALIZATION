import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_forecast(latitude=19.0760, longitude=72.8777, days=2):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,windspeed_10m",
        "forecast_days": days,
        "timezone": "auto"
    }
    resp = requests.get(BASE_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def forecast_to_df(json_data):
    hourly = json_data.get("hourly", {})
    df = pd.DataFrame(hourly)
    df['time'] = pd.to_datetime(df['time'])
    cols = ['time'] + [c for c in df.columns if c != 'time']
    return df[cols]

def save_outputs(df, out_dir="outputs"):
    p = Path(out_dir)
    p.mkdir(exist_ok=True)
    csv_path = p / "forecast.csv"
    png_path = p / "forecast_plot.png"
    df.to_csv(csv_path, index=False)

    plt.figure(figsize=(10,4))
    sns.lineplot(x="time", y="temperature_2m", data=df, marker="o")
    plt.xticks(rotation=45)
    plt.title("Temperature Forecast")
    plt.tight_layout()
    plt.savefig(png_path)
    plt.close()
    return csv_path, png_path

if __name__ == "__main__":
    print("Fetching forecast (Mumbai by default)...")
    data = fetch_forecast()
    df = forecast_to_df(data)
    print("\nFirst 5 rows of forecast data:")
    print(df.head().to_string(index=False))
    csv_file, png_file = save_outputs(df)
    print(f"\nSaved CSV -> {csv_file}")
    print(f"Saved plot -> {png_file}")
