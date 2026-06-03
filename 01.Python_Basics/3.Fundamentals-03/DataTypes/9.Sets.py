# sets are collection of unique elements
# dictionary and sets are in curly braces but in dictionary contains key value pairs but in sets only unique elements
# sets are mutable and unordered

s = {3,3,5,6,6,7,8,4,6}

print(s)  #print: {3, 4, 5, 6, 7, 8}
print(len(s))
print(type(s))

s.add(5)  #add any element in the sets

empty_set = {}   #this create a dictionary 
print(type(empty_set)) #dictionary

empty_set1 = set()       #empty sets
print(type(empty_set1))   #set


# ============-Set Methods/Functions==================
'''
s.add(val)        #add a value
s.remove(val)     #removes a value
s.clear()         #empties the set
s.pop()           #removes a random value
s.union(set2)     #returns new union
s.intersection(set2)  #returns new intersection 

'''

s.add(10)
s.remove(3)
print(s)
s.pop()
print(s)

s2 = {8,9,1,2}
print(s.union(s2))
print(s.intersection(s2))