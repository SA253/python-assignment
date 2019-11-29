def demo():
    print("hello")
    
def caller(a):
    print(type(a))
    print("inside the caller")
    a()
caller(demo)

#nested function
def outer():
    print("outer")
    def inner():
        print("inner")
    inner()
outer()