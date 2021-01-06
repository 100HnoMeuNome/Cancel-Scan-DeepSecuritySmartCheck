import requests
import json

verifyCert=False
username = "administrator"
password = "<senha>"
url = "https://url"
large_number = 100
payload = {
  "user": {
    "userID": username,
    "password": password
  }
}
session = requests.post(f"{url}/api/sessions",json=payload,verify=verifyCert)
token = json.loads(session.text)["token"]
scans_body = requests.get(f"{url}/api/scans?status=pending&limit={large_number}",headers={"Authorization": f"Bearer {token}"},verify=verifyCert)
scans = json.loads(scans_body.text)['scans']
for scan in scans:
  current_scan = scan['href']
  requests.delete(f"{url}{current_scan}",headers={"Authorization": f"Bearer {token}"}, verify=verifyCert)