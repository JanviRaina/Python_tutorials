s_from_list=set([1,2,3,4])
print(s_from_list)

l=[4,8,9,0]
s=set(l)
print(s)
print(type(s))

s1=set()
s1.add(1)
print(s1)
s1.add(7)
print(s1)
s1.add(7)
s1.add(2)
print(s1)
s1.add(0)
print(s1)

#arranges in sorted manner and an element can occur only once in a set
#Other things like UNION INTERSECTION DISJOINT SETS ETC:
# Our set is {0,1,2,7}

b=s1.union({8,9,7})

print(b)

b1=s1.intersection({8,9,7})

print(b1)

print(max(s1))

print(b1.isdisjoint(s1))

s1.remove(7)

print(b1.isdisjoint(s1))
