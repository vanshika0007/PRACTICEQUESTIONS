# english translation of hindi word and option to look after the items by the user


dic={"namaste":"hello","kaiseho":"how are you","tata":"bye"}
print(dic.items(),"\n")


for i in dic.keys():
    a=input("enter the key u want the value")
    print(dic.get(a))
    
    
    
# dic = {"namaste": "hello", "kaiseho": "how are you", "tata": "bye"}
# print(dic.items(), "\n")

# for i in dic.keys():
#     a = input("Enter the key you want the value: ")
#     print(dic.get(a))