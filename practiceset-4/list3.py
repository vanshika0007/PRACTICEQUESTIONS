#sum of list of 4 numbers

a=int(input("enter  the number"))
list_3=[]
for i in range(a):
    print("enter the",i+1,"number")
    a=int(input(""))
    print(list_3.append(a))
print("the list all the number is:",list_3)
    
add=0
for i in list_3:
    add+=i

print("addition of all numbers are:",add)