#main.py

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello_api():
    return {"msg":"Hello API"}
