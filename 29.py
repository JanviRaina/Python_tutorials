n=int(input("enter an integer"))
n1=int(input("enter an integer for t/f"))
b=bool(n1)


if b==True:
    for i in range (n):
        print("*"*i)
elif b==False:
    while(n>0):
        print("*"*n)
        n=n-1

