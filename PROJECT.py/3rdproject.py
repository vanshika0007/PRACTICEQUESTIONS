#MAKING SECRET CODE LANGUAGE 

def encoding(x):
    
    n=len(x)
    if len(x)<=3:
        for i in range(n):
            print(x[n-1-i],end="")
           
            
    else:
        
        c=(x[1:n])
            
        d=x[0]  
        f=str(input("input 3 number to add in front"))
        g=str(input("input 3 number to add at last"))
        concatenate =f+c+d+g          
        print(concatenate)
        
        
ans=encoding(str(input("enter the string which you want tha coding of:")))
print(ans)        