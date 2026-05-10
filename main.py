from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"FastAPI is working"}
def eyoba():
    return {"love eyob"}