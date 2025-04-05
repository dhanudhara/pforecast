import re
from typing import Dict, List
from flask import jsonify
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import (
    create_engine,
    text,
)


DB_USER = 'root'
DB_PSWD = 'password'  # get from the env file
HOST = 'mysqldb:3306'
DB_NAME = 'plastic'
DB_URL = (
    f'mysql+pymysql://{DB_USER}:{DB_PSWD}@{HOST}/{DB_NAME}'
)
engine = create_engine(DB_URL)
Base = declarative_base()


def format_result(row) -> Dict:
    return {
        "time": row.time,
        "lat": row.lat,
        "lon": row.lon,
        "mp_conc": row.mp_conc,
        "num_mp_samples": row.num_mp_samples,
        "stddev_mp_samples": row.stddev_mp_samples
    }


def get_result(
    start_time: str,
    end_time: str,
    top_lat: str,
    top_lon: str,
    bottom_lat: str,
    bottom_lon: str
) -> List[Dict]:
    tname: str = "plastics"  # TODO: get from sdtsl and edtsl
    query: str = text(
        f"""SELECT * FROM {tname.strip()}
                WHERE time >= :start_time AND time <= :end_time AND
                lat >= :top_lat AND lat <= :bottom_lat AND
                lon >= :top_lon AND lon <= :bottom_lon"""
    )
    params = {
        "start_time": start_time,
        "end_time": end_time,
        "top_lat": float(top_lat),
        "bottom_lat": float(bottom_lat),
        "top_lon": float(top_lon),
        "bottom_lon": float(bottom_lon)
    }
    with Session(engine) as session:
        result = session.execute(query, params)
        return [format_result(row) for row in result]
