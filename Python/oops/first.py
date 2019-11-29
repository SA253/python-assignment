"""import second
obj=second.person()"""
#encapsulation at object level
class person:
    pass
obj=person()
print(type(obj))

obj.fname="sachin" #object level encapsulation
obj.lname="tendulkar"
print(obj.fname,obj.lname)


obj2=person()
print(type(obj2))

obj2.fname="rahul" #object level encapsulation
obj2.lname="dravid"
obj2.team="india"
print(obj2.fname,obj2.lname,obj2.team)



# encapsulation at class level
class person1:
    team="india"
obj=person1()
print(type(obj))

obj.fname="sachin" #object level encapsulation
obj.lname="tendulkar"
print(obj.fname,obj.lname,obj.team)


obj2=person1()
print(type(obj2))
obj2.fname="rahul" #object level encapsulation
obj2.lname="dravid"
print(obj2.fname,obj2.lname,obj2.team)





#mixed of all
class person2:
    team="ind"
obj=person2()
print(type(obj))

obj.fname="sachin" #object level encapsulation
obj.lname="tendulkar"
obj.team="austria"

obj2=person2()
print(type(obj2))
person.team="austra"
obj2.fname="rahul" #object level encapsulation
obj2.lname="dravid"
print(person2.team)
print(obj.fname,obj.lname,obj.__class__.team)
print(obj2.fname,obj2.lname,obj2.__class__.team)