import requests
from app.utils.get_env import *

BASE_HEADERS = {
    'Authorization': f'Bearer {CLERK_SECRET_KEY}'
}


def make_request(url, headers, requests_form="get", params=None, files=None, data=None):    
    print("Making request to ", url)
    try:
        if requests_form == "get":
            # Make a GET request to the API
            response = requests.get(url, headers=headers, params=params, data=data)
        elif requests_form == "post":
            # print("POSTT", data)
            # Make a POST request to the API
            response = requests.post(url, headers=headers, params=params, files=files, data=data)
        elif requests_form == "put":
            # Make a PUT request to the API
            response = requests.put(url, headers=headers, params=params, data=data)
        
        # print(response.json())

    except Exception as e:
        response = None
        # print("Error occurred while making request: ", e)
        return {'error': 'Error occurred while making request: ' + str(e)}


    return response.json()
