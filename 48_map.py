# map,filter and reduce:
# syntax:    map(function,list)

# def cub(a):
#     return a*a*a

# lst=[4,5,6,7,8,9]
# cube=list(map(cub,lst))
# print(cube)

# lst=[4,5,6,7,8,9]
# sq=list(map(lambda x:x*x,lst))
# print(sq)



lst=["4","5","6","7","8","9"]
sq=list(map(lambda x:int(x),lst))
print(sq)


