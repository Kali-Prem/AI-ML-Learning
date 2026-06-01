# Note: string ko hum "",'',''' ''' ->teeno se define kr skte hen but generally we use double quotes
# for character , we use single quotes

word = "python"
print(len(word))   #length function 

#----- Concatenation---
word1 = "kali"
word2 = "linux"
# sentence = word1 + " " + word2
print(word1+" "+ word2)   # kali linux


# =====Indexing- start from 0= == = = == = 

word3 = "love python" # length = 11
print(word3[5])


# for loop in string
word4 = "I love Hacking"

for ch in word4:  #print using each char 
    print(ch)

n = len(word4)
for i in range(0,n):  #print using traversing through index number
    print(word4[i])



# ====================Note: Python strings are  Immutable -----------

# we can not assign the value at some positon in string
# word4[4] = 'h' #error because in python we cannot assigned value to a string so
#Therefore strings are called immutable in python means which cant changed



