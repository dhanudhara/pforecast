# import requests
import uvicorn
import json

from fastapi import FastAPI  # , HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()
# DATABASE_URL = ""


@app.get("/data")
def get_data():
    return JSONResponse(
        status_code=404,
        content={"status": "404", "msg": "service unavailable"}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001)
