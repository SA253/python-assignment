# using pass keyword just to use the function without anything
def add():
    pass
print("hello namaste")



#positional argument   ---single * ---class is tuple
def add(*args):    
    print(type(args))
    print(args)
add(1,2)
add(1,2,3)
add(1,2,3,4)
print("hello world")


#positional argument
def add(*args):    
    sum=0
    for x in args:
        sum+=x
    print(args,sum)
add(1,2)
add(1,2,3)
add(1,2,3,4)
print("hello world")



#var length keyworded argument   -----double**  --class is dict
def sayhi(**wards):
    print(type(wards),wards)
sayhi(name1="sachin")
sayhi(name1="sachin",name2="saurav")
sayhi(name1="sachin",name2="saurav",name3="rahul")


#generic functions(mixture of both positional and keyworded)
def sayhi(*args,**wards):
    print(args,wards)
    #print(type(wards),wards)
sayhi(name1="sachin")
sayhi(1,name2="saurav")
sayhi("baby",name2="saurav",name3="rahul")

