import os
from dotenv import dotenv_values

import requests
import json

class SamsaraApi:

    def __init__(self):
        self.BASE_URL = "https://api.samsara.com/fleet/vehicles/stats"
        self.API_TOKEN = dotenv_values('.env')['SAMSARA_API_TOKEN']

a= SamsaraApi()
print(a.API_TOKEN)







'''
token = "Bearer samsara_api_kvh6u7n9BRRwtS3s2gqIdpigYX6LuK"
URL = "https://api.samsara.com/fleet/vehicles/stats"

headers = {
    "Authorization": token,
    "Content-type": "application/json"
}

params = {
    'types': "obdOdometerMeters",
    'after': ''
}

all_data = []  # Store all the data from all pages

while True:
    res = requests.get(URL, headers=headers, params=params)
    res_data = res.json()
    print(params['after'])
    print(res_data['pagination']['hasNextPage'])

    all_data.extend(res_data['data'])

    if not res_data['pagination']['hasNextPage']:
        break

    # Update the endCursor parameter for the next page
    params['after'] = res_data['pagination']['endCursor']

with open('test.json', 'w') as f:
    json.dump(all_data, f, indent=4)

print("All data retrieved and saved to test.json")
'''