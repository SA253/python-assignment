#basic
class person:
    nationality="india"
    def sayhi(p):
        print("hi "+p.fname+" "+p.lname)
    
class employee(person):
    org="DXC"
    def work(o):
        print(o.fname+" is working")
e1=employee()
e1.fname="sharmila"
e1.lname="chowdary"
e1.sayhi()
e1.work()
print(e1.org,e1.nationality)




#reusability,constructor overridding
class person2:
    nationality="india"
    def sayhi(p):
        print("hi "+p.fname+" "+p.lname)
    def __init__(k,fname,lname):
        k.fname=fname
        k.lname=lname
        
class employee2(person):
    org="DXC"
    def __init__(k,fname,lname,dept,loc):
        k.fname=fname
        k.lname=lname
        k.dept=dept
        k.loc=loc
    def work(o):
        print(o.fname+" is working")
e1=employee2("sharmila","chowdary","ECE","bangalore")
e1.sayhi()
e1.work()
print(e1.__dict__)
print(e1.org,e1.nationality)



#by using calling the constructor or constructor chaining
class person1:
    nationality="india"
    def sayhi(p):
        print("hi "+p.fname+" "+p.lname)
    def __init__(k,fname,lname):
        k.fname=fname
        k.lname=lname
        
class employee1(person):
    org="DXC"
    def __init__(k,fname,lname,dept,loc):
       #super().__init__(fname,lname)
        person1.__init__(k,fname,lname)
        k.dept=dept
        k.loc=loc
    def work(o):
        print(o.fname+" is working")
e1=employee1("sharmila","chowdary","ECE","bangalore")
e1.sayhi()
e1.work()
print(e1.__dict__)
print(e1.org,e1.nationality)
print(employee.__bases__)
print(person.__bases__)