import requests
import json

url = 'https://reqres.in/api/users'
response = requests.get(url)
print(response.json())