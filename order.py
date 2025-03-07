
class Order:
    def __init__(self, order_type, ticker, quantity, price):
        self.order_type = order_type  # 'Buy' or 'Sell'
        self.ticker = ticker          
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"Order({self.order_type}, {self.ticker}, {self.quantity}, {self.price})"
