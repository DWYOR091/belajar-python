thislist = ["apple", "banana", "cherry"]

#append nambah di akhir
thislist.append("kocak")

#insert nambah di index tertentu
thislist.insert(1, "gaming")

#extend list untuk menggabungkan 2 list
thislist2 = ["alpukat", "nanas", "melon"]
thislist.extend(thislist2)
print(thislist)

#add any iterable object
thistuple = ("tahu","tempe")
thislist2.extend(thistuple)
print(thislist2)