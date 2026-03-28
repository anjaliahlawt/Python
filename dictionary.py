#DICTIONARY:is a collection of key value pairs and it is mutable (can be changed) and it is unordered collection of items.and not allowed duplicate keys

student={
    "name":"anjali",
    "age":22,
    "subjects":{
        "c":2,
        "java":21,

    }

}
print(student)
print(student["subjects"]["java"])
student["name"]="anju"


print(len(student))
print(list(student)) # type casting of dictionary into list
print(list(student.values()))

#methods

print(student.keys()) #retrun all keys 
print(student.values()) #retrun all values
print(student.items()) #retrun all key value pair as tuples
print(student.get("name")) # retrun keys accoridng to value
student.update({"city":"meerut"})# add new key value pair in dictionary and also upadteexisting value
student.update({"age":"20"})
print(student)
v=student.pop("age") #(doubt)
print(v)
print(student)
del student["subjects"] #(doubt)

#loops
  
Employee={
    "name":"anjali",
    "sallery":12,
    "department":"it"
}
for j in Employee: # retrun both key and value
    print(j,Employee[j])
for i in Employee.values(): # retrun only values
    print(i)
for i ,j in Employee.items():# retrun both key and value
    print(i,j)