class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, val):
        h = self.getHash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.getHash(key)
        print(self.arr[h])

    def __delitem__(self, key):
        h= self.getHash(key)
        self.arr[h] = None

h = HashTable()
h["parvaj"] = 22
h["nahid"] = 221
h["rajib"] = "22"

del h["parvaj"]
h["parvaj"]
print(h.arr)