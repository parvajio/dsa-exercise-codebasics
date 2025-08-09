import csv

# avg and max 

tempArr = []
temDic = {}
with open("nyc_weather.csv", 'r') as file:
    content = csv.reader(file)
    for line in content:
        try:
            temperature = int(line[1])
            tempArr.append(temperature)
            temDic[line[0]] = line[1]
        except:
            print("invalid")

avg = sum(tempArr[0:7])/len(tempArr[0:7])
print(avg)

print(max(tempArr[0:10]))

print(temDic["Jan 4"])
print(temDic["Jan 9"])

# poem 
wordCount = {}

with open("poem.txt", 'r') as file:
    for line in file:
        tokens = line.split(" ")

        for token in tokens:
            token = token.replace("\n", "")
            if token in wordCount:
                wordCount[token] += 1
            else:
                wordCount[token] = 1
        
print(wordCount)

class HashTable: 
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10 
    
    def __setitem__(self, key, val):
        h = self.getHash(key)

        found = False
        for idx, elm in enumerate(self.arr[h]):
            if elm[0] == key:
                self.arr[h][idx] = (key, val)
                found = True

        if not found:
            self.arr[h].append((key, val))

ht = HashTable()
ht["Jan 1"] = 27
ht["Jan 2"] = 31
ht["Jan 3"] = 23
ht["Jan 4"] = 34
ht["Jan 5"] = 37
ht["Jan 6"] = 38
ht["Jan 7"] = 29
ht["Jan 8"] = 30
ht["Jan 9"] = 35
ht["Jan 10"] = 30
print(ht.arr)