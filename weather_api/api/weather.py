import asyncio
import httpx
from fastapi import APIRouter
from weather_api.models.models import City, WeatherResponse, ForecastResponse
from weather_api.core.config import WEATHER_API_KEY, WEATHER_API_BASE_URL

weather_router = APIRouter()

async def get_current_weather(city: str) -> WeatherResponse:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{WEATHER_API_BASE_URL}/weather",
            params={"q": city, "appid": WEATHER_API_KEY, "units": "metric"},
        )
        response.raise_for_status()
        data = response.json()
        return WeatherResponse(
            temperature=data["main"]["temp"],
            feels_like=data["main"]["feels_like"],
            description=data["weather"][0]["description"],
        )

async def get_5day_forecast(city: str) -> ForecastResponse:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{WEATHER_API_BASE_URL}/forecast",
            params={"q": city, "appid": WEATHER_API_KEY, "units": "metric"},
        )
        response.raise_for_status()
        data = response.json()
        forecast_data = []
        for item in data["list"]:
            forecast_data.append(
                {"datetime": item["dt_txt"], "temperature": item["main"]["temp"]}
            )
        return ForecastResponse(forecast=forecast_data)

@weather_router.get("/weather/{city_name}", response_model=WeatherResponse)
async def weather(city_name: str):
    return await get_current_weather(city_name)

@weather_router.get("/forecast/{city_name}", response_model=ForecastResponse)
async def forecast(city_name: str):
    return await get_5day_forecast(city_name)