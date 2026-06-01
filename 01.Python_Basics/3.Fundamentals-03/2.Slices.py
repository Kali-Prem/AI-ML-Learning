# syntax:  str[starting id : end idx]   --> end idx not included and if we left empty the end idx then by default it goes to the last index


# Note:- [ we take the index both negative or positive ]

# =========Default format for slicing in positive index   (0 to n-1)=================
str = "python" 
print(str[2:4])

# =--
word = "I am a hacker"
# print(word[0:13])
print(word[0:]) #when ending index is not defined then it takes to the end
print(word[0 : len(word)])
print(word[:7])  # if starting index is not defined then still print from 0
print(word[:])   #if remove start and ending both index then it takes 0 to ending index



# ========Negative Indexing  =========================
word1 = "python"     #n=-1, o= -2, h = -3 , t = -4, y = -5, p = -6

print(word1[-4:-1])    #print= tho [-4 is work like starting index and -1 is ending index]