# functions are the block of codes that perform a specific task
# Syntax: 
# def fnxname();

def hello(): #fnx definition
    print("hello")
    print("from python")
# call the functions
hello()
hello()


# ----------Sum fnx---------
def sum(a,b): #a and b are called the parameter
    s = a + b
    return s
ans = sum(4,5) #5,4 are called arguments
print(ans)


# --------AVerage value of 3 value--------
def printAverage(a,b,c):
    average = (a+b+c)/3
    return average
k = printAverage(3,4,5)
print(k)


# ----------Note:- Default Value in a function--------

#( non-default parameters, default parameter)
# example: (a,b= 1) -> (5) -> value agar sirf 5 pass kiya jaye toh a ko 5 milega aur b default me 1 ho jayega and if (5,6) arguments bheja gaya toh fir b ko 6 milega 1 nhi 

def Average(a,b=1):
    av = a+b/2
    return av
print(Average(5,6))









#==================Types of Functions================================================

# ----------Types= 2 types  =>1.built-in function    --> print(),input(),type(),range()
                            # =>2. user defined funtion       ---> khud logic likhte he

# Note:- ye sabhi "def " se use krte hen syntax hai 



# ----------Lambda functions-----> small operation me use krenge--------

# syntax: lambda a,b: a+b     =>a and b as an input lega aur fir a+b krke return krega fir uss return ko hum ek valriable me store kr skte hen

sum1 = lambda a,b: a+b
print(sum1(4,6))


avg = lambda a,b: (a+b)/2
print(avg(4,6))


# ------print factorial of N----------
def print_fact(n):
    fact = 1
    for i in range(1,n+1,1):
        fact = fact*i
    return fact
n = int(input("Enter the number to calculate fact: "))
print(print_fact(n))
