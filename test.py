from samsara import SamsaraApi
from tmw import TmwApi

samsara_client = SamsaraApi()
tmw_client = TmwApi()

print(tmw_client.get_meter_reading('4V4MC9EG7GN963062', 'GPSODOMETER'))