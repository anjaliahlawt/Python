# #write a program to check the number is odd or even 

# n=int(input("enter the number"))
# if n%2==0:
#     print(f"number is even {n}")
# else:
#     print(f"number is odd {n}")



# #write a program to find greatest of 3 number


# a=int(input("enter the number 1")) 
# b=int(input("nter tge value of number 2"))
# c=int(input("enter the value of number3"))
# # if a>b and a>c:
# #  print(a)
# # elif b>a and b>c:
# #    print(b)
# # else:
# #    print(c)

# print(max(a,b,c))



# #write a program if a number is multiple of 7 or not
 
# num=int(input("enter the number"))
# if num%7==0:
#     print(f" this no. multiple of 7 {num}")
# else:
#     print(f"this is not multiple of 7 {num}")


# # write a program to user enter theri 3 favourite movies and store them in list

# mov1=input("enter movie1 name ")
# mov2=input("enter movie2 name ")
# mov3=input("enter movie3 name ")

# movies=[]
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# movies1=[mov1,mov2,mov3]
# print(movies1)



#wap to check if the list contains a palindrome of element

# list=["a",3,3,"a"]
# copylist=list.copy()
# copylist.reverse()
# if(copylist==list):
#  print("palindrome number")
# else:
#    print("not palindrome number")



# a=input("enter the number")
# if a==a[::-1]:
#     print("palindrome no")
# else:
#     print("not palindrome")


#search number x in the tuple using loop

t=(1,2,3,4)
s=5
found=False
for i in t:
    if(s==i):
        found=True
        
if found:
    print("number found")
else:
    print("number not found")   
   