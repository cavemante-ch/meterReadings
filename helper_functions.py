import requests
import json

def handle_pagination(URL, headers):
    all_data = []  # Store all the data from all pages

    params = {
            'types': "obdOdometerMeters,gpsOdometerMeters",
            'after': ''
    }

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

    return all_data

def clean_samsara_data(data):
    return_data = []
    template = {
                "id": "",
                "name": "",
                "externalIds": {
                    "samsara.serial": "",
                    "samsara.vin": ""
                },
                "obdOdometerMeters": {
                    "time": "",
                    "value": 0
                },
                "gpsOdometerMeters": {
                    "time": "",
                    "value": 0
                }
            }
    for dictionary in data:
        for key, value in template.items():
            if key not in dictionary:
                dictionary[key] = value
            elif isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    if sub_key not in dictionary[key]:
                        dictionary[key][sub_key] = sub_value
    with open('samsara_raw.json', 'w') as f:
            json.dump(data, f, indent=4)

    for truck in data: 
        return_data.append({
            'id': truck['id'],
            'name': truck['name'],
            'samsara.serial': truck['externalIds']['samsara.serial'],
            'samsara.vin': truck['externalIds']['samsara.vin'],
            'obd_time': truck["obdOdometerMeters"]["time"],
            'obd_value': int(truck["obdOdometerMeters"]["value"]*0.000621371192),
            'gps_time': truck["gpsOdometerMeters"]["time"],
            'gps_value': int(truck["gpsOdometerMeters"]["value"]*0.000621371192)
        })

    return return_data

