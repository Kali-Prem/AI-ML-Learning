#============= While Loops=================

# while condition:          jb tk condition true rhega tb tk print krwate rho 
#     print("Hello")


# ======Infinite lOOP
# while True:
#     print("Kali linux")

# ----------------------------
i = 1; #itrator
while (i <= 5):
    print("Kali linux", i)
    i += 1


# ----------PRINT NUMBERS 1-5-------
i = 1
while (i <= 5):
    print(i)
    i += 1


# ---------Print Multiplication table------
n = int(input("enter the number: "))
i = 1
while (i<=10):
    print(i * n)
    i += 1





# ==========Break & Continue Loops=============
i = 1
while (i<=10):
    if (i % 6 == 0):
        break
    print(i)
    i += 1 
print("Outside the loop now")


# continue -> ye kisi iteration ko skip krwane ke liye use kiya jta hai 
# jese agar mujhe 1 se 10 tk sare 3 ke multiple ko skip krke print krwana hoga toh hum continue ka use krenge
i = 1
while (i <= 10):
    if(i % 3 == 0):
        i += 1
        continue
    print(i)
    i += 1



# =======Print EVEN NUMBERS 1 - 50 ==================
i = 2
while (i <= 50):
    print(i)
    i += 2



# ========Sun of first N natural numers===========
n = int(input("enter the number: "))
sum = 0
i = 1
while(i <= n):
    sum = sum + i
    i += 1
print("Sum", sum)


# ========4. Reverse counting from 20 to 1========
i = 20
while (i > 0):
    print(i)
    i -= 1

# ==========Reverse a number=================
num = int(input("Enter the number ot reverse: "))
revNo = 0
while(num > 0):
    revNo = revNo*10 + num % 10
    num = num // 10
print(revNo)

# =========Count digits in a number============
num = int(input("Enter number to count digit: "))
count = 0
while(num > 0):
    count += 1
    num = num // 10     #remove the last digit
print("total count digit: ",count)

# --------------------------------------------------------

# =========Check palindrome number=============
num = int(input("Enter num to check Palindrome: "))
reversed = 0
temp = num
while(num > 0):
    digit = num % 10
    reversed = reversed*10 + digit
    num = num // 10
if(reversed == temp):
    print("Number is palindrome")
else:
    print("Number is not palindrome")



# --------------ATM Machine Simulation--------------------


