# import the Order class from order.py
from order import Order



sell_orders = [[] for _ in range(1024)]
buy_orders = [[] for _ in range(1024)]




def addOrder(order_type, ticker, quantity, price):
    """
    the frist function: addOrder
    add order to the sell and buy list, including buy and sell orders
    """
    order = Order(order_type, ticker, quantity, price)
    if order_type == 'Buy':
        buy_orders[ticker].append(order)
    elif order_type == 'Sell':
        sell_orders[ticker].append(order)
    print(f"Added {order}")


def matchOrder():
    """
    the second function: matchOrder
    search the lowest price in the sell orders and match it with the buy orders
    """
    for ticker in range(1024):
        buy_order = buy_orders[ticker]
        sell_order = sell_orders[ticker]
        if not buy_order or not sell_order:
            continue

        # search the lowest price in the sell orders, O(n)
        lowest_sell = min(sell_order, key=lambda order: order.price)

        # find the buy orders that can match the lowest sell order
        for buy in buy_order:
            if buy.price >= lowest_sell.price:
                traded_quantity = min(buy.quantity, lowest_sell.quantity)
                print(f"Matched: {buy} and {lowest_sell}, traded quantity: {traded_quantity}")
                # update the quantity of buy and sell orders
                buy.quantity -= traded_quantity
                lowest_sell.quantity -= traded_quantity
                # update the buy orders list and sell orders list
                break  

        sell_orders[ticker] =list(filter(lambda order: order.quantity > 0, sell_order))
        buy_orders[ticker] = list(filter(lambda order: order.quantity > 0, buy_order))


