# Tuples datatypes are immutable sequences of values
# Tuples = ()
# we cannot assigned value (same as strings)
# Tuples methods/functions => t.index(val) #returns 1st occurence idx
#                          => t.count(val) #counts total occurences

# all will be same = same loop , same slicing etc.............

tup = (1,2,3,4,5,6,7, "abc", 3.24)
print(tup)
print(type(tup))

# index based 
print(tup[3])

#=========== Single value tuple==========

# tup1 = ("abc") # this is string
# print(type(tup1)) #print = string

tup1 = ("abc",) # so if we want to create single value tupple we have to put one comma after the value
print(type(tup1)) # print = tuple


# loop
for val in tup:
    print(val)

# calculate sum of tup
tup3 = (1,2,3,4,5,6,3.45)
sum = 0
for val in tup3:
    sum = sum + val
print(f"sum of value is of tup3 is {sum}")



# ============Tuples Functions/Methods=============

tup4 = (1,2,3,4,2,2,2,5,6,3.45)
print(tup4.count(2))  #return the total occurence of 2 in this tuple
print(tup4.index(2))  #return the first index at which 2 will be exist

