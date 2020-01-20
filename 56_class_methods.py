# since we require class variable to change class variables...we can do on ething we can create class  methods which even the insance
# variables can change and we even dont rquire self..we require cls

class Employee:
    no_of_leaves=89

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name} and salary is {self.salary} and a job is {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves

harry=Employee("Harry",456,"instructor")
rohan=Employee("Rohan",900,"Manager")

a=harry.printdetails()
print(a)
rohan.change_leaves(71)
print(rohan.no_of_leaves)


