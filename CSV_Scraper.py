fileInput = 'C:/test_data.csv'
myFile = open(fileInput, 'r')

newDict = {}
newSortDict = {}
x = 0

for line in myFile:
    values = line.split(',')
    userName = values[0]
    if 'MB' in values[6]:
        print("Small data usage")
    else:
        overage = float(values[6].replace(' GB', ''))
    newDict.update({overage:userName})

sortedDict = sorted(newDict, reverse=True)
while x < len(sortedDict):
    newSortDict.update({sortedDict[x]: None})
    x += 1
newSortDict.update(newDict)

for key in newSortDict.keys():
    print(newSortDict[key], "used ", key, "GB of data over their limit.")


