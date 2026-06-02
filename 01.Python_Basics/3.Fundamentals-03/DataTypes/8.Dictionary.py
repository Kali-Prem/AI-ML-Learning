# key:value pairs
# keys are always unique and duplicates are not allowed
# defined by = {}
# dictionary are mutable means we can changes the values
# dictionary -> unordered hote hen


info = {
    "name": "Kali linux",
    "CGPA" : 9.2,
    "subjects": ["maths", "science"],
    3.14 : "PI"
}

# print(info)
# print(info["name"])
# print(info["CGPA"])


# dictionary_keys = info.keys()
dictionary_keys = list(info.keys()) #typecasting to list
print(dictionary_keys)
print(info.keys()) #print all the keys

# =============ALL Dictionary Functions ============
'''
d.keys() =  #return all the keys
d.values()  = #return all the values
d.items()   = #returns (key,val) pairs
d.get(val)  = #return val acc. to key
d.update(new_item)  = #adds new item to dict

'''
