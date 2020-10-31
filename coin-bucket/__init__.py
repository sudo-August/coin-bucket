import os, websocket, json, csv
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine, Column, Integer, String, Float
from pathlib import Path
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
load_dotenv()






"""
        DATABASE
"""

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
    price = Column(String)
    open_24h = Column(String)
    volume_24h = Column(String)
    low_24h = Column(String)
    high_24h = Column(String)
    volume_30d = Column(String)
    best_bid = Column(String)
    best_ask = Column(String)
    side = Column(String)
    time = Column(String)
    trade_id = Column(Integer)
    last_size = Column(String)

    def __repr__(self):
        return "<Transaction(type='%s', sequence='%d', product_id='%s', price='%s', open_24h='%s', volume_24h='%s', low_24h='%s', high_24h='%s', volume_30d='%s', best_bid='%s', best_ask='%s', side='%s', time='%s', trade_id='%d', last_size='%s')>" % (
            self.type, self.sequence, self.product_id, self.price, self.open_24h, self.volume_24h, self.low_24h, self.high_24h, self.volume_30d, self.best_bid, self.best_ask, self.side, self.time, self.trade_id, self.last_size
        )





"""
        COINBASE
"""


to_add = []
def write_db():
    print("adding")
    session.add_all(to_add)
    to_add = []
    print(to_add)
    session.commit()
    print("committed")


def on_open(ws):
    print("opened connection")

    subscribe_message = {
        "type": "subscribe",
        "channels": [
            {
                "name": "ticker",
                "product_ids": [
                    "BTC-USD",
                    "XRP-USD",
                    "ETH-USD"
                ]
            }
        ]
    }

    ws.send(json.dumps(subscribe_message))

def on_message(ws, message):
    tick = json.loads(message)
    session.add(Transaction(type=tick['type'], sequence=tick['sequence'], product_id=tick['product_id'], price=tick['price'], open_24h=tick['open_24h'], volume_24h=tick['volume_24h'], low_24h=tick['low_24h'], high_24h=tick['high_24h'], volume_30d=tick['volume_30d'], best_bid=tick['best_bid'], best_ask=tick['best_ask'], side=tick['side'], time=tick['time'], trade_id=tick['trade_id'], last_size=tick['last_size']))
    session.commit()
    #to_add.append(Transaction(type=tick['type'], sequence=tick['sequence'], product_id=tick['product_id'], price=tick['price'], open_24h=tick['open_24h'], volume_24h=tick['volume_24h'], low_24h=tick['low_24h'], high_24h=tick['high_24h'], volume_30d=tick['volume_30d'], best_bid=tick['best_bid'], best_ask=tick['best_ask'], side=tick['side'], time=tick['time'], trade_id=tick['trade_id'], last_size=tick['last_size']))
    #if len(to_add) >= 5:
    #    write_db()
    print(tick)

socket = "wss://ws-feed.pro.coinbase.com"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)




"""
        WEB SERVER
"""

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'hello world'

    @app.route('/status')
    def status():
        return 'running...'

    @app.route('/start')
    def commence_suckdown():
        ws.run_forever()

    return app