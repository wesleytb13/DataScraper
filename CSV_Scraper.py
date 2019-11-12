fileInput = 'C:/test_data.csv'
myFile = open(fileInput, 'r')

newDict = {}
newSortDict = {}
x = 0
i = 0
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

while i < 11:
    print('{0:<25s}{1:<4s}{2:>7,.3f}{3:<25s}'.format([value for value in newSortDict.values()][i], 'used', [key for key in newSortDict.keys()][i], 'GB over their data limit.'))
    i += 1
