#WRITE A PROGRAM TO DISPLAY A/B WHERE A AND B ARE INTEGERS WHERE  IF B=0 DISPLAY INFINITE BY DISPLAYING ZERO ERROR

a=5
try:
    b=int(input("enter your value for b"))
    c=int(a)/int(b)
    print(c)
except ValueError:
    print("error") 
except ZeroDivisionError:
    print("infinite") 
else:
    print("try block is executed")          
    
    
    