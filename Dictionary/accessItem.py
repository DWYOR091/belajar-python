thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

#accessing items
x = thisDict["model"]
print(x)

y = thisDict.get("brand")
print(y)

#get key
z = thisDict.keys()
print(z)

#get values
v = thisDict.values()
print(v)
thisDict["model"] = "galardo"
print(thisDict["model"])

#get items
i = thisDict.items()
print(i)

#check if keys exist
if "model" in thisDict:
    print("ya ada!")
    
