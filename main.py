from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Load data once at startup
with open("q-vercel-python.json") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    # For each requested name, find marks in the data or return None if not found
    results = []
    for n in name:
        mark = marks_data.get(n)
        results.append({"name": n, "marks": mark})
    return JSONResponse(content=results)
