thislist = ["apple", "banana", "cherry"]
#loop melalui list
for x in thislist:
    print(x)
    
#loop melalui index
for i in range(len(thislist)):
    print(i)

#while loopp
y = 0
while y < len(thislist):
    print(thislist[y])
    y += 1

#using comprehension (short hand)
thislist2 = ["mobil","motor","truk"]
[print(z) for z in thislist2]
