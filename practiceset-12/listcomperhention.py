#WRITE A LIST COMPREHRNTION TO PRINT ALIST WHICH CONTAIN THE MUJLTIPLICATION TABLE OF ENTER BY THE USER

num=int(input("enter the number"))
list1=[]
for i in range(1,11):
    list1.append(i)
print(list1) 

#type1
for i in list1:
  print(f" {i} x {num}={i*num}")


#type2
list2= [i*num for i in list1]  
c=list2
print(c)
    