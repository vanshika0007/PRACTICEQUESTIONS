#string length in a given list  if string lenght in 2 or more and first and last char is same

def strlen(list):
    matching=0
    for item in list:
        if (len(item)>=2 and item[0]==item[-1])  :
            matching=matching+1
    return matching        
             
c=strlen(["vans","kans","hello","oopso"]) 
print(c) 
             
                
    