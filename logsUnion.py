import json

def createSortedFile(pathToFirstLog, pathToSecondLog, pathToResultLog):
    with open(pathToFirstLog) as fl:
        log1 = fl.read()

    with open(pathToSecondLog) as sl:
        log2 = sl.read()

    unionData = log1 + log2

    unionList = [json.loads(jline) for jline in unionData.splitlines()]

    sortedList = sorted(unionList, key=lambda k: k['timestamp'])

    with open(pathToResultLog, 'w') as outfile:
        for entry in sortedList:
            json.dump(entry, outfile)
            outfile.write('\n')

    outfile.close()