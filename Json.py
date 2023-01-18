import json

""" x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y)
print(y["age"]) """



x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(x)
# print(type(x))
# print(json.dumps(x))
# print(json.dumps(x, indent=4))
# print( json.dumps(x, indent=4, separators=("... ", " = ")) )
# print(json.dumps(x, indent=4, sort_keys=True))

