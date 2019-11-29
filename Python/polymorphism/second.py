class person:
    nationality="india"
    def sayhi(p):
        print("hi "+p.fname+" "+p.lname)
    def __init__(k,fname,lname,cost):
        k.fname=fname
        k.lname=lname
        k.cost=cost
    def __int__(self):
        return len(self.fname)+len(self.lname)
    def __str__(self):
        return '{fname}' '{lname}'.format(**self.__dict__)
    def __bool__(self):
        return bool(self.fname) and bool(self.lname)
    def __float__(self):
        return ((self.cost)/5)
p1=person("sachin","tendulkar",12)
print(int(p1))
print(p1) # this is for string
print(float(p1))
print(bool(p1))