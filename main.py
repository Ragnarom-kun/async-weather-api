from fastapi import FastAPI
from weather_api.api.weather import weather_router

app = FastAPI()

app.include_router(weather_router)
