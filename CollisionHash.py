class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [[] for i in range(self.Max)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, val):
        h = self.getHash(key)
        found = False

        for idx, elm in enumerate(self.arr[h]):
            if len(elm) == 2 and elm[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.getHash(key)
        
        for elm in self.arr[h]:
            if elm[0] == key:
                return elm[1] 

    def __delitem__(self, key):
        h= self.getHash(key)
        for idx, elm in enumerate(self.arr[h]):
            if elm[0] == key:
                del self.arr[h][idx]

h = HashTable()
h["parvaj"] = 22
h["nahid"] = 221
h["rajib"] = "22"
print(h["parvaj"])
del h["parvaj"]
print(h["parvaj"])
# print(h.arr)