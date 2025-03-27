thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist2 = [1,5,10,9,3,2,4]
thislist2.sort(reverse=True)
print(thislist2)

# custom sort
thislist3 = [100, 50, 65, 82, 23]
def myFunc(n):
    return abs(n - 50)

thislist3.sort(key = myFunc)
print(thislist3)

#case intensive sort
thislist4 = ["banana", "Orange", "Kiwi", "cherry"]
thislist4.sort(key = str.lower)
print(thislist4)

#reverse
thislist4.reverse()
print(thislist4)