from fastapi import FastAPI

app = FastAPI(
    title="Тест API для Docker"
)

@app.get("/")
def home_page():
    return None

