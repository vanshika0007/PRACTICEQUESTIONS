# print pattern-  * * * * *
                # * * * * *
                # * * * * *
                # * * * * * 
                # * * * * *

rows=int(input("enter the number"))
for i in range(rows):
    for j in range(rows):
        print("*",end=" ")
    print("")