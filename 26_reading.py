f=open("#26_janvi.txt")
content=f.read(3)
print(content)
content=f.read(6)
print(content)
f.close()
# f=open("#26_janvi.txt","rb")
# content=f.read()
# print(content)

"""
TO READ LINE BY LINE
 for line in f:
     print(line,end="")
print(f.readline())
TO get ALL LINES IN LIST:
print(f.readlines())
"""


