"""

a=int(input("enter the number1"))
b=int(input("enter the number2"))
div=a/b
print("data:",div)
print("hello world")



#exceptional handling
try:
    k=int(input("enter the number3"))
    l=int(input("enter the number4"))
    division=k/l
    print("data:",division)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:  # this is for when string/character is used
    print(e)
print("hello world")


#multiple errors
try:
    k1=int(input("enter the number"))
    l1=int(input("enter the number"))
    division=k1/l1
    print("data:",division)
except (ZeroDivisionError,ValueError) as e:
    print("please enter non zero numeric value")
    print(type(e))
except Exception as e:
    print("generic handler")
print("hello world")


#
try:
    names=["sachin","saurav","rahul"]
    name=input("enter the name: ")
    if name not in names:
        raise Exception("name no tfound")
    print("welcome "+name)
except (ZeroDivisionError,ValueError) as e:
    print("please enter non zero numeric value")
    print(type(e))
except Exception as e:
    print("generic handler")
print("some other important task")

"""

#creating our own exception
class NameNotFound(Exception):
    def __int__(self,msg="name not found"):
        Exception.__init__(self,msg)

class PassNotFound(Exception):
    def __int__(self,msg="password not found"):
        Exception.__init__(self,msg)


try:
    names={"sachin":"icci","saurav":"bcci","rahul":"bbc"}
    name=input("enter the name: ")
    password =input("enter the password")
    if name not in names:
        raise NameNotFound
    print("welcome "+name)
    if names[name] is not password:
        raise PassNotFound
except Exception as e:
    print(e)
print("some other important task")