# Generally we use for loop
nums = [2,3,5,6,7,5,4,10]

for i in nums:
    print(i)


# find x = 10 and return that index
x = 10
count = 0
for val in nums:
    if(val == x):
        print(f"index of {x} is {count}")
        break
    count += 1
    
