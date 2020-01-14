#  CODE FOR FACTORIAL:
# ITERATIVE
# n=int(input("enter a number whose factorial you want"))
# fact=1
# for i in range(n):
#     i=i+1
#     fact=fact*i
# print(fact)

# RECURSIVE


def factorial(n):
    if  n==1:
        return 1
    return n*factorial(n-1)

print(factorial(4))
factorial(4)