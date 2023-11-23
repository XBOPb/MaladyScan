import json
import requests

file_path = r''
api_key = ''
params = dict(apikey=api_key)

def check_file(file_path):
    scan_url = 'https://virustotal.com/vtapi/v2/file/scan'
    with open(file_path, 'rb') as file:
        files = dict(file=(file_path, file))
        response = requests.post(scan_url, files=files, params=params)
        print(response)
    if response.status_code == 200:
        result = response.json()
        json_result = json.dumps(result, sort_keys=False, indent=4)
        json_dict = json.loads(json_result)
        scan_id = json_dict.get('scan_id')
        return scan_id
    else: 
        return response.status_code
    
def file_check_result(scan_id):
    report_url = 'https://virustotal.com/vtapi/v2/file/report'
    params = dict(apikey=api_key, resource=scan_id)
    response = requests.get(report_url, params=params)
    if response.status_code == 200:
        result = response.json()
        print(json.dumps(result, sort_keys=False, indent=4))


def check_link(link):
    scan_url = 'https://virustotal.com/vtapi/v2/url/scan'
    params = dict(apikey=api_key, url=link)
    response = requests.post(scan_url, data=params)
    if response.status_code == 200:
        result = response.json()
        json_result = json.dumps(result, sort_keys=False, indent=4)
        json_dict = json.loads(json_result)
        scan_id = json_dict.get('scan_id')
        return scan_id


def link_check_result(scan_id):
    report_url = 'https://virustotal.com/vtapi/v2/file/report'
    params = dict(apikey=api_key, resource=scan_id)
    response = requests.get(report_url, params=params)
    if response.status_code == 200:
        result = response.json()
        print(json.dumps(result, sort_keys=False, indent=4))

def scan_ip_address():
    report_url = 'https://virustotal.com/vtapi/v2/ip-address/report'
    params = dict(apikey=api_key, domain='google.com')
    response = requests.get(report_url, params=params)
    if response.status_code == 200:
        result = response.json()
        print(json.dumps(result, sort_keys=False, indent=4))
        

