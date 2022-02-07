import requests
import json
import os
from dotenv import load_dotenv

# Load environment variable
load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")
refresh_token = os.getenv("REFRESH_TOKEN")
api_endpoint = os.getenv("API_ENDPOINT")
company_id = os.getenv("COMPANY_ID")

header_token = {'Authorization': 'Bearer ' + access_token}


def c_outputter(jsonr):
    outtxt = (json.dumps(jsonr.json(), indent=2))
    print(outtxt)


def f_outputter(jsonr):
    file = open("vendor.json", "w")
    file.write(jsonr.text)
    file.close()


# Call Procore Get Vendor API
ur = api_endpoint + company_id
response = requests.get(ur, headers=header_token)
if response.status_code == 401:
    ':except'

else:
    print(response.status_code)

# Output to file.
f_outputter(response)

# Output to the console.
c_outputter(response)
