# a set with two same vallue but different literals(diff. data type)

num=set()
n=int(input(" enter the number of items you want"))

for i in range(n):
    int_value=int(input("enter the int value"))
    str_value=input("enter the str value")
    num.add((int_value,str_value))                   #hamne tuple------>(int_value,str_value) ko set k andar pass kardia ek argument banakar bcz add ek element 
    
    
                                                     #ko hi add krta h
print(num)