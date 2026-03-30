# #function: is a block of code which perform a specific task and it is reusable and it is defined by def keyword and it can take input and return output.


def greet():
    print("heelo")
greet()

#function with parameter

def sum(a,b):
    s=a+b
    return s
print(sum(2,3))

def even(a):
    if(a%2==0):
        print("number is even")
    else:
        print("not even no")
even(15)   

#default  paramter

def mult(a=5):
    s=a*1
    print(s)
mult() 

#multiple arguments

def sub(a,b,c):
    s=a-b-c
    return s
print(sub(8,1,2))

#  global variable
x = 10  

def test():
    print(x)

test()

#local variable
def fun():
  y=24
  print(y)
fun()
  
#global keyword

z=12
def cn():
 global z
 z=23
 print(z)
cn()
print(z)

# *args is used to pass a variable number of arguments to a function. It allows you to pass any number of arguments to a function, and they will be treated as a tuple.

def add(*args):
    s=0
    for i in args:
        s+=i
    return s
print(add(1,4,2,3))


# **kwargs is used to pass a variable number of keyword arguments to a function. It allows you to pass any number of keyword arguments to a function, and they will be treated as a dictionary.
def info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
info(name="Anjali",age=24,city="pune")

## lambda function is an anonymous function which is defined by lambda keyword and it can take any number of arguments but it can only have one expression.
square=lambda x:x*x
print(square(5))

print((lambda x,y:x+y)(3,4))