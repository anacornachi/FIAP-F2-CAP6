import oracledb

DB_USER = "RM564678"
DB_PASSWORD = "160600"
DB_HOST = "oracle.fiap.com.br"
DB_PORT = 1521
DB_SERVICE = "ORCL"


def get_connection():
    dsn = f"{DB_HOST}:{DB_PORT}/{DB_SERVICE}"
    return oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=dsn)
