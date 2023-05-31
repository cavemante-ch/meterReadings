#!/usr/bin/env python3
from samsara import SamsaraApi
from tmw import TmwApi
import json
import sys
import datetime
from posttest import post_new_data

samsara_client = SamsaraApi()
tmw_client = TmwApi()

samsara_data = samsara_client.get_all_truck_data()
tmw_data = tmw_client.get_active_tractors()
meter_data = []

for tmw_unit in tmw_data:
    for samsara_unit in samsara_data:
        if tmw_unit["SerialNo"] == samsara_unit["samsara.vin"]:
            if samsara_unit["obd_value"]:
                meter_type = "OBDODOMETER"
                time = samsara_unit['obd_time']
                val = samsara_unit['obd_value']
            else:
                meter_type = "GPSODOMETER"
                time = samsara_unit['gps_time']
                val = samsara_unit['gps_value']
            
            meter_data.append({
                "UnitNumber": tmw_unit['UnitNumber'],
                "MeterType": meter_type,
                "ReadDate": time,
                "Reading": val
            })

with open('test.json', 'w') as f:
    json.dump(meter_data, f, indent=4)

for meter_reading in meter_data:
    print(f'posting: {meter_reading["UnitNumber"]}')
    a = post_new_data(meter_reading["UnitNumber"], meter_reading["Reading"], meter_reading["ReadDate"])
    if a[0] == 500:
        with open('output.log', 'a') as f:
            f.write(f'TMW POST 500 ERROR: {a[1]} \n')
        sys.exit()

with open('output.log', 'a') as f:
    f.write(f'SUCCESFUL UPDATE AT {datetime.datetime.now()}')
