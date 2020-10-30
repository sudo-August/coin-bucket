import websocket, json, csv
import dateutil.parser

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
    print(tick)

def stupid_run(pour):
    while pour:
        ws.run_forever()

def start_pour():
    POUR = True
    stupid_run(POUR)

def stop_pour():
    POUR = False
    stupid_run(POUR)

socket = "wss://ws-feed.pro.coinbase.com"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
#ws.run_forever()