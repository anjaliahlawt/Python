
#sets: is a collection of unique elements and it is mutable (can be changed) and it is unordered collection of items.


s={1,2,3,2}
print(s)
nums=set() # empty set
print(nums)

#methods

set={1,2,3,4}
set.add(5) # add element
print(set)
set.remove(3) #remove the element
print(set)
#set.clear() #empty the set
#print(set)
set.pop() #  remove random value
print(set)
set1={4,5,6}
print(set.union(set1)) #combine both values
print(set.intersection(set1)) #retrun comon value