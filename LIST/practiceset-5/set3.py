s=set()
s.add(5)
s.add("5")
s.add(5.56)
print(len(s))
print(s)


for item in s:
    print(type(item))
