from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Привет, это мой первый DevOps-проект!"}

@app.get("/weather/{city}")
def get_weather(city: str):
    return {
        "city": city,
        "temperature": 22,
        "condition": "ясно"
    }

