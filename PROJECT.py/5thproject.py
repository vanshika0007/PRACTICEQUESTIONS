#GAME TO GUESS THE LETTER OF WORDS IN GIVEN CHANCES

list1=['vanshika','harry','hellomy']
import random
word=random.choice(list1)
print(word)
list2=['']*(len(word)-1)

chances=len(word)+2
print("enter only single letter at a time ")
for i in range(chances):
    user_input=(input("enter your letter   ").lower())
    if (len(user_input))==1 and user_input.isalpha():
        if user_input in word:
            index=word.find(user_input)   
            print(f"index available at{index}")
            list2.insert(index,user_input)
            print(list2)
        else:
            print("not avaialable")    
    else:
        print("you entered more than 1 letter")  
        
        
c=','.join(list2) 
print(c)  
if c==word:
    print("you won")
else:
    print("you lost")    
