
#LIST:like array but same type of data store in java/c/c++ and we store any type of data in list


#1.create list

l=[1,2,3,4]

#2.aceess element

print(l[0])

#3.change value(list is mutable)

l[0]=3
print(l[0])

#4.diffrent data types store in list


l1=[1,"anjali",3]
l1[2]="anjau"
print(l1)
print(len(l1))

#5 methods

nums=[1,2,3,"anjali"]
nums.append(4) # add data end
print(nums)
nums.insert(2,5) #add element at specfic index
print(nums)
nums.remove(3) #remove element by value
print(nums)
nums.pop(3) #remove element by index and also we cannot writ value so it remove last element by default
print(nums)
print(1 in nums)

nums2=[1,9,67,23]
#nums2.sort() #sort the element in list but it change the original list
print(nums2)
new=sorted(nums2) # create new list and sort the element in new list
print(new)



#slicing :kuch part find krna end value not included 

nums1=[1,2,3,4]
print(nums1[1:])
print(nums1[:3])
print(nums1[-1])
print(nums1[1:3:2])
print(nums1[::-1])
