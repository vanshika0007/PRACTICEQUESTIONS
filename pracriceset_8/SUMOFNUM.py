# sum of n numbers using function
def sum(*numbers):
    sum=0
    for i in numbers: 
        sum=sum+i
    return sum    

c=sum(1,2,3,4,5,6,7)
print(c)