list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

#using + operator
newList = list1 + list2
print(newList)

#append
for x in list1:
    list2.append(x)
print(list2)

#extend
newList = []
newList.extend(list2)
print(newList)