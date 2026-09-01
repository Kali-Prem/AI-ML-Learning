class Car:
    # constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # method
    def full_name(self):
        return f"{self.brand} {self.model}"

# objects
my_car = Car("tata", "Safari")
new_car = Car("Toyota", "Fortuner")

print(my_car.brand)
print(new_car.brand)
print(new_car.model)


# Inherite the property from the parent . Extend the property
class ElectricCar(Car):
    # constructor
    def __init__(self,brand,model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

# Objects creation
car1 = ElectricCar("toyato", "lafa", "85kWh")
print(car1.battery_size)
print(car1.brand)
print(car1.model)

