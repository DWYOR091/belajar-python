#how to change or update value in tuple
myTuple = ("motor","mobil","becak")
myTupleUpdate = list(myTuple)
myTupleUpdate[1] = "pesawat"
myTuple = tuple(myTupleUpdate)
print(myTuple)

#add item in tuple
#conver into list
addNewItem = list(myTuple)
addNewItem.append("kereta")
myTuple = tuple(addNewItem)
print(myTuple)
#add tuple to tuple
addNewTuple2 = ("Mobil listrik",)
myTuple += addNewTuple2
print(myTuple)

#remove tuple
#conver to list
removeMyTuple = list(myTuple)
removeMyTuple.remove("pesawat")
myTuple = tuple(removeMyTuple)
print(myTuple)

del myTuple 
print(myTuple) #error karena sudah dihapus

