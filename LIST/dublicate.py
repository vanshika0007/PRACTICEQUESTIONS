#remove dublicate element from list


def dublicate(list):
    list_1=[]
    for item in list:
        if item not in list_1:
            list_1.append(item)
            
    return list_1

c=dublicate(["vanshi","kansal","vanshi","hello"])
print(c)
