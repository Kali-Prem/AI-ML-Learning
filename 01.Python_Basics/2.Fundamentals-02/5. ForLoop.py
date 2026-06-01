# For in Loop syntax: 
#   for i in range(start,end,iteration):

string = "hello"


#in => membership operator

for var in string: #in se string ke sare char var ek variable ka naam hai usme jark store hoga aur var ke jagah kuchh bhi likh kste hen
    print(var)


# in ko presence check krne ke liye bhi use krte hen jese 
#check krna ho ki string me 'o' exist krta hai ya nhi 
if 'o' in string:
    print(" o is exist in the stirng")

# Or
for k in string:
    if( k == 'o'):
        print("exsit")





#===============Sequence============
#range(5) means 0 se lekr n-1 tk kyunki 0 se start hua hai 
for i in range(5):
    print(i)

for k in range(10):
    print(k+1)

# 

# ---------count 'i' how many times occurs in this word-----------
word = "artificial intelligence"
count = 0
for ch in word:
    if(ch == 'i'):        #singel char ko hamesha single quote ke saath likhte hne
        count += 1
print(count)



# ------------1. Print numbers from 1 to 10---------------
for i in range(1,11):    #range start from 0 . so i add 1 in the print function
    print(i)


# -------------2. Print even numbers from 1 to 50------

for i in range(2,51, 2):
    print(i)

# ------------3. Sum of first N natural numbers----
n = int(input("enter your number :"))
sum = 0
for i in range(1,n):
    sum = sum + i
print(sum)


# ---------4. Multiplication table------
n = int(input("enter the number:"))
for i in range(1,11):
    print(i*n)




# ---------5. Factorial of a number-----------
num = int(input("enter your number: "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print(factorial)


# --------6. Reverse a string----------
word = input("enter th word: ") #word = "hello"
reverse = ""
for ch in word:
    reverse = ch + reverse
print(reverse)



# ---------7. Count vowels in a string--------
word = input("Enter Word for vowel count: ")
word.lower()
print(word.lower())
count = 0
for ch in word:
    if ch in "aeiou":
        count += 1

    # if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    #     count += 1
print(count)



# ---------


