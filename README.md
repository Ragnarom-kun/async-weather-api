# Asynchronous Weather API
## For LAW's Individual Assignment 2
### Romi Fadhurrohman Nabil (2006535016)
This is a web service that provides current weather and 5-day forecast data for a given city. The service is built using FastAPI, with data sourced from the OpenWeatherMap API.

## Usage

To use the service, send GET requests to the following endpoints:

- `/weather/{city_name}`: Returns the current weather data for a given city.
- `/forecast/{city_name}`: Returns the 5-day forecast data for a given city.

Replace `{city_name}` with the name of the city you'd like to retrieve data for.

### Example Request

curl http://localhost:8000/weather/london

### Example Response

{
    "temperature": 15.0,
    "feels_like": 14.5,
    "description": "overcast clouds"
}

## Requirements

- Python 3
- Node.js
- npm

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment for the project and activate it:
```
python3 -m venv venv
source venv/bin/activate
```
3. Install the Python dependencies :
```
pip install -r requirements.txt
```
4. Install the Node.js dependencies :
```
cd static
npm install
```

## Configuration
Before running the web service, you need to set the following environment variables :

* WEATHER_API_KEY: Your API key from OpenWeather.
* WEATHER_API_BASE_URL: The base URL of the OpenWeather API.

You can set these variables either in your system environment or in a .env file in the project directory.

Here's an example .env file:
```
WEATHER_API_KEY=your_api_key_here
WEATHER_API_BASE_URL=https://api.openweathermap.org/data/2.5
```

## Usage
To run the web service, activate the virtual environment and start the server :
```
source venv/bin/activate
uvicorn main:app --reload
```
Then, open your browser and go to http://localhost:8000 to access the web service.

## API Endpoints

- `/` : The home page of the web service.
- `/weather/{city_name}` : Retrieves the current weather data for the specified city.
- `/forecast/{city_name}` : Retrieves the 5-day weather forecast for the specified city.