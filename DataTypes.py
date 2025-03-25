# getting data type
print(type(5))
iniString = "string"
iniBoolean = True
iniTuple = ("pisang", "jeruk", "apel") #sama dengan list tapi immutable
iniList = ["pisang", "jeruk", "apel"] #array atau list
iniFrozenSet = frozenset({"pisang", "jeruk", "apel"}) 
iniSet = {"haha","haha","haha"}
iniDict = {1 : "pisang", "jeruk" : "jeruk", "apel" : "apel"}
iniRange = range(0,10)
iniNone = None
print(type(iniString))
print(type(iniBoolean))
print(type(iniTuple))
print(type(iniList))
print(type(iniFrozenSet))
print(type("haha" in iniSet))
print(type(iniSet))
print(type(iniDict))
print(iniDict[1])
print(iniRange)
print(type(iniRange))
print(type(iniNone))