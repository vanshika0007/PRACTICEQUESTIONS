list=['hi','bye','namaste']
index=0 
while(index<=len(list)):
    print(list)
    for i in list:
        print(i)
    for j in i:
        print(j)    
    index=index+1
    print("\n")
else:
    print("loop end")    