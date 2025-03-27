fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
#comphrension
# newlist = [x for x in fruits if "a" in x]
for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print(newlist)

upperList = [x.upper() for x in fruits ]
print(upperList)

newlist2 = [x for x in range(10) if x > 5]
print(newlist2)