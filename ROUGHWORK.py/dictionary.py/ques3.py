#USING LIST COMPREHENTION TO PRINT THE LIST WHICH CONTAIN THE MULTIPLICATION TABLE ENTERED BY THE USER

item=int(input("enter the number which u want table"))
list1=[]
for i in range(10):
    list1.append(item)

list2=[]
c=[i*item for i,item in enumerate(list1,start=1)]
list2.append(c)
print(list2)