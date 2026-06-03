# list = []
# tuples = ()
# dictionary = {}
# sets = {}

# Givne list
info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
] 

# print all the tuples
for tup in info:
    print(tup)

# print the tuples first index value and second index value
for tup in info:
    print(tup[0])
    print(tup[1])

#  OR      #Note:- hum direct value ko bhi tuple se le skt ehen
for name,course in info:
    print(name,course)

# print the subject only
for tup in info:
    print(tup[1])

# LIST ALL UNIQUE COURSES
s = set()
for tup in info:
    s.add(tup[1])
print(s)


# LIST students enrolled in english
count = 0
for tup in info:
    if(tup[1] == "English"):
        count += 1
print(count)