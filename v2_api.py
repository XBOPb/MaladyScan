import json
import requests

file_path = r''
api_key = ''
params = dict(apikey=api_key)

def check_file():
    scan_url = 'https://virustotal.com/vtapi/v2/file/scan'
    with open(file_path, 'rb') as file:
        files = dict(file=(file_path, file))
        response = requests.post(scan_url, files=files, params=params)
    if response.status_code == 200:
        result = response.json()
        json_result = json.dumps(result, sort_keys=False, indent=4)
        json_dict = json.loads(json_result)
        scan_id = json_dict.get('scan_id')
        return scan_id
    
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

if __name__ == '__main__':
    scan = check_link('https://google.com')
    link_check_result(scan)
    scan_id = check_file()
    file_check_result(scan_id)