# iterable: __itr__() or __getitem__()    //if we run these functions on an object it returns an iterator

# iterator: __next__()                    //iterators is an object in which  this function is defined

# iteration:the procedure of iterating

# generators are that type of iterators which can be traversed only one time

for i in range(6):
    print (i)
    # generates on the fly..its not that it is already stored..can be checked by keeping number large like 6000



def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = 546546                                            # integer can't...gives error
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
