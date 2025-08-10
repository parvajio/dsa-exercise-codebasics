str = "We will conquere COVID-19"

words  =str.split(" ")
from collections import deque
s = deque()

for word in words:
    s.append(word)

rstr = "" 
while len(s) != 0:
    rstr += s.pop() + " "

print(rstr)

