from typing import Dict, List
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import (
    create_engine,
    Column,
    TEXT,
    FLOAT,
    DOUBLE,
)


DB_USER = 'root'
DB_PSWD = 'password'
HOST = 'mysqldb:3306'
DB_NAME = 'plastic'
DB_URL = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
    DB_USER,
    DB_PSWD,
    HOST,
    DB_NAME
)
engine = create_engine(DB_URL)
Base = declarative_base()


class Plastics(Base):
    __tablename__ = 'plastics'
    time = Column(TEXT, primary_key=True)
    lat = Column(FLOAT, primary_key=True)
    lon = Column(FLOAT, primary_key=True)
    mp_conc = Column(FLOAT)
    num_mp_samples = Column(DOUBLE)
    stddev_mp_samples = Column(FLOAT)


def get_result(
    time,
    tlat, tlon,
    blat, blon
) -> List[str]:
    with Session() as session:
        result = session.query(Plastics).filter(
            # Plastics.time == time,
            Plastics.lat <= tlat,
            Plastics.lat >= blat,
            Plastics.lon <= tlon,
            Plastics.lon >= blon,
        ).all()
        return [
            f"time: {row.time}, lat: {row.lat}, lon: {row.lon}, mp_conc: {row.mp_conc}, num_mp_samples: {row.num_mp_samples}, stddev_mp_samples: {row.stddev_mp_samples}"
            for row in result
        ]
