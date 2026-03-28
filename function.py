 #function: is a block of code which perform a specific task and it is reusable and it is defined by def keyword and it can take input and return output.


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