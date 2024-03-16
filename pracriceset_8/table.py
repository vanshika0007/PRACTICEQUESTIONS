# multiplication number of given table
def table(a):
    n=int(input("enter the number till whre you want ypur table"))
    for i in range(1,n+1):
        print(a,"x",i,"=",a*i)
        
b=table(int(input(" enter the number")))  
print(b)      