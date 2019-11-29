astring="hello world"
print(len(astring))
print(astring.index("o"))
print(astring.index("o",5))
print(astring.index("o",5,8))
print(astring.count("l"))
print(astring.upper())
print(astring.lower())
print(astring.startswith("hello"))
print(astring.endswith("d!"))
words=astring.split(" ")
print(words)
print(astring.find("o"))
print(astring.find("o",5))
print(astring.find("o",5,7))
print(astring.replace("world","python"))




#format functions1
data=" i am a {0} from {1}"
sub1="string"
lang="python"
print(data.format(sub1,lang))
temp="""hello {fname} {lname} , welcome to {city} """
dataString=temp.format(fname="sachin",lname="tendulkar",city="mumbai")
print(dataString)



#format functions2
data=" i am a {0} from {1}"
sub1="string"
lang="python"
print(data.format(sub1,lang))
temp="""hello {fname} {lname} , welcome to {city} """
obj=[{
    "fname":"sachin",
    "lname":"tendulkar",
    "city":"mumbai"
    },
    {
    "fname":"sharmila",
    "lname":"chowdary",
    "city":"anantapur"
    }]
for i in range (len(obj)):
    dataString=temp.format(**obj[i])
    print(dataString)
    
    #or
for i in obj:
    dataString=temp.format(**i)
    print(dataString)