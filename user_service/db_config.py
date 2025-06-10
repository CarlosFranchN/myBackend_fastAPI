import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def get_db_conn():
    db_user = os.getenv("user")
    db_password = os.getenv("password")
    db_host = os.getenv("host")
    db_port = os.getenv("port")
    db_name = os.getenv("dbname")

    if not all([db_user, db_password, db_host, db_port, db_name]):
        raise ValueError("Uma ou mais variáveis de ambiente não foram definidas.")

    return psycopg2.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        dbname=db_name
    )