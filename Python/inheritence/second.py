#multilevel inheritence
class person:
    nationality="india"
    def sayhi(p):
        print("hi "+p.fname+" "+p.lname)
    def __init__(k,fname,lname):
        k.fname=fname
        k.lname=lname
        
class employee(person):
    org="DXC"
    def __init__(k,fname,lname,dept,loc):
       #super().__init__(fname,lname)
        person.__init__(k,fname,lname)
        k.dept=dept
        k.loc=loc
    def work(o):
        print(o.fname+" is working")
class manager(employee):
    
    def __init__(k,fname,lname,dept,loc,reportees):
        employee.__init__(k,fname,lname,dept,loc)
        k.reportees=reportees
    def manage(self):
        print(self.fname+" is managing")
e1=manager("sharmila","chowdary","ECE","bangalore",[])
e1.sayhi()
e1.work()
e1.manage()
print(e1.__dict__)
print(e1.org,e1.nationality)
print(employee.__bases__)  #this show the parent of employee class
print(person.__bases__)     #this show the parent of person class



#hierarchial inheritance
class person1:
    nationality="india"
    def sayhi(p):
        print("hi "+p.fname+" "+p.lname)
    def __init__(k,fname,lname):
        k.fname=fname
        k.lname=lname
        
class employee1(person1):
    org="DXC"
    def __init__(k,fname,lname,dept,loc):
       #super().__init__(fname,lname)
        person1.__init__(k,fname,lname)
        k.dept=dept
        k.loc=loc
    def work(o):
        print(o.fname+" is working")
class student(person1):
    institute="python university"
    def __init__(self,fname,lname,stream):
        person1.__init__(self,fname,lname)
        self.stream=stream
    def study(self):
        print(self.fname+" is studying")
e1=student("sharmila","chowdary","sports")
e1.sayhi()
e1.study()
print(e1.__dict__)


#
class person1:
    nationality="india"
    def sayhi(p):
        print("hi "+p.fname+" "+p.lname)
    def __init__(k,fname,lname):
        k.fname=fname
        k.lname=lname
        
class employee2(person1):
    org="DXC"
    def __init__(k,fname,lname,dept,loc):
       #super().__init__(fname,lname)
        person1.__init__(k,fname,lname)
        k.dept=dept
        k.loc=loc
    def work(o):
        print(o.fname+" is working")
class student1(person1):
    institute="python university"
    def __init__(self,fname,lname,stream):
        person1.__init__(self,fname,lname)
        self.stream=stream
    def study(self):
        print(self.fname+" is studying")
class intern(student1,employee2):
    def __init__(self,fname,lname,dept,loc,stream):
        student1.__init__(self,fname,lname,stream)
        employee2.__init__(self,fname,lname,dept,loc)
    def interns(self):
        print(self.fname+" is intern")
e1=intern("sharmila","chowdary","ece","bangalore","sports")
e1.sayhi()
e1.work()
e1.study()
e1.interns()
print(e1.__dict__)
