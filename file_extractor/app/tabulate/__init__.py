import sqlalchemy

from pandas.core.frame import DataFrame

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
engine = sqlalchemy.create_engine(DB_URL)


def tabulate(df: DataFrame):
    df.to_sql(con=engine, name='plastics', if_exists='append', index=False)
