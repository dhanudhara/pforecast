import dbhandler

import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/data/s={stime}&e={etime}&bbox={tlat},{tlon},{blat},{blon}")
def get_data(
        stime: str,
        etime: str,
        tlat: str,
        tlon: str,
        blat: str,
        blon: str
):
    # result = dbhandler.get_result(stime, tlat, tlon, blat, blon)
    # print(result)
    return JSONResponse(
        status_code=404,
        content={
            "timeRange": f"{stime} - {etime}",
            "boundingBox": ",".join([tlat, tlon, blat, blon]),
            "data": [
                # dbhandler.get_result(stime, tlat, tlon, blat, blon),
                "Unavailable at the moment"
            ]
        }
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001)
