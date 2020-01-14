#dictionary combination of keys and values

d1={}
print(type(d1))

d1={
    "car":"ferrari",
    "name":"jeff bezoz",
    "company":"amazon",
    "eats":"baingan"
}
print(d1["name"])
print(d1["company"])
d2={
    "sneha":"poha",
    "janvi":"idli",
    "nikhil":{"breakfast":"egg","lunch":"daal","dinner":"roti"}
}
print(d2["nikhil"]["lunch"])

d2["nikhil"]["dinner"]="kebabs"

print(d2)

d1["name"]="jack"

del d1["company"]
print(d1)

#     d3=d2
#     better:
#     d3=d2.copy()   because it creates copy.Above one creates only reference.On deleting one both delete for d3=d2.Copy better.

d3=d2.copy()
print("the copy is :")
print(d3)

#print(d2.get("harry"))
d2.update({"Ankit":"Orange"})
print(d2)
print(d2.keys())
print(d2.values())


# d3={
# "madhura":{"lunch":"poha","dinner":"daal"},
# "janvi":{"breakfast":"poha","lunch":"rice","dinner":"roti"},
# "karuna":"kebabs",
# "nishi":"ice-cream"
# }
# print(type(d3))
# print(d3["nishi"],end=" and janvi ate ")
# print(d3["janvi"]["dinner"])

















