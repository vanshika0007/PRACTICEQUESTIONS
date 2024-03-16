
# l=[1,"harry",2,'c',9]
# m=[3,"vanshika",9.8]
# k=l+m
# print(k)
# print(l.count(9))


# a=(5 ,6,6,7,8)
# print(a[0:2])    


 #a=list(input("enter the elements in list"))       #ye hamara sring ki trh input lega even space ko bhi
#print(a)                                          # split use krane se eelement char m nhi store hote string m hote 


# def last(n):
#     return(n[-1])


# def sort_list_last(tuples):
#     # Sort the list of tuples 'tuples' using the 'last' function as the key for sorting
#     return sorted(tuples,key=last)

# # Call the 'sort_list_last' function with a list of tuples as input and print the sorted result
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))     




# Months ={"January","February", "March", "April", "May", "June"}
  
# print(Months)    
  
# months2={"July","August","September","October"} 
# Months.update(months2);    
   
# print(Months);  -


# Frozenset = frozenset((1,2,3,4,5)) 
# print(type(Frozenset))    





# info={"hello":"world","how":"you"}
# print(info.values())
# print(info.keys())
# for i in info.keys():
#     print(info[i])
    
tuple1=(1,2,3,4,5)
list1=list(tuple1)
list1.extend((4,5,6,7))
tuple2=tuple(list1)
print(tuple2)
 