def harry():
    x=20
    def rohan():
        global x
        x=88
    print("before calling rohan() ", x)
    rohan()
    print("after calling rohan() ", x)
harry()    # 20 # 20
print(x)   # 88          since there is nthg. in global ..it creates its own global and makes it 88
# THIS HAPPENS BECAUSE ON MAKING IT GLOBAL,IT DOESNT GO OUT OF NESTED...IT GOES ON TOP TO FINF=D GLOBAL
x1=89
def harry1():
    x1=20
    def rohan1():
        global x1
        x1=88
    rohan1()
    print("after calling rohan1() ", x1)
harry1()    # 20
print(x1)   # 88