#acces tuple with index
myTuple = ["apple", "banana", "cherry"]
print(myTuple[1])

#negative index
print(myTuple[-1])

#range index
print(myTuple[1:2])
print(myTuple[:2])
print(myTuple[1:])
print(myTuple[-3:-2])

#check item if exist
if "apple" in myTuple:
    print("ada")
else:
    print("tidak ada")
