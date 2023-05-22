from dotenv import dotenv_values
from helper_functions import handle_pagination, clean_samsara_data
import json
import requests

class SamsaraApi:

    def __init__(self):
        self.BASE_URL = "https://api.samsara.com/fleet/vehicles/stats"
        self.GET_VEHICLE_URL = "https://api.samsara.com/fleet/vehicles/"
        self.API_TOKEN = dotenv_values('.env')['SAMSARA_API_TOKEN']
        self.headers = {
            "Authorization": self.API_TOKEN,
            "Content-type": "application/json"
        }

    def get_all_truck_data(self):

        all_data = handle_pagination(self.BASE_URL, self.headers)
        formatted_data = all_data

        with open('test.json', 'w') as f:
            json.dump(formatted_data, f, indent=4)

    def get_single_truck(self, vehicleId):
        res = requests.get(self.BASE_URL + vehicleId, headers=self.headers)

        print(res.json())

    def get_all_ids(self):
        with open('samsara_data.json', 'r') as f:
            data = json.load(f)

        ids = []
        for i in data:
            ids.append(i['id'])

        return ids

a = SamsaraApi()
a.get_single_truck("1M1AW07Y8GM078351")
