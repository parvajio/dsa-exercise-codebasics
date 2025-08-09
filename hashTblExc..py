import csv

tempArr = []
with open("nyc_weather.csv", 'r') as file:
    content = csv.reader(file)
    for line in content:
        try:
            temperature = int(line[1])
            tempArr.append(temperature)
        except:
            print("invalid")

avg = sum(tempArr[0:7])/len(tempArr[0:7])
print(avg)

print(max(tempArr[0:10]))
