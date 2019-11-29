class A:
    def sayhi(self):
        print("hi from A")
class B(A):
    def sayhi(self):
        print("hi from B")
class C(B,A):
    pass
e=C()
e.sayhi()
