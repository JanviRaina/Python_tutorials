                    #     a
                    #    / \
                    #    b  c
                    #     \/
                    #     d
class A:
    def met(self):
        print("this is method of A ")
class B(A):
    def met(self):
        print("this is method of B ")
    
class C(A):
    def met(self):
        print("this is method of C ")
class D(C,B):
# class D(B,C):
    pass

a=A()
b=B()
c=C()
d=D()

d.met()