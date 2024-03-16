#WRITE A PROGRAM TO PRINT THE 3RD ,5TH ,7TH element from the list using enumerated function
input_list=[]
for i in range(10):
     c=(input("enter the list"))
     input_list.append(c)
print(input_list) 

for i,item in enumerate(input_list,start=1):
    if i==3:
        print(f"{i}:{item}")   
    elif i==5:
        print(f"{i}:{item}")   
    elif i==7:
        print(f"{i}:{item}") 
    else:
        print()    
                  