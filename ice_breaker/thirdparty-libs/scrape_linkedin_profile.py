import os
import requests

api_key = "YOUR_API_KEY"
headers = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
print(f"Headers {headers}")
api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
params = {"url": "https://www.linkedin.com/in/davidblake/"}
response = requests.get(api_endpoint, params=params, headers=headers)
print(response.json())
