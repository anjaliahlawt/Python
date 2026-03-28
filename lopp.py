
 #conditional statements
age=21
if age>20:
 print('eligible')
elif age==20:
 print('just elgible')
else:
 print('not elgible')    





#LOOPS

#1.for loop
for i in range(5):
 print(i)  

 for i in range(2,5):
  print(i)

for i in range(2,6,1):
   print(i)

   #2 while loop

   j=0
   while j<=5:
     print(j)
     j=j+1

     #LOOP CONTROL

     #1.break
j=12
while j>=2:
       if(j==5):
         break
       print(j)
       j=j-1
#2.continue:doubt
j=11
while j>=4:
    if j==6:
      j-=1
      continue
    
    print(j)
    j-=1
