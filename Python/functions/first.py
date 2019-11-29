def sayhi():
    print("hi all")
    
sayhi()
sayhi()
sayhi()

#parameterized
def sayhello(name1,name2,name3):
    print("hi  "+name1+" "+name2+" "+name3)
sayhello("sachin","saurav","hello")
    
    
    
  #return type  
def sayhello(name1,name2):
    return("hi  "+name1+" "+name2)
data=sayhello("sachin","saurav")
print("Data:",data)



#positional
def sayhello(name1,name2,name3):
    print("hi  "+name1+" "+name2+" "+name3)
sayhello(name2="sachin",name1="saurav",name3="hello")



#mixture of positional and keyword
def sayhello(name1,name2,name3):
    print("hi  "+name1+" "+name2+" "+name3)
sayhello("sachin",name3="saurav",name2="hello")