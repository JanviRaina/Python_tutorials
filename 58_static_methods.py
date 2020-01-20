class Employee:
    no_of_leaves=89

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name} and salary is {self.salary} and a job is {self.role}"

# packing inside class...static methods are like normal methods but are made inside class.We need them only to access objects
#  so we prefer to keep them inside class.
    @staticmethod
    def printgood(string):
        print("this is good",string)
        return 45

harry=Employee("Harry",456,"instructor")
rohan=Employee("Rohan",900,"Manager")
harry.printgood("janvi")          
print(rohan.printgood("everyone"))



