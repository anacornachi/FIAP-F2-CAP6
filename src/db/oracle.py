import oracledb
from dotenv import load_dotenv
import os

load_dotenv()
#
DB_USER = os.getenv("ORACLE_USER")
DB_PASSWORD = os.getenv("ORACLE_PASSWORD")
DB_HOST = os.getenv("ORACLE_HOST")
DB_PORT = os.getenv("ORACLE_PORT")
DB_SERVICE = os.getenv("ORACLE_SERVICE")


def get_connection():
    dsn = f"{DB_HOST}:{DB_PORT}/{DB_SERVICE}"
    return oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=dsn)
