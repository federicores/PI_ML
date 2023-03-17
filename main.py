from fastapi import FastAPI
#from config import settings

app = FastAPI()

@app.get("/")
def hello_api():
    return {"msg":"Hello API"}