#splitting the list,set,tuple,dict
def sayhi(n1,n2,n3):
    print("hi "+n1+" "+n2+" "+n3)
li=["sachin","saurav","rahul"]
s={"sachin","saurav","rahul"}
t=("sachin","saurav","rahul")
d={
    "n1":"sachin",
    "n2":"saurav",
    "n3":"rahul"
    }
print("list")
sayhi(*li)
print("set")
sayhi(*s)
print("tuple")
sayhi(*t)
print("dict")
sayhi(*d.values())