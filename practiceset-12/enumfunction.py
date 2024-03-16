#WRITE A PROGRAM THAT PRINT 1,3,7 ELEMENT FROM THE LIST USING ENUMERATE FUNCTION

list=[1,2,3,4,5,6,7,8]

for index,item in enumerate(list,start=1):
    if index==1:
        print(f"{index}:{item}")
    elif index==3:
        print(f"{index}:{item}")
    elif index==7:
        print(f"{index}:{item}")
    else:
        print