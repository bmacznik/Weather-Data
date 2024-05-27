import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dash import Dash, dcc, html
# Gather Weather Data 
def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data
# Process Data
def process_weather_data(data):
    df = pd.DataFrame({
        'Temperature': [data['main']['temp']],
        'Humidity': [data['main']['humidity']],
        'Pressure': [data['main']['pressure']],
        'Wind Speed': [data['wind']['speed']]
    })
    return df
# Visualization
def plot_weather_data(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df)
    plt.title('Current Weather Data')
    plt.show()
# Build Dashboard
def build_dashboard(df):
    app = Dash(__name__)
    app.layout = html.Div([
        html.H1("Weather Data Dashboard"),
        dcc.Graph(
            id='weather-graph',
            figure={
                'data': [
                    {'x': df.columns, 'y': df.iloc[0], 'type': 'bar'}
                ],
                'layout': {
                    'title': 'Current Weather Data'
                }
            }
        )
    ])
    return app
# Main Function
if __name__ == '__main__':
    city = "Austin"
    api_key = "your_openweathermap_api_key"
    weather_data = fetch_weather_data(city, api_key)
    df = process_weather_data(weather_data)
    plot_weather_data(df)
    app = build_dashboard(df)
    app.run_server(debug=True)

