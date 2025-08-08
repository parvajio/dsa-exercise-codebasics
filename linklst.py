class Node:
    def __init__(self, data=None, next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

# insert at begining 

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

# print 
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
    
# insert at the end 
    def inser_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

# insert multiple values 
    def insert_values(self, dataList):
        # self.head = None
        # for data in dataList:
        #     if self.head is None:
        #         self.head = Node(data, None)
            
        #     else:
        #         itr = self.head
        #         while itr.next:
        #             itr = itr.next

        #         itr.next = Node(data, None)
        self.head = None
        for data in dataList:
            self.inser_at_end(data)

# get length 
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

# remove index     
    def remove_idx(self, idx):
        if idx < 0 or idx >= self.get_length():
            raise Exception("Invalid Index")
        
        if idx == 0:
            self.head = self.head.next
            return

        count_idx = 0
        itr = self.head
        while itr:
            if count_idx == idx-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count_idx += 1

# insert at index 
    def insert_at(self, idx, data):
        if idx < 0 or idx >= self.get_length():
            raise Exception("Invalid index")
        
        if idx == 0:
            node = Node(data, self.head)
            self.head = node
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itrN = itr.next
                itr.next = Node(data, itrN)
                return
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
            itr = itr.next

li = LinkedList()
# li.insert_at_begining(10)
# li.insert_at_begining(2)
# li.print()
# li.inser_at_end(33)
# li.inser_at_end(5)
# li.inser_at_end(2222)
li.insert_values(["parvaj","niloy", "rajib", "rajon"])
li.remove_idx(2)
li.insert_at(0, "rafi")
li.print()
print("Length : ", li.get_length())
li.insert_after_value("rafi", "shakib")
li.print()