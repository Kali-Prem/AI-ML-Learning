# Conditional Statements
'''
if, elif, else
'''

age = int(input("Enter your age: "))

if age >= 18:
    print("you can vote")
    print("you can drive")
else:
    print("you can not vote")





# Note:  elif = is used with if condition

# Traffic ligth
color = input("Enter color: ")

if color == "red":
    print("stop")
elif color == "gree":
    print("go")
elif color == "yellow":
    print("look")
else:
    print("wrong color for traffic light")







# WAP    AGE
age = int(input("Enter your age: "))

if (age < 13):
    print("child")
elif (age>=13 and age<18):
    print("teenager")
else:
    print("Adult")



# ===========WAP IF username="admin" and password="pass" then allow to login===

username = input("Enter your username: ")
password = input("Enter your passowrd: ")

if (username == "admin" and password == "pass"):
    print("Successfully login")
elif (username == "admin"):
    print("Please enter valid password")
elif (password == "pass"):
    print("Please enter valid username")
else:
    print("Your username and password is incorrect")




# =========WAP to check n is the multiple of 5 or not============
n = int(input("Enter number:  "))
if(n%5 == 0):
    print("Number is multiple of 5")
else:
    print("Number is not a multiple of 5")





# ==========WAP to check n is even or odd numbres ==============
n = int(input("enter number: "))

if(n % 2 == 0):
    print("Number is even")
else:
    print("numerb is not odd")