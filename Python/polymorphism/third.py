class box:
    def __init__(self,itemlist):
        self.itemlist=itemlist
    def __str__(self):
        return str(self.itemlist)
    def __add__(self,other):
        newitems=self.itemlist+other.itemlist
        b=box(newitems)
        return b
    def __lt__(s,o):
        return len(s.itemlist)<len(o.itemlist)
b1=box(["item1","item2"])
b2=box(["item3","item4","item5"])
b3=b1+b2
print(b1)
print(b2)
print(b3)
print(b1>b2)