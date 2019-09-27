import requests
import json

url_base = 'http://localhost:8080/api'
creds = ("admin", "admin")
accept_header = [
    'application/vnd.yang.api+json',
    'application/vnd.yang.datastore+json',
    'application/vnd.yang.data+json',
    'application/vnd.yang.collection+json'
]
headers = {'Accept': ','.join(accept_header)}

response = requests.get(
    f'{url_base}/running/devices/device', auth=creds, headers=headers).json()
#print(json.dumps(response, indent=2, sort_keys=True))
devices = response['collection']['tailf-ncs:device']
for device in devices:
    print(f"Name: {device['name']}")
    print(f"IP: {device['address']}")
    print(f"SSH Port: {device['port']}")
    print(" ")
