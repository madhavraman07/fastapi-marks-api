from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Load data once when app starts
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str]):
    results = [data.get(n, "Not found") for n in name]
    return JSONResponse(content=results)
