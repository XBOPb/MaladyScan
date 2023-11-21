import json
import requests

file_path = ''
api_url = 'https://virustotal.com/vtapi/v2/file/scan'
api_key = ''
params = dict(apikey=api_key)
with open(file_path, 'rb') as file:
    files = dict(file=(file_path, file))
    response = requests.post(api_url, files=files, params=params)
if response.status_code == 200:
    result = response.json()
    print(json.dumps(result, sort_keys=False, indent=4))