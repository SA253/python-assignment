class person:
    team="india"
    def sayhi(s):
        print("hi "+s.fname+" "+s.lname)
    def __init__(o,f,l):
        o.fname=f
        o.lname=l
def demo():
    print("this.demo")
data="hello world"

#print("inside first: ",__name__)  # it tells the name of the imported file
if __name__=="__main__":
    print("Hiiiiiiiiiiii")
    print("Hiiiiiiiiiiii")
    print("Hiiiiiiiiiiii")