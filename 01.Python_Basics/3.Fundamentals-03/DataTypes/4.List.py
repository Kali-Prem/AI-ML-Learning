# Lists--> mutable sequence of values  ==> []


# ---------------------------------------
marks = [99, 89, 47, 38,100]
print(marks)
print(len(marks)) #5
print(marks[4])  #index based printing allow
# print(marks[8])  #error => index out of range

marks[2] = 45  #lists are mutable (can be changed at any index position)
print(marks)



# -------------Slicing in List------------

# slicing means sublist bnana
# print(marks1[starting indx : ending index])

marks1 = [99, 89, 100, 65, 92, "abc", 100.99]

# print(type(marks1))
# print(marks[0:len(marks1)])
print(marks1[5:])
print(marks1[-5:-3])