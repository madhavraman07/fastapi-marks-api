from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1. Enable CORS for *all* origins, methods, and headers:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # any domain
    allow_methods=["GET"],      # or ["*"] for all methods
    allow_headers=["*"],        # any headers
)

# 2. Dummy data (replace with your q-vercel-python.json load)
marks_data = {
    "X": 10,
    "Y": 20,
    # … all your student entries …
}

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    # Build the list in the same order as query params
    result_list = [marks_data.get(n, None) for n in name]
    return {"marks": result_list}
