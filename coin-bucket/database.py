import psycopg2, os
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
load_dotenv()

URL = os.getenv("POSTGRES_URL")
USER = os.getenv("POSTGRES_USER")
PWD = os.getenv("POSTGRES_PWD")
DB = os.getenv("POSTGRES_DB")
SSLMODE = "require"

DB_URL = 'postgresql+psycopg2://{user}:{pwd}@{url}/{db}'.format(user=USER,pwd=PWD,url=URL,db=DB)

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(URL, USER, DB, PWD, SSLMODE)
conn = psycopg2.connect(conn_string)
print("Connection established")