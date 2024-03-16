#MAKING KAUN BANEGA CROREPATI PROJECT

points=0
list=[['question1','answer1','answer2','answer3','answer4'],['question2','answer1','answer2','answer3','answer4']
      ,['question3','answer1','answer2','answer3','answer4']]
for i in list:  
    for j in i:                                       # agar mujhe list k sndar list ko acees krna hai toh print(list[1][2])
        print(i[0])
        x=i[0]
        if x=="question1":    
                print("options for",i,"question are:")
                print("1:answer1,2:answer2")
                print("3:answer3,4:answer4")
                num=int(input("enter your number"))
                d=i[num]
                if d==i[2] and i[num]=="answer2":
                    print("correct answer")
                    points+=1000
                    break
                else:
                    print("wrong answer")  
                    break  
                    
        elif x=="question2":    
                print("options for",i,"question are:")
                print("1:answer1,2:answer2")
                print("3:answer3,4:answer4")
                num=int(input("enter your number"))
                d=i[num]
                if d==i[2] and i[num]=="answer2":
                    print("correct answer")
                    points+=2000
                    break
                else:
                    print("wrong answer") 
                    break 
                    
        elif x=="question3":    
                print("options for",i,"question are:")
                print("1:answer1,2:answer2")
                print("3:answer3,4:answer4")
                num=int(input("enter your number"))
                d=i[num]
                if d==i[2] and i[num]=="answer2":
                    print("correct answer")
                    points+=4000
                    break
                else:
                    print("wrong answer") 
                    break
                    
        else:
                print("no more question")          
            
           
print("total points:",points)        