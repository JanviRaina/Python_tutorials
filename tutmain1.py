# import sklearn
# suppose these are some imp functions:
def printy(string):
    return f"This is my name {string}"

def add(a,b):
    print(a+b)

print("and the name is",__name__)               #name's value is main only when running in same1

if __name__ == "__main__":
    print(printy("janvi"))
    add(2,4)