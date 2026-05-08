import sys
import json
import os

if len(sys.argv) != 4:
    print("Использование: python task3.py <file> <file> <file>")
    sys.exit(1)

values = sys.argv[1]
tests = sys.argv[2]
report = sys.argv[3]

if os.path.getsize(values) == 0:
    print("Файл пуст")
    sys.exit(1)
    
if os.path.getsize(tests) == 0:
    print("Файл пуст")
    sys.exit(1)

try:
    f = open(values, 'r')
    valuesData = json.load(f)
    f.close()
    
except FileNotFoundError:
    print("Файл не найден")
    sys.exit(1)
except json.JSONDecodeError:
    print("Файл должен содержать валидный JSON")
    sys.exit(1)
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
    sys.exit(1)

valDict = {}
for v in valuesData["values"]:
    valDict[v["id"]] = v["value"]


try:
    f = open(tests, 'r')
    testsData = json.load(f)
    f.close()
except FileNotFoundError:
    print("Файл не найден")
    sys.exit(1)
except json.JSONDecodeError:
    print("Файл должен содержать валидный JSON")
    sys.exit(1)
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
    sys.exit(1)
    
    
def rec(obj):
    if type(obj) == dict:
        if "id" in obj and obj["id"] in valDict:
            obj["value"] = valDict[obj["id"]]
        for k in obj:
            rec(obj[k])
    elif type(obj) == list:
        for i in obj:
            rec(i)

try:
    rec(testsData)
except Exception as e:
    print(f"Произошла непредвиденная ошибка при обработке: {e}")
    sys.exit(1)
    
try:    
    f = open(report, 'w')
    json.dump(testsData, f, indent=2)
    f.close()
    
except Exception as e:
    print(f"Произошла непредвиденная ошибка при записи данных в файл: {e}")
    sys.exit(1)