# File Operations: {Open, read & close}
# f = open("data.txt", "r")
# yahan pr hum file ko open krne ke liye open functons ka use krenge
# fir open functions ke andr hum pass krenge filekoaur , aur mode ko ki kis mode me open krna chahte hen jese yahan hai r means read mode same hota hai write mode
# NOte:- agar data file same folder me nhi rhega tb hume uska path pass krna hoga
#  python hamesha Current working directory me search krta hai jo ki yahan pr aiml hai esilye aiml me ye sample.txt search krega by defaults

f = open("01.Python_Basics/6.Fundamentals-05/sample.txt", "r") #file object ke form me ye open krega dat ako esilye f chahiye refernce ke liye
# f = open("01.Python_Basics/6.Fundamentals-05/sample.txt", "w")
# abb hum uss data pr koi bhi operations kr skte huen using f
data = f.read()
print(data)
# print(type(data)) # string

f.close() 


# write()  functions- Overwrite the all the ata but read mode se write mode krna hoga
# f.write("This is my first sample file operations")

# -==============With Keyword======================
# ------we have to run close() function to close that file when reading or writing

# So, now with keyword help in so that we have not fixed to write close()
with open("01.Python_Basics/6.Fundamentals-05/sample.txt", "r") as f:
    print(f.read())


# -============Delete file fucntins=================
# first improt os module
import os
os.remove("sample.txt")