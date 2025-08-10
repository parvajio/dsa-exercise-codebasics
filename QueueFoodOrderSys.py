import time
import threading
from collections import deque
d = deque()

orders = ['pizza','samosa','pasta','biryani','burger']

def placeOrder(orders):
    for order in orders:
        d.appendleft(order)
        print(f"Placed order: {order}")
        time.sleep(0.5)

def serveOrder():
    time.sleep(1)
    while len(d):
        print(f"Served order: {d.pop()}")
        time.sleep(2)

t1 = threading.Thread(target=placeOrder, args=(orders,))
t2 = threading.Thread(target=serveOrder)

t1.start()
t2.start()

t1.join()
t2.join()

