import threading
import random
import time
from code import addOrder, matchOrder

def random_order_generator():
    """
    test the addOrder function by generating random orders.
    """
    while True:
        order_type = random.choice(['Buy', 'Sell'])
        ticker = random.randint(0, 3)
        quantity = random.randint(1, 100)
        price = round(random.uniform(10, 500), 2)
        addOrder(order_type, ticker, quantity, price)
        time.sleep(random.uniform(0.01, 0.1))

def match_order_loop():
    """
    use the matchOrder function to match the orders.
    """
    while True:
        matchOrder()
        time.sleep(0.05)

def main():
    # begin the random_order_generator and match_order_loop
    generator_thread = threading.Thread(target=random_order_generator, daemon=True)
    matcher_thread = threading.Thread(target=match_order_loop, daemon=True)
    generator_thread.start()
    matcher_thread.start()
    # run test for 5 seconds
    time.sleep(5)

if __name__ == "__main__":
    main()
