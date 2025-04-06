#fungsi lambda ini digunakan untuk membuat fungsi yang sederhana
#cuman bisa 1 expression saja

# x = lambda a : a + 2

# print(x(1))

#multiple argument
x = lambda a,b : a +b
print(x(2,3))

def test(a,b,c):
    return lambda x: a * x + b * x + c

test1 = test(2,2,2)
test2 = test(3,3,3)
test3 = test(4,4,4)


print(test1(1))
print(test2(2))
print(test3(3))