myTuple = ("banan","orange","kiwi")

myit = iter(myTuple)
print(next(myit))
print(next(myit))
print(next(myit))

myName = "rifqi"
myit2 = iter(myName)
print(next(myit2))
print(next(myit2))
print(next(myit2))      
print(next(myit2)) 
print(next(myit2)) 

#class
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myClass = MyNumbers()
myit3 = iter(myClass)
print(next(myit3))
print(next(myit3))
print(next(myit3))