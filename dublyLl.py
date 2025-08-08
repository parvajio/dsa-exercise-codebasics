class Node:
    def __init__(self, data = None, next = None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev

class DubbleLL:
    def __init__(self):
        self.head = None
        self.tell = None

    def inser_at_begining(self, data):
        if self.head == None and self.tell == None:
            node = Node(data, self.head, )
            self.head = node
    