

#class: is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

# class Student:
#     name="anjali"
#     age=20
#     grade="A"

# s1= Student()
# print(s1.name)
# print(s1.age)


#method 2

# class Student:
#     name="anjali"
#     age=20
#     grade="B"
#     def display(self):
#         print(self.name,self.age,self.grade)

# s1= Student()
# s1.display()


#construtor:is a special method that is automatically called when an object of a class is created. It is used to initialize the attributes of the object.

# class Student:
#     def __init__(self):
#         print("constructor call")

# s1=Student()


class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=student("anju",20)
print(s1.name)

#without contsructor

class Student:
    pass

s1 = Student()
s1.name = "Anjali"   # manually dena padta hai 
