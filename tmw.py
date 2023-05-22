from dotenv import dotenv_values
import json
import requests
import base64

class TmwApi:

    def __init__(self):
        self.BASE_URL = 'https://trc.tmwcloud.com/AMSApp/Integration/System/Unit'
        self.username = dotenv_values('.env')['TMW_USERNAME']
        self.password = dotenv_values('.env')['TMW_PASSWORD']
        self.headers = {
        'Authorization': 'Basic ' + base64.b64encode((self.username + ':' + self.password).encode()).decode(),
        'Content-Type': 'application/json'
        }

    def get_active_tractors(self):
        res = requests.get(self.BASE_URL, headers=self.headers)
        list = []

        for unit in res.json()['Units']:
            if unit['Status'] == "ACTIVE" and unit['Type'] == 'TRACTOR':
                data = {
                    'UnitNumber': unit["UnitNumber"],
                    'SerialNo': unit['SerialNo']
                }
                list.append(data)

        with open('test.json', 'w') as f:
            json.dump(list, f, indent=4)
        return list


a = TmwApi()
ids = a.get_active_tractors()
