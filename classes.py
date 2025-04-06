class MyClass:
    #properti
    x = 5
    
#create obj
p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    

person1 = Person("Rifqi",20)

print(person1.name,person1.age)

#method __str__
class Turunan(Person):
    def __init__(self, name, age,hobi):
        super().__init__(name, age)
        self.hobi = hobi
        
    def __str__(self):
        return f"nama saya {self.name},umur saya {self.age}, dan hobi saya {self.hobi}"
    
person2 = Turunan("Rifqi",20,"main game")
#modify property
person2.age = 22
#delete hobi property
del person2.hobi
#tidak akan error karena sudah ada method __str__ 
print(person2)

class PassError:
    pass