class person:
    team="india"
    def sayhi(p):
        print("hi "+p.fname+" "+p.lname)
obj=person()
print(type(obj))
obj.fname="sachin" #object level encapsulation
obj.lname="tendulkar"

obj2=person()
obj2.fname="rahul" #object level encapsulation
obj2.lname="dravid"
person.sayhi(obj)
person.sayhi(obj2)
obj.sayhi()
obj2.sayhi()
