class Node:
    def __init__(self, data=None, next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Your linked list is empty.")
            return
        
        itr = self.head
        listr = ''
        while itr: 
            listr += str(itr.data) + "-->"
            itr = itr.next
        print(listr)
    
    def inser_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, dataList):
        self.head = None
        for data in dataList:
            if self.head is None:
                self.head = Node(data, None)
            
            else:
                itr = self.head
                while itr.next:
                    itr = itr.next

                itr.next = Node(data, None)

li = LinkedList()
# li.insert_at_begining(10)
# li.insert_at_begining(2)
# li.print()
# li.inser_at_end(33)
# li.inser_at_end(5)
# li.inser_at_end(2222)
li.insert_values([2,3,66,7])
li.print()