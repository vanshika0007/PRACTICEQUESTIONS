# print pattern-  1
#                 2 2
#                 3 3 3
#                 4 4 4 4
#                 5 5 5 5 5
             
num=int(input(" enter the number"))
for i in range(num):
    for j in range(i+1):
        print(i,end=" ")
    print("")    
            
