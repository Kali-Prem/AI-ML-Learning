# ============================================================
# PYTHON OOP — DEEP SHORT NOTES
# ============================================================


# ------------------------------------------------------------
# 1. CLASS
# ------------------------------------------------------------

class Car:
    # Class = Blueprint / template
    # Class banne par Python ek class object create karta hai.
    # Iske andar methods (__init__, full_name) defined hote hain.

    def __init__(self, brand, model):
        # __init__ automatically call hota hai jab Car ka object banta hai.
        #
        # Car("TATA", "Safari")
        #        ↓
        # __init__(object, "TATA", "Safari")
        #
        # self = jis object ke liye __init__ chal raha hai
        # brand = "TATA"
        # model = "Safari"

        self.brand = brand
        self.model = model

        # self.brand  → object ki attribute/property
        # brand       → sirf __init__ ka local parameter
        #
        # self.brand = brand
        #        ↓
        # current_object.brand = "TATA"


    def full_name(self):
        # self = jis object se method call hua hai
        #
        # my_car.full_name()
        #        ↓
        # Car.full_name(my_car)
        #        ↓
        # self = my_car

        return f"{self.brand} {self.model}"


# ------------------------------------------------------------
# 2. OBJECT CREATION
# ------------------------------------------------------------

my_car = Car("TATA", "Safari")

# Back-end conceptually:
#
# Car("TATA", "Safari")
#        ↓
# New Car object create hota hai
#        ↓
# __init__(new_object, "TATA", "Safari")
#        ↓
# self = new_object
#        ↓
# self.brand = "TATA"
# self.model = "Safari"
#        ↓
# my_car ───────► new_object
#
#
# Memory ka simple mental model:
#
# my_car ───────► Car Object
#                    ├── brand = "TATA"
#                    └── model = "Safari"


# ------------------------------------------------------------
# 3. MULTIPLE OBJECTS
# ------------------------------------------------------------

your_car = Car("Toyota", "Lenka")
car1 = Car("Hello", "Linux")

# Har Car(...) par NEW object create hota hai.
#
# my_car  ───► Object 1
#               brand = "TATA"
#               model = "Safari"
#
# your_car ──► Object 2
#               brand = "Toyota"
#               model = "Lenka"
#
# car1 ──────► Object 3
#               brand = "Hello"
#               model = "Linux"
#
# Class same hai, lekin objects aur unka data alag hai.


# ------------------------------------------------------------
# 4. ACCESSING ATTRIBUTES
# ------------------------------------------------------------

print(my_car.brand)
# my_car → Object 1
# Object 1 ke andar brand → "TATA"

print(my_car.model)
# my_car → Object 1
# Object 1 ke andar model → "Safari"


# ------------------------------------------------------------
# 5. METHOD CALL
# ------------------------------------------------------------

print(my_car.full_name())

# Normal syntax:
#
# my_car.full_name()
#
# Python conceptually:
#
# Car.full_name(my_car)
#        ↓
# self = my_car
#
# Method ke andar:
#
# self.brand → my_car.brand → "TATA"
# self.model → my_car.model → "Safari"
#
# return:
# "TATA Safari"


# ------------------------------------------------------------
# 6. SAME METHOD — DIFFERENT OBJECT
# ------------------------------------------------------------

print(your_car.full_name())

# Conceptually:
#
# Car.full_name(your_car)
#        ↓
# self = your_car
#
# self.brand → "Toyota"
# self.model → "Lenka"
#
# Result:
# "Toyota Lenka"


# ------------------------------------------------------------
# 7. MOST IMPORTANT CONCEPT
# ------------------------------------------------------------

# self = CURRENT OBJECT
#
# my_car.full_name()
#       ↓
# self = my_car
#
# your_car.full_name()
#       ↓
# self = your_car
#
# car1.full_name()
#       ↓
# self = car1
#
# Isi wajah se SAME method different objects ke liye
# different data ke saath kaam karta hai.


# ------------------------------------------------------------
# 8. IMPORTANT DIFFERENCE
# ------------------------------------------------------------

# brand
# → __init__ ka local parameter
#
# self.brand
# → object ki attribute/property
#
# Example:
#
# def __init__(self, brand, model):
#                  ↑      ↑
#               parameter
#
# self.brand = brand
# ↑           ↑
# object      parameter
# attribute


# ------------------------------------------------------------
# 9. self IS NOT A KEYWORD
# ------------------------------------------------------------

# self Python ka keyword nahi hai.
# Ye sirf convention hai.
#
# Technically:
#
# def __init__(abc, brand, model):
#     abc.brand = brand
#
# bhi kaam karega.
#
# Lekin Python mein hamesha "self" use karna standard hai.


# ------------------------------------------------------------
# 10. ONE-LINE MEMORY MODEL
# ------------------------------------------------------------

# CLASS
#   ↓
# Blueprint
#
# Car(...)
#   ↓
# New object
#
# __init__()
#   ↓
# Object initialize
#
# self
#   ↓
# Current object
#
# self.brand
#   ↓
# Current object's brand
#
# obj.method()
#   ↓
# Class.method(obj)
#
#
# GOLDEN CHAIN:
#
# Car("TATA", "Safari")
#        ↓
# Object created
#        ↓
# __init__(object, "TATA", "Safari")
#        ↓
# self = object
#        ↓
# self.brand = "TATA"
# self.model = "Safari"
#        ↓
# my_car ───► object
#        ↓
# my_car.full_name()
#        ↓
# full_name(my_car)
#        ↓
# self = my_car
#        ↓
# "TATA Safari"