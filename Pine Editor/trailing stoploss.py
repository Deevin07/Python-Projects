# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:54:29 2022

@author: Vineet
"""
""""
Use pine editor for this
"""

//@version= 5
strategy("Trailing stoploss", overlay = true, initial_capital = 100000, default_qty_type=strategy.percent_of_equity)

//EMA
ema_input1 = input.int(200,'EMA lenght')
ema_ = ta.ema(close,ema_input1)

// trading logic
ema_buy_condition = ema_ < close
ema_sell_condition = ema_ > close

//Stoploss and target price
use_trailing_stop_loss  = input.bool(title = 'Use Trailing Stoploss', defval = true)

percent_based = input.float(10.0, '% Stop Multiplier', minval = 0.0, step = 0.5)
r_ratio = input.float(2.0, 'Risk Reward ratio', minval = 0.0, step = 0.5)
stop_loss_amount = close * percent_based/100

bought = strategy.position_size[0] > strategy.position_size[1]
since_entry_long = ta.barssince(bought)
sold = strategy.position_size[0] < strategy.position_size[1]
since_entry_short = ta.barssince(sold)

price_stop_long = 0.0
price_stop_short = 1000000000.0
targetvalue_long_1 = 0.0
targetvalue_short_1 = 0.0
stopvalue_long = 0.0
stopvalue_short = 0.0

//stoploss and target price
if (strategy.position_size>0)
    stopvalue_long := close - stop_loss_amount
    if use_trailing_stop_loss == false
        price_stop_long := close[since_entry_long] - stop_loss_amount[since_entry_long]
    else
        price_stop_long := math.max(stopvalue_long,price_stop_long[1])    
    targetvalue_long_1 := close[since_entry_long] + close[since_entry_long]*(percent_based/100)*r_ratio
else
    price_stop_long := 0.0


if (strategy.position_size<0)
    stopvalue_short := close + stop_loss_amount
    if use_trailing_stop_loss == false
        price_stop_short := close[since_entry_short] + stop_loss_amount[since_entry_short]
    else
        price_stop_short := math.min(stopvalue_short , price_stop_short[1])
    targetvalue_short_1 := close[since_entry_short] - close[since_entry_short]*(percent_based/100)*r_ratio
else
    price_stop_short := 1000000000.0

// Executing trades
if ema_buy_condition == true 
    strategy.entry('Long', strategy.long, qty = 1000, when = strategy.position_size <= 0)

if ema_sell_condition == true 
    strategy.entry('Short',strategy.short,qty = 1000, when = strategy.position_size >= 0)


// Stop loss and target price trading logics
strategy.exit('Long Exit', from_entry = 'Long', limit = targetvalue_long_1, stop = price_stop_long, when = strategy.position_size > 0)
strategy.exit('Short Exit', from_entry = 'Short', limit = targetvalue_short_1, stop = price_stop_short, when = strategy.position_size < 0)


// Plots
P1 = plot(price_stop_long > 0 ? price_stop_long : na, "SL long", color = color.purple, style=plot.style_linebr)
P2 = plot(price_stop_long > 0 ? targetvalue_long_1 : na, "Traget long", color = color.aqua, style=plot.style_linebr)

P3 = plot(price_stop_short < 1000000000.0 ? price_stop_short : na, "SL Short", color = color.purple, style=plot.style_linebr)
P4 = plot(price_stop_short < 1000000000.0 ? targetvalue_short_1 : na, "Traget Short", color = color.aqua, style=plot.style_linebr)



// plot(close)