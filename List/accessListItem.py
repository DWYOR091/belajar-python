thislist = ["pisang","mangga","jeruk","kiwi","strawberry","melon"]
print(thislist[1]) #item ke 2

# negatif index
print(thislist[-1]) #jeruk

#range of index
print(thislist[2:]) #2 ke kanan

print(thislist[:2])# 2 ke kiri

#check item in list
if "melon" in thislist:
    print("ada")
else:
    print("tidak ada")