

#class: is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

# class Student:
#     name="anjali"
#     age=20
#     grade="A"

# s1= Student()
# print(s1.name)
# print(s1.age)


#method 2

class Student:
    name="anjali"
    age=20
    grade="B"
    def display(self):
        print(self.name,self.age,self.grade)

s1= Student()
s1.display()