# to find out given number is prime or not
num=int(input("enter the number"))
if(num==1):
    print("prime")
for  i in range(2,num):
    if(num%i==0):
        print("not prime")
        break    
else:
    print("prime")
