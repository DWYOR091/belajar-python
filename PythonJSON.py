import json

#parse json json.loads
a = '{"name":"rifqi","hobi": "main game"}'
b = json.loads(a)
print(b)
print(b["name"])


#conver python to json
d = {
    "name" : "rifqi",
    "kota": "bandung",
    "hobi": "main game"
}

e = json.dumps(d)
print(e) #hasilnya json string q

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

y = json.dumps(x,indent=3,separators=(".","="),sort_keys=True)
print(y)
