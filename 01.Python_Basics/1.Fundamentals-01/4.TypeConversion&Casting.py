'''
int -> float
float -> int
int -> bool

'''

# =========Types=========

#  1.Type conversion -> automatic conversion in python

# 2. Type Casting -> developer will change

ans1 = int(5+ 10.0) #casting
ans2 = 5 + 10.0     #conversion

print(ans1,type(ans1))
print(ans2,type(ans2))


val = int("123")
print(type(val))

val = bool(10)
print(val,type(val))
