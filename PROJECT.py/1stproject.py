#CREATING SNAKE GUN AND WATER PROJECT

import random
list=['snake','water','gun']
randomchoice_1=random.choice(list)
print("choice from computer",randomchoice_1)

n=int(input("enter the number of round you want to play"))
print(" choicefrom:snake,water,gun")

for i in range(n):
    userschoice_1=str(input("choice"))
    match userschoice_1:
        case "snake":
            if(randomchoice_1=="water"):
                print("you won!")
            elif(randomchoice_1=="gun"):
                print("you lost!")  
            else:
                print("match with draw!") 
            
        case "water":
           if(randomchoice_1=="snake"):
               print("you won!")
           elif(randomchoice_1=="gun"):
               print("you lost!")  
           else:
               print("match with draw!") 
                       
        case "gun":
            if(randomchoice_1=="snake"):
                print("you lost!")
            elif(randomchoice_1=="water"):
                print("you won!")  
            else:
                print("match with draw!")
            
        case other:
            print("you have not given any input")
         
         
                 
                       
