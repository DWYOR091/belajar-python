class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        return f"move !!"
    
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        return f"Sail!"
    
class Airplane(Vehicle):
    def move(self):
        return f"Fly!"
    
myCar = Car("Ford","Mustang")
myBoat = Boat("Honda","Civic")
myAirplane = Airplane("Boeing","747")

print(myCar.move())
print(myBoat.move())
print(myAirplane.move())
