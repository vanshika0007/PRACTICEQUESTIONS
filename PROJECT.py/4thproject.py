#GUESSING A RANDOM NUMBER PROJECT

a=int(input("enter number from range:"))
b=int(input("enter number towhich range:"))
list1=[]
n=3 # number of turns given to a user
chance=0

for i in range(a,b+1):
    list1.append(i)
    
import random
computer_choice=random.choice(list1) 
print(computer_choice) 

for i in range(n):
    user_input=int(input("enter your choice"))
    if a<= user_input <=b:
        if computer_choice==user_input:
            print("correct choice")
            break
        else:
            print("wrong choice")
            chance+=1                                                                  
            if chance==3:
                print("you lost!")
    else:
        print("your choice is out of range")      
        
    

  
    