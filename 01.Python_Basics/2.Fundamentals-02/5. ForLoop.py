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



# ------------



