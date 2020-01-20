# def square(x):
#     return x*x
# def cube(x):
#     return x*x*x
# func=[square,cube]
# for i in range(5):
#     val=list(map(lambda x:x(i),func))
#     print(val)

# # filter:


# def greater_tha_5(num):
#     return num>5

# lst=[4,5,6,7,8,9]


# is_great=list(filter(greater_tha_5,lst))
# print(is_great)
lst=[4,5,6,7,8,9]

def divi(num):
    return num%2==0                 #prints the numbers who satisfy this...map gives true false for it

is_div=list(filter(divi,lst))
print(is_div)

#REDUCE:

# lst1=[4,5,6,7,8,9]
# num=0
# for item in lst1:
#     num=num+item
#     print(num)


from functools import reduce
lst1=[4,5,6,7,8,9]
num=reduce(lambda x,y:x+y,lst1)
print(num)


lst1=[4,5,6,7,8,9]
num=reduce(lambda x,y:x*y,lst1)
print(num)















