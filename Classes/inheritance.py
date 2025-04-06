class Animal:
    def __init__(self,name,age,sound):
        self.name = name
        self.age = age
        self.sound = sound
        
    def makeSound(self):
        print("suara",self.sound)
        
class Dog(Animal):
    def __init__(self, name, age, sound,color):
        super().__init__(name, age, sound)
        self.color = color
        
    def makeSound(self):
        super().makeSound()
        return f"{self.name} berwarna {self.color}"
        
        
animal1 = Dog("Dogi",2,"woof","black")
print(animal1.makeSound())


