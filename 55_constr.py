class Employee:
    no_of_leaves=3
    def __init__(self,aname,asalary,ajob):
        self.name=aname
        self.salary=asalary
        self.job=ajob

    #this way func can be used for various objects
    def printdetails(self):
        return f"Name is {self.name} and salary is {self.salary} and role is {self.job}"

harry=Employee("Harry",567,"teacher")

print(harry.salary)
print(harry.printdetails)