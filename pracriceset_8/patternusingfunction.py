# following pattern using function * * *
                                #  * *
                                #  *

def pattern(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end="")
        print()    
        
a=pattern(int(input("enter the number")))  
print(a)                            