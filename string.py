#STRING

#1.string is a sequence of characters and it is immutable (cannot be changed) and it is a collection of characters enclosed in single quotes('') or double quotes("").

name="anjali"
print(name)
name="anjali's"
print(name)
string="""
        my name is anjali
        and i am from meerut
        complted mca
        """
print(string)

#using for lopp print string
name="shlawat"
for i in name:
    print(i)

#Acess characetr
print(name[0])

#length of string
print(len(name))

#concentaion of string
fisrt_name="anjali"
last_name="ahlawat"
print(fisrt_name+" "+last_name)

#slicing:accessing a part of string
str='anjali ahlawat'
print(str[1:5])
print(str[2:len(str)])

#negative index in slicing
str2="programming"
print(str2[-1:-5:-2])

#methods of string

str3="coding"
print(str3.upper())
print(str3[1:4])
# print(str3.lower())
# print(str3.strip()) #remove space strt and end
# print(str3.replace("c","j"))
# print(str3.startswith("co"))
# print(str3.find("g"))
# print(str3.count("n"))
# str4="cat"
# str4="f"+str4[1:]
# print(str4)
# print(str2[::-1])
        