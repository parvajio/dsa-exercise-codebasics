# queue = []

# queue.insert(0, 1)
# queue.insert(0, 2)
# queue.insert(0, 3)
# queue.insert(0, 4)

# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())

from collections import deque
d  = deque()

d.appendleft(1)
d.appendleft(2)
d.appendleft(3)
d.appendleft(4)

print(d.pop())
print(d.pop())
print(d.pop())

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def isEmpty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

q = Queue()

q.enqueue({
    "company" : "Wall Mart",
    "time_stamps" : "10 apr, 11.01 AM",
    "price" : 131.02
})
q.enqueue({
    "company" : "Wall Mart",
    "time_stamps" : "10 apr, 11.02 AM",
    "price" : 132.32
})
q.enqueue({
    "company" : "Wall Mart",
    "time_stamps" : "10 apr, 11.03 AM",
    "price" : 136.92
})

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
