#multiplication table 
#using for loop
table=int(input(" enter the number for which u want the table"))
for i in range(10):
    print(table, "X", i+1,"=",table*i+1)
    i=i+1
    
    
    
#using while loop
table=int(input("enter the number"))
i=0
while (i<=10):
    print(table,"x",i,"=",table*i)
    i=i+1