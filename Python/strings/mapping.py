obj=[22,32,19,43]
def mymap(el):
    return 32+el*9/5
newobj=map(mymap,obj)
print(type(newobj))
for i in newobj:
    print(i)