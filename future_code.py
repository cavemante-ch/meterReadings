import json

with open('test.json', 'r') as f:
    a = json.load(f)

with open('samsara_data.json', 'r') as f:
    b = json.load(f)

for i in a:
    found = False
    for j in b:
        if i["SerialNo"] == j["samsara.vin"]:
            found = True
            break
    if not found:
        print('ERRORRRRRR at ' + i['SerialNo'])