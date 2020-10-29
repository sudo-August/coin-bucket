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
    

socket = "wss://ws-feed.pro.coinbase.com"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()