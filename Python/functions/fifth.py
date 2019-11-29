def outer(a):
    def inner(*arg,**kward):  #inner function is generic bcz we donot konw how many args we want
        print("inner function")
        print(type(a))
        a(*arg,**kward)    # demo1:this will call hello()  function    ,demo2: this time it calls hi() function
        print("inner function finished execution")
    return inner
@outer       # this is wrapperfunction  this is also called as decorator
def hello(name):
    print("hello "+name)
@outer    # this is wrapperfunction
def hi(name1,name2,name3):
    print("hi "+name1+" "+name2+" "+name3)   
hello("sachin")
#hi("sachin","saurav")  # here it is tuple,dict=0  ---arg=tuple,kward=dictonary
#or
hi(name2="sachin",name1="saurav",name3="rahul") #dictonary,tuple=0




def allstrings(a):
    def inner(*arg,**kward):  #inner function is generic bcz we donot konw how many args we want
        for i in arg:
            if type(i)!=str:
                print("invalid args")
                break
        else:
            for i in kward.values():
                if type(i)!=str:
                    print("invalid args")
                    break
            else:
                a(*arg,**kward)
    return inner
@allstrings       # this is wrapperfunction  this is also called as decorator
def hello(name):
    print("hello "+name)
@allstrings    # this is wrapperfunction
def hi(name1,name2,name3):
    print("hi "+name1+" "+name2+" "+name3)   
hello("sachin")
#hi("sachin","saurav")  # here it is tuple,dict=0  ---arg=tuple,kward=dictonary
#or
hi(name2="sachin",name1="saurav",name3="rahul") #dictonary,tuple=0
hi(1)
hello(True)