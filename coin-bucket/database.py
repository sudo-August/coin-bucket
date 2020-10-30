import os
import pandas as pd 
from sqlalchemy import create_engine, Column, Integer, String, Float
from pathlib import Path
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()

URL = os.getenv("POSTGRES_URL")
USER = os.getenv("POSTGRES_USER")
PWD = os.getenv("POSTGRES_PWD")
DB = os.getenv("POSTGRES_DB")
SSLMODE = "require"
table_init = Path("../schema.sql")

engine = create_engine(f"postgresql://{USER}:{PWD}@{URL}:5432/{DB}")

class Transaction(Base):
    __tablename__='transactions'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    sequence = Column(Integer)
    product_id = Column(String)
    price = Column(Float)
    open_24h = Column(Float)
    volume_24h = Column(Float)
    low_24h = Column(Float)
    high_24h = Column(Float)
    volume_30d = Column(Float)
    best_bid = Column(Float)
    best_ask = Column(Float)
    side = Column(String)
    time = Column(String)
    trade_id = Column(Integer)
    last_size = Column(Float)

    def __repr__(self):
        return "<Transaction(type='%s', sequence='%d', product_id='%s', price='%f', open_24h='%f', volume_24h='%f', low_24h='%f', high_24h='%f', volume_30d='%f', best_bid='%f', best_ask='%f', side='%s', time='%s', trade_id='%d', last_size='%f')>" % (
            self.type, self.sequence, self.product_id, self.price, self.open_24h, self.volume_24h, self.low_24h, self.volume_30d, self.best_bid, self.best_ask, self.side, self.time, self.trade_id, self.last_size
        )


# erases table transactions if it exists and then recreates it with necessary columns
def init_db():
    con = engine.connect()
    con.execute("DROP TABLE IF EXISTS transactions")
    con.execute("CREATE TABLE transactions(type TEXT NOT NULL,sequence INT NOT NULL,product_id TEXT NOT NULL,price FLOAT NOT NULL,open_24h FLOAT NOT NULL,volume_24h FLOAT NOT NULL,low_24h FLOAT NOT NULL,high_24h FLOAT NOT NULL,volume_30d FLOAT NOT NULL,best_bid FLOAT NOT NULL,best_ask FLOAT NOT NULL,side TEXT NOT NULL,time TIMESTAMP NOT NULL,trade_id INT NOT NULL,last_size FLOAT NOT NULL);")
    con.close()

# function that takes a dictionary representing data coming in from the websocket to be written to the database
def commence_extraction(transaction):
    con = engine.connect()
    
    #con.execute("INSERT INTO transactions (type, sequence, product_id, price, open_24h, volume_24h, low_24h, high_24h, volume_30d, best_bid, best_ask, side, time, trade_id, last_size) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(transaction["type"],transaction["sequence"],transaction["product_id"],transaction["price"],transaction["open_24h"],transaction["volume_24h"],transaction["low_24h"],transaction["high_24h"],transaction["volume_30d"],transaction["best_bid"],transaction["best_ask"],transaction["side"],transaction["time"],transaction["trade_id"],transaction["last_size"],))
    con.close()

