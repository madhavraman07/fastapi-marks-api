from fastapi import FastAPI, Request
import json
from fastapi.responses import JSONResponse

app = FastAPI()

with open("q-vercel-python.json", "r") as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    results = [marks_data.get(name, "Not found") for name in names]
    return JSONResponse(content=results)
