import os
import json, requests, re

API_ENDPOINT="https://api.github.com/users/Ayon-ssp"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

resp = requests.get(API_ENDPOINT, headers=headers)
Json_data = json.loads(resp.text)
jsonContent = json.dumps(Json_data, indent=4)
# print(jsonContent)

with open('Ayon_ssp.json', "w") as f:
  f.write(jsonContent)