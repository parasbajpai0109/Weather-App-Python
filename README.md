# Weather App 🌦️
A simple command-line Weather Application built with Python that fetches real-time weather information using the WeatherAPI service.
## Features
- Search for the weather by city name
- Displays:
  - City Name
  - Region Name
  - Country Name
  - Local Time
  - Temperature (°C)
  - Feels Like Temperature (°C)
  - Humidity (%)
  - Wind Speed (km/h)
  - Weather Condition
- Handles invalid city names
- Allows multiple searches without restarting the application
- Exit option using q

## Technologies Used
- Python 
- Requests Library
- WeatherAPI

## Installation
1- Clone the repository:
```blash
    https://github.com/your-username/weather-app-python.git
```
2- Navigate to the project directory:
```blash
    cd weather-app-python
```
3- Install dependencies:
```blash
    pip install requests
```
## Usage
1- Get your free API key from WeatherAPI.
2- Replace:
api_key = "YOUR_API_KEY"

with your actual API key.

3- Run the application:
```blash
python weather.py
```
## Example Output

```text
Weather Report

City Name: Delhi
Region Name: Delhi
Country Name: India
Local Time: 2026-06-09 12:30
Temperature: 40.3°C
Feels Like: 42.3°C
Humidity: 25%
Wind Speed: 18.0 km/h
Condition: Severe sandstorm
```
## Author
Paras Bajpai
