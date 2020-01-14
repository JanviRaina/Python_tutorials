# FIBONACCI SERIES
# def fibo(n):
#     first = 1
#     second = 1
#     i=2
#     print(first,second,end="")
#     while(second<n):
#         next_term=first+second
#         print(next_term, end="")
#         first = second
#         second=next_term
#         i=i+1
#
# fibo(5)


# RECURSIVE APPROACH

def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    n=n-1
print(fibo(6))






