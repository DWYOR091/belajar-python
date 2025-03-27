thislist = ["apple", "banana", "cherry","blueberry","melon"]
thislist.remove("banana")
print(thislist)

#remove spesifik index
thislist.pop(0)
print(thislist)
#jika tanpa index paramsnya akan menghapus akhir item
thislist.pop()
print(thislist)

#del
del thislist[1]
print(thislist)

#clear method menghapus semua item
thislist.clear()