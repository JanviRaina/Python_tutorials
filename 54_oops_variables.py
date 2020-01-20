# To explain the difference between class and instance variables:
class Employee:
    no_of_leaves=3                   #this is class variable
    pass

harry=Employee()
sarry=Employee()

harry.name="Harry"
harry.salary=345
harry.job="cook"

sarry.name="Sarry"
sarry.salary=678
sarry.job="instructor"

# can be accessed using employee,harry and sarry
print(harry.job)
print(harry.no_of_leaves)
print("employees'leaves",Employee.no_of_leaves)

#for changing..we can only change using Employee>>we cannot change class variables using instance variables
print(harry.__dict__)
harry.no_of_leaves=9
print(harry.__dict__)

print(harry.no_of_leaves)
print("Employee's leaves after changing leaves from harry",Employee.no_of_leaves)

Employee.no_of_leaves=6
print(Employee.no_of_leaves)
print(harry.no_of_leaves)