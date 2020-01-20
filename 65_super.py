class A:
    classvar1="I am class variable in class A"
    def __init__(self):
        self.var1="I am in class A's constructor"
        self.classvar1="I am in instance var in A"

class B(A):
    classvar1="I am class variable of class B"

a=A()
b=B()

print(b.classvar1)             # First looks for instance variable in B and then an instance variable from the class from which it is inheriting 
                               # and then goes for class variable in its own and then in the class from which it inherits

                               #if sth. gets overwrite that doesnt run...so if we overwrite A's method in B and then comment half of B then it
                               #will not look for instance variable in A