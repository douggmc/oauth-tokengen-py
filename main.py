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

header_token = {'Authorization': 'Bearer ' + access_token}


def c_outputer(jsonr):
    outtxt = (json.dumps(jsonr.json(), indent=2))
    print(outtxt)


def f_outputer(jsonr):
    file = open("vendor.json", "w")
    file.write(jsonr.text)
    file.close()


def get_new_token():
    l_ur = oauth_base_endpoint + api_refresh_token
    print('x')


# Call Procore Get Vendor APIs
def main():
    ur = base_endpoint + api_vendor + company_id
    response = requests.get(ur, headers=header_token)
    if response.status_code == 401:
        get_new_token()
    else:
        print(response.status_code)

    # Output to file.
    f_outputer(response)

    # Output to the console.
    c_outputer(response)


if __name__ == "__main__":
    main()
