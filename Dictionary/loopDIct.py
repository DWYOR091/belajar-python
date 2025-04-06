myDict = {
    "brand" : "Ford",
    "model" : "mustang",
    "year"  : 1964
}

#key
for x in myDict:
    print(x)
    
#print all values
for x in myDict:
    print("opsi 1",myDict[x])
    
#opsi 2 print all value
for x in myDict.values():
    print("opsi2: ",x)
    
#keys
for x in myDict.keys():
    print("key: ",x)
    
for x,y in myDict.items():
    print(y) #loop keys
    print(x) #loop values
    
#copy dict
myDict2 = myDict.copy()
print("hasil copy:",myDict2)

#nested dict
myCars = {
    "car1":{
        "brand" : "Ford",
        "model" : "mustang",
    },
    "car2":{
        "brand" : "Honda", 
        "model" : "civic",
    },
    "car3":{
        "brand" : "Tesla", 
        "model" : "model 3",
    }
}

print("Hasil nested:",myCars)

