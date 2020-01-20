"""def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum
a=funcret(0)
b=funcret(1)

print(a)
print(b)"""
# a function can return a function as well as take function as argument

# def executor(func):
#     func("hello")

# executor(print)

def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec