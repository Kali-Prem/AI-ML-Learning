# Data ko private krna ya hide krna .
# kisi bhi attribute ko private bnane ke liye do baar underscore lgate hen __brand
# class se bahar attribute ya variable ko access krne ke liye getter function ka use krte hen jo (get_attributeName(self)) hota hai

class Car:
    # constructor
    def __init__(self, brand, model):
        # self.brand = brand  # NOte private
        self.__brand = brand  #this is private(class ke bahar esko access krne ke liye abb getter function chahiye)
        self.__model = model  #this is also a private 
 
    # getter function -- return something
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model

    # setter functon
    def set_brand(self,brand):
        self.__brand = brand

    def set_model(self,model):
        self.__model = model

    # method
    def full_name(self):
        return f"{self.brand} {self.model}"

# objects
my_car = Car("tata", "Safari")
new_car = Car("Toyota", "Fortuner")

my_car.set_brand("Kali")
my_car.set_model("LInux")

# print(my_car.brand) #gives error because brand is private so error is Car object has no attribute brand
print(my_car.get_brand())
print(my_car.get_model())

print(new_car.get_brand())
print(new_car.get_model())
# print(new_car.brand)
# print(new_car.model)
