
#filtering
obj=[
    {"team":"india","fname":"sachin","lname":"tendulkar"},
    {"team":"india","fname":"saurav","lname":"gangauly"},
    {"team":"india","fname":"dhoni","lname":"ms"},
    {"team":"australia","fname":"sachin","lname":"tendulkar"},
    {"team":"australia","fname":"saurav","lname":"gangauly"},
    {"team":"australia","fname":"dhoni","lname":"ms"}
    ]
def myfilter(el):
    return el["team"]=="india"
newobj=filter(myfilter,obj)
print(type(newobj))
for i in newobj:
    print('{fname} {lname}'.format(**i))
    
    
    
    
def myfilter(el):
    return el["fname"].startswith("s")
newobj=filter(myfilter,obj)
print(type(newobj))
for i in newobj:
    print('{fname} {lname}'.format(**i))