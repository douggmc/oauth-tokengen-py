import json
import os

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
access_token = os.getenv('ACCESS_TOKEN')
refresh_token = os.getenv('REFRESH_TOKEN')
base_endpoint = os.getenv('BASE_ENDPOINT')
oauth_base_endpoint = os.getenv('OAUTH_BASE_ENDPOINT')
api_vendor = os.getenv('API_VENDOR')
company_id = os.getenv('COMPANY_ID')
api_refresh_token = os.getenv('API_REFRESH_TOKEN')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')

header_token = {'Authorization': 'Bearer ' + access_token}


def c_outputer(jsonr):
    outtxt = (json.dumps(jsonr.json(), indent=2))
    print(outtxt)


def f_outputer(jsonr):
    file = open("vendor.json", "w")
    file.write(jsonr.text)
    file.close()


def get_new_token():
    t_ur = oauth_base_endpoint + api_refresh_token + '&client_id=' + client_id + '&client_secret=' + client_secret + '&refresh_token=' + refresh_token + '&redirect_uri=' + redirect_uri
    t_response = requests.post(t_ur, headers=header_token)
    if t_response.status_code == 200:
        jdata = t_response.json()
        os.environ['REFRESH_TOKEN'] = jdata.refresh_token
        os.environ['ACCESS_TOKEN'] = jdata.refresh_token


def get_vendor():
    ur = base_endpoint + api_vendor + company_id
    v_response = requests.get(ur, headers=header_token)
    return v_response


# Call Procore Get Vendor APIs
def main():
    v_response = get_vendor()
    if v_response.status_code == 401:
        # Token has expired, get new token
        get_new_token()
        v_response = get_vendor()
    else:
        # Output to file.
        f_outputer(v_response)

        # Output to the console.
        c_outputer(v_response)


if __name__ == "__main__":
    main()
