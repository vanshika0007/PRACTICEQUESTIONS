# largest among the numbers
def max_min(list):
    max=list[0]
    for item in list:
        if max<item:
            max=item
            
    return max    
            
            
a=max_min([0,2,3,1,9,0])  
print(a)