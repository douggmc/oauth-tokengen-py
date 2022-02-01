import requests
import json

company_id = '32616'
api_base_endpoint = 'https://sandbox.procore.com/rest/v1.0/vendors?company_id='
api_token = 'eyJhbGciOiJFUzUxMiJ9.eyJhaWQiOiIxMGE5MjFkNjRhZDNlYTliNTAwMDE4MzgzZDZhNDY0YTczODIyNzU0N2E0NTE0NWRlYTA2NGRjN2IwNjI3NGQ3IiwiYW91aWQiOm51bGwsImFvdXVpZCI6bnVsbCwiZXhwIjoxNjQzNzY0MzQzLCJ1aWQiOjgzMDY3LCJ1dWlkIjoiYmZmMzkxMmUtNTg3Mi00MmJjLThiZjQtMGIyY2E4MjQwZTQwIn0.AA-Lj2ctNSy66y-C_TeVkzkoSAzSRwEw77vIskf9-_uQvkaWtzIegf19uhpNsPNHyRjrBzr_RMtLzmBQe_mYvrdHAQ37xcs7tC1NLiIbO0onpe7KZAMtKXiD8I0cUsSZII6r0blbsPg13ZSo6kM2iPySz2Lvuy3zijpseXD2TVzPODNm'
header_token = {'Authorization': 'Bearer ' + api_token}


def c_outputter(jsonr):
    outtxt = (json.dumps(jsonr.json(), indent=2))
    print(outtxt)


def f_outputter(jsonr):
    file = open("vendor.json", "w")
    file.write(jsonr.text)
    file.close()


# Call Procore Get Vendor API
ur = api_base_endpoint + company_id
response = requests.get(ur, headers=header_token)

# Output to file.
f_outputter(response)

# Output to the console.
c_outputter(response)
