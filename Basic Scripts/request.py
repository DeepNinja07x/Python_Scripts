import requests

response = requests.get("")
print(response.json())
print(response.status_code)