#PRINT
print("""Anjali 
      ahlawat
       softwrae 
      developer
      """)
name="anjali"
age=22
print(type(name))

#conditional statements
if age>20:
 print('eligible')
elif age==20:
 print('just elgible')
else:
 print('not elgible') 


#class
class Student:
  name='anjali'
  age=20
  language="c,java"

stu = Student()
print(stu.age)
 
#with function inside class
#used self keyword to access the variable inside the class wihout self keyword we cannot access the variable inside the class.
class Person:
 def greet(self):
  print("heelo shina")
p = Person()
p.greet()

# underscore variable declareation  is before the variable name and it is used to indicate that the variable is intended for internal use only and should not be accessed from outside the class or module. It is a convention in Python to use a single underscore before a variable name to indicate that it is intended for internal use. However, it does not prevent access to the variable from outside the class or module, it is just a convention to indicate that it should not be accessed.ern
_my=20
print(_my)

a,b=6,2
c=a/b # gives the float value(exact value)
c=a//b # gives the integer value (flor division) closest integer(which is lesser than or equal)
print(c)

#taking input from user
 
name=input("name: ")
print(name)
age=int(input("age: "))
print(type(age))

# for loops

#for i in range(5):
 #print(i)

for i in range(1,10,2):
  print(i)
#while loop

i=10
while i>=5:
 print(i)
 i -=1

# string
name="anjali"
print(name[0])
for ch in name:
 print(ch)
 print(len(name))