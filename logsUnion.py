import json

# UNION FILES
data1 = data2 = ""

# Reading data from log1
# Path to dir1
with open('PATH_TO_DIR1') as fp:
    data1 = fp.read()

# Reading data from log2
# Path to dir2
with open('PATH_TO_DIR2') as fp:
    data2 = fp.read()

unionData = data1 + data2

# print(unionData)
# print(type(unionData))

result = [json.loads(jline) for jline in unionData.splitlines()]
print(result)
print(type(result))
# print(result[0])
# listElem = result[0]
# print(type(listElem))

newList = sorted(result, key=lambda k: k['timestamp'])
print(newList)
print(type(newList))

# SAVE TO NEW FILE
# Path to result file
with open('result.jsonl', 'w') as outfile:
    for entry in newList:
        json.dump(entry, outfile)
        outfile.write('\n')

outfile.close()