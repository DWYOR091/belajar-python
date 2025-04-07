#local scope in func
# def myFunc():
#     x = 10
#     return x
    
# print(myFunc())


#func inside func

# def func1():
#     x = 30
#     def func2():
#         print(x)
#     func2()
    
# func1()


#global scope
# a = 50
# def myFunc2():
#     return a

# print(a)

#naming variable jadi menjadi beda meskipun namanya sama yg satu luar satu lagi d dalam.
z = 100
def namingVar():
    z = 200
    def kocak():
        nonlocal z #nonlocal fungsinya untuk mengubah variable luar
        z = 300
    kocak()
    return z

# print(z)
print(namingVar())