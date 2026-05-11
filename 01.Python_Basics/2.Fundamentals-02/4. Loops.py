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

