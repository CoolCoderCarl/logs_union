import json

def createSortedFile(pathToFirstLog, pathToSecondLog, pathToResultLog):
    with open(pathToFirstLog) as fl:
        log1 = fl.read()

    with open(pathToSecondLog) as sl:
        log2 = sl.read()

    unionData = log1 + log2

    # print(unionData)
    # print(type(unionData))

    unionList = [json.loads(jline) for jline in unionData.splitlines()]
    # print(unionList)
    # print(type(unionList))
    # print(result[0])
    # listElem = result[0]
    # print(type(listElem))

    sortedList = sorted(unionList, key=lambda k: k['timestamp'])
    # print(sortedList)
    # print(type(sortedList))

    with open(pathToResultLog, 'w') as outfile:
        for entry in sortedList:
            json.dump(entry, outfile)
            outfile.write('\n')

    outfile.close()