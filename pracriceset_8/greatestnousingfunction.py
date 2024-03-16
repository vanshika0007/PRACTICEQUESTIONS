#finding the gretest number among three number using function
def greatest(a,b,c):
    if((a>b) and(a>c)):
        print("a is greter among all")
    elif((b>a)and(b>c)):
        print("b is greter among all") 
    else:
        print("c is greter")       
        
greatest(2,4,9)        