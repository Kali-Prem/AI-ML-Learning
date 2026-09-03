# POlymorphism--> same function with different work then polymorphism hoga

class Car:
    total_car = 0
    def __init__(self,brand, model):  #Constructor
        self.brand = brand
        self.model = model
        # self.total_car += 1
        Car.total_car += 1

    # function for polymorphism---------
    def fuel_type(self):
        return "Diseal"
    
# child class
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    # function for polymorphism----------
    def fuel_type(self):
        return "Electricity"


# OBject creation
safari = Car("tata","leva")   #OBject bnte time hi constructor call ho jat ahai 
safari3 = Car("tata","Nexon")
print(safari.brand)
print(safari.model)
print(safari.fuel_type()) # same function here retrun Diseal

# OBject creation for electricCar
car1 = ElectricCar("hello","x11x","85kWh")
print(car1.model)
print(car1.brand)
print(car1.fuel_type())   #same function here return Electricity

print(Car.total_car)