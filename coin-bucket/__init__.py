import os

from flask import Flask 
from . import database
from . import coinbase

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/init-db')
    def build_db():
        database.init_db()
        return 'table initialized'

    @app.route('/test-one')
    def test_one():
        transaction = {
            "type": "BTC-USD",
            "sequence": 1, 
            "product_id": "BTC", 
            "price": 12.23, 
            "open_24h": 534.2, 
            "volume_24h": 32.23, 
            "low_24h": 22.43, 
            "high_24h": 543.3, 
            "volume_30d": 542.75, 
            "best_bid": 12.3, 
            "best_ask": 23.43, 
            "side": "side", 
            "time": "TIME",
            "trade_id": 324,
            "last_size": 323.2
        }
        database.commence_extraction(transaction)
        return "transaction maybe completed"

    @app.route('/start-pour')
    def pouring():
        coinbase.start_pour()
        return "maybe started pouring"

    @app.route('/stop-pour')
    def not_pouring():
        coinbase.stop_pour()
        return "should have stopped pouring"

    return app