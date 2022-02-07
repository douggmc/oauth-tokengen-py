from urllib import response

import requests
import json
import os
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

g_response = ''
g_ur = ''


def c_outputer(jsonr):
    outtxt = (json.dumps(jsonr.json(), indent=2))
    print(outtxt)


def f_outputer(jsonr):
    file = open("vendor.json", "w")
    file.write(jsonr.text)
    file.close()


def get_new_token():
    l_ur = oauth_base_endpoint + api_refresh_token + '&client_id=' + client_id + '&client_secret=' + client_secret + '&refresh_token=' + refresh_token + '&redirect_uri=' + redirect_uri
    l_response = requests.post(l_ur, headers=header_token)
    if l_response.status_code == 200:
        os.environ['REFRESH_TOKEN'] = refresh_token
        os.environ['ACCESS_TOKEN'] = access_token


def get_vendor():
    g_ur = base_endpoint + api_vendor + company_id
    g_response = requests.get(ur, headers=header_token)
    return response.status_code


# Call Procore Get Vendor APIs
def main():
    if get_vendor() == 401:
        get_new_token()
    else:
        print(get_vendor())
        # Output to file.
        f_outputer(response)

        # Output to the console.
        c_outputer(response)


if __name__ == "__main__":
    main()
