from binance.enums import *
from bot.client import get_client

def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    if order_type == "MARKET":
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity
        )

    elif order_type == "LIMIT":
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )