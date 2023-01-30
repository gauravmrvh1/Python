import requests
import json

r=requests.get('https://hulkv2.urbanladder.com/v1/consumers/3757364/profile')
x=r.json()
print(x)