# can ypu chnage the value of  alist which contain in a set
#s={8,7,12,"harry",[1,2]}
s1={8,7,12,"harry",(1,2)}       #tuple banalenge varna list error dega kyuki vo mutable hota h
 
for item in s1:
    if (1,2) in s1:
        s1.remove((1,2))
        s1.add((2,1))
        
print(s1)        