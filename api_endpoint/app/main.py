import dbhandler

import uvicorn

from typing import List, Dict
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/data/s={start_time}&e={end_time}&bbox={top_lat},{top_lon},{bottom_lat},{bottom_lon}")
def get_data(
        start_time: str,
        end_time: str,
        top_lat: str,
        top_lon: str,
        bottom_lat: str,
        bottom_lon: str
) -> JSONResponse:
    data: List[Dict] = []
    try:
        data = dbhandler.get_result(
            start_time, end_time, top_lat, top_lon, bottom_lat, bottom_lon)
        response = {
            "timeRange": f"{start_time} - {end_time}",
            "boundingBox": f"{top_lat}, {top_lon}, {bottom_lat}, {bottom_lon}",
            "data": data
        }
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        ) from e


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001)
