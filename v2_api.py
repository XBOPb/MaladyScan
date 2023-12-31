import json
import requests


def check_file(api_key, file_path):
    scan_url = 'https://virustotal.com/vtapi/v2/file/scan'
    params = dict(apikey=api_key)

    with open(file_path, 'rb') as file:
        files = dict(file=(file_path, file))
        response = requests.post(scan_url, files=files, params=params)
    if response.status_code == 200:
        result = response.json()
        json_result = json.dumps(result, sort_keys=False, indent=4)
        json_dict = json.loads(json_result)
        scan_id = json_dict.get('scan_id')
        return scan_id
    else: 
        return response.status_code
    
def file_check_result(api_key, scan_id):
    report_url = 'https://virustotal.com/vtapi/v2/file/report'
    params = dict(apikey=api_key, resource=scan_id)
    response = requests.get(report_url, params=params)
    if not response.status_code == 200:
        return 'Unable to complete file scan.'
    result = response.json()
    result = json.dumps(result, sort_keys=False, indent=4)
    return result


def check_link(api_key, link):
    scan_url = 'https://virustotal.com/vtapi/v2/url/scan'
    params = dict(apikey=api_key, url=link)
    response = requests.post(scan_url, data=params)
    if response.status_code == 200:
        result = response.json()
        json_result = json.dumps(result, sort_keys=False, indent=4)
        json_dict = json.loads(json_result)
        scan_id = json_dict.get('scan_id')
        return scan_id


def link_check_result(api_key, scan_id):
    report_url = 'https://virustotal.com/vtapi/v2/file/report'
    params = dict(apikey=api_key, resource=scan_id)
    response = requests.get(report_url, params=params)
    if response.status_code == 200:
        result = response.json()
        return json.dumps(result, sort_keys=False, indent=4)

def scan_ip_address(api_key, ip_address):
    report_url = 'https://virustotal.com/vtapi/v2/ip-address/report'
    params = dict(apikey=api_key, domain=ip_address)
    response = requests.get(report_url, params=params)
    if response.status_code == 200:
        result = response.json()
        return json.dumps(result, sort_keys=False, indent=4)
        

