#wrapping,closures 
#wrapping:-to use the same business logic again and again we use wrapper functions
def outer(a):
    print("outer function")
    def inner():
        print("inner function")
        print(type(a))
        a()    # demo1:this will call hello()  function    ,demo2: this time it calls hi() function
        print("inner function finished execution")
    return inner
def hello():
    print("hello world")
def hi():
    print("hi world")   
#demo1=outer(hello)   #demo1,demo2 are inner functions here
#demo2=outer(hi)   #here outer is wrapping both hello() and hi()
#demo1()
#demo2()
#or
hello=outer(hello)    #---- output is same instead of using 2 more classes we use sameone 
hi=outer(hi)
hello()
hi()  


# another way of using wrapper
def outer(a):
    print("outer function")
    def inner():
        print("inner function")
        print(type(a))
        a()    # demo1:this will call hello()  function    ,demo2: this time it calls hi() function
        print("inner function finished execution")
    return inner
@outer       # this is wrapperfunction  this is alos called as ""decorator""
def hello():
    print("hello world")
@outer    # this is wrapperfunction
def hi():
    print("hi world")   
#hello=outer(hello)    ---- output is same instead of using 2 more classes we use sameone 
#hi=outer(hi)
hello()
hi()  