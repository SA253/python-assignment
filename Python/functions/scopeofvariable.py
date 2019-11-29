#global variable

data="hello world"
def demo():
    print(data)
demo()


#local variable loses scope when the function completes execution
"""def demo():
    data1="hello"
demo()
print(data1)   #error is name "data1" is not defined" bcz scope is not available outside the function
"""

def demo():
    print("hello world")
test=demo() # return of demo is passed ie, there is no return of demo so ans is 'NoneType' object is not callable
test=demo  # reference of demo is passed
print(type(test))
test()