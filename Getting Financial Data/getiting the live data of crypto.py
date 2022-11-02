# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:17:21 2022

@author: Vineet
"""

#!pip install websocket-client

import websocket,json

cc = 'btcusd'
interval = '1m'
socket = f'wss://stream.binance.com:9443/ws/{cc}t@kline_{interval}'

closes, highs, lows  = [],[],[] 

def on_message(ws, message):
    json_message = json.loads(message)
    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']
    high = candle['h']
    low = candle['l']
    vol = candle['v']
    
    
    if is_candle_closed:
        closes.append(float(close))
        highs.append(float(high))
        lows.append(float(low))
        
        print(closes)
        print(highs)
        print(lows)

def on_close(ws, close_status_code, close_msg):
    print("connection closed")
   
ws = websocket.WebSocketApp(socket, on_message=on_message,on_close=on_close)

ws.run_forever()

    
    
    