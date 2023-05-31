import http.client
import urllib.parse
import json
import base64
from dotenv import dotenv_values

def post_new_data(id, Reading, ReadDate):
    # Prepare the request data
    post_data = {
        "UnitId": "-1",
        "UnitNumber": id,
        "MeterType": "ODOMETER",
        "MeterReading": Reading,
        "MeterDate": ReadDate
    }
    post_data = json.dumps(post_data)
    POST_URL = '/AMSApp/Integration/Mobile/MeterReading'
    host = 'trc.tmwcloud.com'
    port = 443
    
    # Prepare the request headers
    username = dotenv_values('.env')['TMW_USERNAME']
    password = dotenv_values('.env')['TMW_PASSWORD']
    headers = {
        'Authorization': 'Basic ' + base64.b64encode((username + ':' + password).encode()).decode(),
        'Content-Type': 'application/json'
    }
    
    # Make the HTTP connection
    conn = http.client.HTTPSConnection(host, port)
    
    # Send the POST request
    conn.request("POST", POST_URL, body=post_data, headers=headers)
    
    # Get the response
    response = conn.getresponse()
    status_code = response.status
    
    # Read and parse the response data
    response_data = response.read().decode("utf-8")
    response_json = json.loads(response_data)
    
    # Close the connection
    conn.close()
    
    return status_code, response_json