from pydantic import BaseModel
from typing import List

class City(BaseModel):
    name: str

class WeatherResponse(BaseModel):
    temperature: float
    feels_like: float
    description: str

class ForecastData(BaseModel):
    datetime: str
    temperature: float

class ForecastResponse(BaseModel):
    forecast: List[ForecastData]
