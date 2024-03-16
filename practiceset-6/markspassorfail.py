#program to check wheather a student is pass or fail in class exam condition-40% total 33% in each exam total 3 subject
marks_1=int(input(" enter the1 number "))
marks_2=int(input(" enter the 2number  "))
marks_3=int(input(" enter the3 number "))
total_1=int(input("enter the number out of which 1st is numberd"))
total_2=int(input("enter the number out of which 1st is numberd"))
total_3=int(input("enter the number out of which 1st is numberd"))
total=total_1+total_2+total_3
firstper=(marks_1/total_1)*100
secondper=(marks_2/total_2)*100
thirdper=(marks_3/total_3)*100
total_percentage=((marks_1+marks_2+marks_3)/total)*100

if((total_percentage>40)and( firstper>=33)and(secondper>=33)and(thirdper>=33)):
    print("pass!")
else:
    print("fail!")
    
