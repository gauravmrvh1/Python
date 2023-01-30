import requests
import json

x = requests.get('https://restcountries.com/v2/all')
# print(x.text)
# print(type(x.text))
# print(json.loads(x.text))
# print(x.status_code)

res = json.loads(x.text)
for x in res:
    print(x['name'])




# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {'somekey': 'somevalue'}
# x = requests.post(url, json = myobj)
# x = requests.post(url, data = myobj, timeout=0.001)



# x = requests.delete('https://w3schools.com/python/demopage.php')
# print(x.text)
# print(x.status_code)





# url = 'https://w3schools.com/python/demopage2.php'
# myobj = {'somekey': 'somevalue'}
# x = requests.post(url, data = myobj, cookies = {"favcolor": "Red"})
# print(x.text)