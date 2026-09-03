# Desing & create an online store for products (name, price).
# Track total products being created
#  Create a static method to calculate discount on each product based on a % parameter

class Product:
    total_product = 0
    def __init__(self, name,price):
        self.name = name
        self.price = price
        Product.total_product += 1

    # Instance methond
    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.total_product}")

    @staticmethod   #static method ko class ke property se koi lene dena nnhi hota hai aur usko object sebhi kuchh lena dena nhi hota ha
    def calc_discount(price, discount):
        print(f"discounted price = {price - (price * discount / 100)}")
    

p1 = Product("phone","15_000")
p2 = Product("Laptop", "50_000")

Product.get_count()
p1.calc_discount(10_000, 12)