iniList = ["banana","apple","melon","jeruk"]

for x in iniList:
    if x == "apple":
        continue
    print(x)

#range function
for x in range(11):
    if x % 2 == 0:
        continue
    print(x)
else:
    print("selesai")
    
# for a in range(4, 10):
#     print(a)

# for i in range(2,20,2):
#     print("genap",i)


    
#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)