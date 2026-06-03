# ============Prime Number Check===========
num = int(input("enter the number: "))
# num = 23
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print(True)
else: print(False)


# ==========Fibonacci Series================
n = int(input("enter the number: "))
a = 0
b = 1
# if n == 1:
#     print(a)
# if n == 2:
#     print(b)

# for i in range(3,n+1):
#     temp = a + b
#     a = b
#     b = temp
# print(temp)

for i in range(n):
    print(a)

    temp = a + b
    a = b
    b = temp


# ==========Remove Duplicates from List============
nums = [2,3,4,5,6,7,2]
unique = list(set(nums))
print(unique)

# ==========Word Frequency Counter==============
text = input("ENter word for frequency count: ")



# ==========Palindrome Check==================
text = input("Enter the number to check palindrome: ")
