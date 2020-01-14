# list1=["Harry","Larry","Carry","Marry"]
#
# for items in list1:
#     print(items)
#
# list1 = [   ["Harry",1] , ["Larry",2] , ["Carry",3] , ["Marry",4] ]
#
# for items,books in list1:
#     print(items, "and books are",books)


# print("If we typecast in dictionary")
# dict1=dict(list1)
#

# for items,books in dict1.items():
#     print(items,"and books are",books)
#


items=[int,float,"Harry",9,56,78,54,"Darry"]

for item in items:
    if str(item).isnumeric() and item>6:
      print(item)