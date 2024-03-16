#PROGRAM TO DISPLAY A/B WHERE A AND B ARE INTEGERS,IFB=0 DISPLAY INFINITE BY HANDLING THE ZERO DIVISION ERROR

a=input("enter the a numbers:")
b=input("enter the b numbers:")

try:
    c=int(a)/int(b)
    print(c)
except ZeroDivisionError:
    print("INFINITE")  
except ValueError:
    print("different literal")    