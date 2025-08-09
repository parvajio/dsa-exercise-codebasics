from collections import deque

# stack = deque()

# stack.append("hello")
# stack.append("hi")
# stack.append("wssap")

# print(stack)
# print   (stack.pop())
# print(stack)

class Stack:
    def __init__(self):
        self.stk = deque()
    
    def push(self, val):
        self.stk.append(val)

    def pop(self):
        return self.stk.pop()
    
    def peek(self):
        return self.stk[-1]
    
    def isEmpty(self):
        return len(self.stk) == 0

    def size(self):
        return len(self.stk)
    
    def print(self):
        print(self.stk)

s = Stack()
s.push(5)
s.push(22)
s.push(6)
s.print()
print(s.size())