# formatting se dynamic string bnate hen

# Two ways to format:- 1) format() ->format function  2.) f-strings

# 
a = 5
b = 6
sum = a + b

# Normal formatting
print("language is {}".format("python"))   #python string will be put at the placeholder {}
print("sum is {}".format(sum)) # sum is 11
print("sum of {} & {} is {}".format(a,b, sum)) #sum of a & b is 11

# index based formatting
print("sum of {0} & {1} is {2}".format(a,b,sum))  #a is on 0 index and b is on 1 index and sum is on 2 index


# Value based formattting
print("value of vars {a} & {b}".format(a=5, b=6))





# ===================F-strings====================================
# -----Literal string interpolation


c = 5
d = 10
print(f"sum of {a} & {b} is {a+b}")
print(f"average of {c} & {d} is {(c+d)/2}")
print(f"diff of {d} & {c} is {d-c}")
