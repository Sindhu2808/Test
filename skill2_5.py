import json
with open('attendance.json','r') as jsonfile:
    jsontxt = jsonfile.read()
dicttype = json.loads(jsontxt)
print(dicttype)