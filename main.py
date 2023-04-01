from fastapi import FastAPI
from weather_api.api.weather import weather_router
from fastapi.responses import HTMLResponse

app = FastAPI()

app.include_router(weather_router)

# Mount the static files to the root path
@app.get("/")
async def read_index():
    with open("static/index.html") as f:
        html = f.read()
    return HTMLResponse(content=html, status_code=200)
