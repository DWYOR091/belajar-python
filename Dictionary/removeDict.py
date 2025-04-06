myDict = {
    "brand" : "Ford",
    "model" : "mustang",
    "year"  : 1964
}

myDict.pop("brand")
print(myDict)

myDict.popitem() #remove the last item
print(myDict)

myDict["color"] = "red"
del myDict["model"]
print(myDict)

#clear all dict
myDict.clear()
print(myDict)

