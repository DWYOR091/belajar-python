#loop use for
myTuple = ("apple", "banana", "cherry")
for x in range(len(myTuple)):
    print("1: ",myTuple[x])
    
#while loop
x=0
while x < len(myTuple):
    print("2: ",myTuple[x])
    x += 1
    
#using comprehension (short hand)