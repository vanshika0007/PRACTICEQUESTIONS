info={"hello":"world","how":"you"}

print(info["hello"])
print(info.get("hello"))
print(info.values())
print(info.keys())
print(info.items())

for i in info.keys():
    print(info[i])
    
    
    