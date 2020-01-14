# Lists are like arrays.Element accessed using index
# Syntax: ["", ""]
# for dictionary:
# d1={
#     "":"",
# }

# sort and reverse change original list

grocery=["Vim Bar",56,"juice","deodrant"]

print(grocery[3])
numbers=[1,2,21,80,9]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[1:3])
print(numbers[1:])
print(numbers[:])
print(numbers[1::2])
print(numbers)
# One below gives right ans only when first 2 are not provided
print(numbers[::-2])
print(len(numbers))
print(max(numbers))

num=[]
num.append(3)
num.append(7)
num.append(4)
num.append(70)
num.insert(1,50)
print(num)
num.remove(50)
print(num)
num.pop()
print(num)
num[1]=67
print(num)


# Immutable:Cannot Change
# Tuple is immutable

tp=(1,2,3,5)
print(tp)

#We can't change values like this
# tp[1]=9
# print(tp)

# for making tuple with single elment
tp1=(1,)
print(tp1)

# To swap 2 numbers
a=2
b=4
print(a,b)
a,b=b,a
print(a,b)
