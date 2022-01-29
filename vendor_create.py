import requests
import json

company_id = '32616'
api_base_endpoint = 'https://sandbox.procore.com/rest/v1.0/vendors?company_id='
api_token = 'eyJhbGciOiJFUzUxMiJ9.eyJhaWQiOiIxMGE5MjFkNjRhZDNlYTliNTAwMDE4MzgzZDZhNDY0YTczODIyNzU0N2E0NTE0NWRlYTA2NGRjN2IwNjI3NGQ3IiwiYW91aWQiOm51bGwsImFvdXVpZCI6bnVsbCwiZXhwIjoxNjQzNDA4OTEwLCJ1aWQiOjgzMDY3LCJ1dWlkIjoiYmZmMzkxMmUtNTg3Mi00MmJjLThiZjQtMGIyY2E4MjQwZTQwIn0.ACntLbp4jbEq7mdZLX-oW-5NkK8oW9k96aILJutJ9ChQg_ovEyCbULOAwuryjolwTVKm5n93-BbAK7t1bf0vpIn-AW8M2_qn7bZbFUOqdG9JXGSLAA5bRAbj7OwDMGa4IzEycVbbUF46MrA43sHskSc_T4Ccx2HK6IAWPoRDEHuWbAhN'
header_token = {'Authorization': 'Bearer ' + api_token}


def c_outputter(jsonr):
    outtxt = (json.dumps(jsonr.json(), indent=2))
    print(outtxt)


def f_outputter(jsonr):
    file = open("vendor.json", "w")
    file.write(jsonr.text)
    file.close()


#z Call Procore Get Vendor API
ur = api_base_endpoint + company_id
response = requests.get(ur, headers=header_token)

# Output to file.
f_outputter(response)

# Output to the console.
c_outputter(response)
