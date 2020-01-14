def sum(a,b):
    print(a+b)
sum(8,9)
def func1(c,d):
    average=(c+d)/2
    return average
print (func1(8,9))

# DOCSTRINGS:used to understand what we had taken in function

def func2(str):
    """  this is a docstring"""
    print(str, "I am function")

func2("hello")
print(func2.__doc__)