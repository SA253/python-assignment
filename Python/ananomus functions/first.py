#anonymous function
#inline function
#lambda function

"""
rule:1
function should contain only 1 line
rule:2
that 1 line should be return statement
"""
# it doesnot contain any name,return keyword is not required,add lambda in front

#type1
data=(lambda n1,n2:"hi "+n1+" "+n2)("sachin","saurav")
print(data)



#type2
hello=lambda n1,n2:"hi "+n1+" "+n2
print(type(hello))
print(hello("a","b"))
print(hello("c","d"))
print(hello("e","f"))


#example1
hi=lambda a,b: a+b
print(hi(1,2))


#example2  --mapping
obj=[22,32,19,43]

newobj=map(lambda el:32+el*9/5,obj)
print(type(newobj))
for i in newobj:
    print(i)
    
    
#example3 --sorting
obj=[{
    "fname":"sachin",
    "lname":"tendulkar",
    "city":"mumbai"
    },
    {
    "fname":"sharmila",
    "lname":"chowdary",
    "city":"anantapur"
    },{
    "fname":"saurav",
    "lname":"gangauly",
    "city":"bengal"
    }]
obj.sort(key=lambda el:el["fname"])
print(obj)


#example4 =   ---filtering
obj=[
    {"team":"india","fname":"sachin","lname":"tendulkar"},
    {"team":"india","fname":"saurav","lname":"gangauly"},
    {"team":"india","fname":"dhoni","lname":"ms"},
    {"team":"australia","fname":"sachin","lname":"tendulkar"},
    {"team":"australia","fname":"saurav","lname":"gangauly"},
    {"team":"australia","fname":"dhoni","lname":"ms"}
    ]
newobj=filter(lambda el:el["team"]=="india",obj)
print(type(newobj))
for i in newobj:
    print('{fname} {lname}'.format(**i))