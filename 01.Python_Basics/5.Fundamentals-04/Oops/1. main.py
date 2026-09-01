# class ko ek form ki tarah samjho . jese ki bank me koi ek form same hota hai aur usme bahut sare user aa krke apna naam ka value dete hen kyunki form me sirf "name:- " sirf likha rhta hai aur log aa krke usme uska value de krke 
class Car:
    # Constructor || self is a keyword (like this in Java) jisse current object ki properties access hoti hain
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    # methods inside the class
    def full_name(self):
        return f"{self.brand} {self.model}"

# Car() - class ka name with bracket lgate hi ek object create kr deta hai memory me but abb eske address ke reference ko ek object ka name de krke hum usme store krwa dete hen warna ess object ko access hi nhi kr payenge
my_car = Car("TATA","Safari")   # yahan jese hi object bna waise hi contructor call hua car class ka aur usko value diya gya brand ka aur model ka
your_car = Car("Toyota","Fortuner") 
car1 = Car("Hyundai","Creta")

# hum chahte hen ki my_car ka brand kya hai aur model kya hai usko print krwana 
print(my_car.model)
print(my_car.brand)
print(my_car.full_name())

# print(car1.brand)
# print(car1.model)

# ---------------------- VERY IMPORTANT ---------------------

    #                 CLASS
    #               ┌─────────┐
    #               │   Car   │
    #               │         │
    #               │ __init__│
    #               │full_name│
    #               └────┬────┘
    #                    │
    #          creates instances
    #                    │
    #       ┌────────────┼────────────┐
    #       ▼            ▼            ▼

    #   my_car        your_car       car1
    #      │             │             │
    #      ▼             ▼             ▼
    # ┌─────────┐   ┌─────────┐   ┌─────────┐
    # │ Object  │   │ Object  │   │ Object  │
    # │         │   │         │   │         │
    # │ brand   │   │ brand   │   │ brand   │
    # │ TATA    │   │ Toyota  │   │ Hyundai │
    # │         │   │         │   │         │
    # │ model   │   │ model   │   │ model   │
    # │ Safari  │   │ Fortuner│   │ Creta   │
    # └─────────┘   └─────────┘   └─────────┘

# when u do : my_car.full_name()
    # then python conceptually does:-

    # my_car.full_name()
    #    ↓
    # find full_name from Car
    #    ↓
    # call full_name with my_car
    #    ↓
    # self = my_car
    #    ↓
    # self.brand → TATA
    # self.model → Safari
    #    ↓
    # "TATA Safari"



# ===========NOTes==================

        # Bas ye chain dimaag mein permanently set kar lo:
        # Class → blueprint
        # Car(...) → instance creation + initialization
        # object → actual instance
        # my_car → object ko refer karne wala name
        # self → currently used object
        # self.brand → current object ki brand attribute
        # my_car.full_name() → full_name ko my_car ke context mein call karna
        # self hi woh bridge hai jo same method ko different objects ke saath kaam karwata hai.