import sys
import json

values = sys.argv[1]
tests = sys.argv[2]
report = sys.argv[3]

f = open(values, 'r')
valuesData = json.load(f)
f.close()

valDict = {}
for v in valuesData["values"]:
    valDict[v["id"]] = v["value"]

f = open(tests, 'r')
testsData = json.load(f)
f.close()

def rec(obj):
    if type(obj) == dict:
        if "id" in obj and obj["id"] in valDict:
            obj["value"] = valDict[obj["id"]]
        for k in obj:
            rec(obj[k])
    elif type(obj) == list:
        for i in obj:
            rec(i)

rec(testsData)

f = open(report, 'w')
json.dump(testsData, f, indent=2)
f.close()