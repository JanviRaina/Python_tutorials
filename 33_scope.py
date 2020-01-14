l=10  #  global
def function1(n):
    l=5    #local
    print(l)    # first finds in local..if not then global
    print(n,"i hv printed")
function1("this is me")
print(l)    # can't access local variables here
print("explaination for next :")
# WE CANT CHANGE GLOBAL VARIABLES IN LOCAL SCOPE
# TO CHANGE,WE DO THIS :
m=10  #  global
def function2(n1):
    global m
    m=m+7
    print(m)
    print(n1,"i hv printed")
function2("this is me")
print(m)




