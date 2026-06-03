#======= Print all even numbers from 1 to 100
for i in range(2,101,2):
    print(f"Even number is {i}")
# Or
for i in range(1,101):
    if i % 2 == 0:
        print(i)

# ======Take input n and print sum from 1 to n.
n = int(input("enter the number"))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)

# =======Reverse a string (Input: "python")
s = input("enter your string: ")
# s = "python"
print(s[::-1])



# =======Count vowels in a string.
text = input("enter String: ").lower()
count = 0
for i in text:
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        count += 1
print(count)

# OR
count = 0
for i in text:
    if i in "aeiou":
        count += 1
print(count)


# ===========Find Largest Number in List=======

nums = [2,3,4,5,6,7,8]
largest = nums[0]
for val in nums:
    if val > largest : 
        largest = val
print("Largest number: ",largest)