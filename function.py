def iniFungsi():
    print("ini adalah fungsi")
    
    
iniFungsi()

def myName(fname,lname):
    print("hello:",fname,lname)
    
myName("Muhamad","Rifqi")

#keyword argument
def child(child1,child2):
    print("the youngest child is:",child2)
    
child(child1="sule",child2="kocak")

#keyword **kwargs 
def binatang(**hewan):
    print("ini binatang darat:", hewan["darat"])
    
binatang(darat="buaya",air = "ikan")

#default parameter
def paramsDefault(name="wakwaw"):
    print("nama saya", name)
paramsDefault()

#passing list argusmen
def list(fruits):
    for x in fruits:
        print("buah:",x)
items = ["apple","banana","cherry"]
list(items)

def perkalian(a,b):
    return a * b

print(perkalian(2,2))

def kocak():
    pass

#args
def iniArgs(*args):
    return sum(args)
print(iniArgs(1,2,3,4,5))

