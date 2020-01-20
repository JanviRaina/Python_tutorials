# class Programmer(Employee):
class Employee:
    no_of_leaves=89

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name} and salary is {self.salary} and a job is {self.role}"

class Programmer(Employee):
    def __init__(self,aname,asalary,arole,alanguages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.languages=alanguages

    def printprog(self):
        return f"The Programmer's name is {self.name} and salary is {self.salary} and a job is {self.role} and languages are {self.languages}"

harry=Employee("Harry",456,"instructor")
rohan=Employee("Rohan",900,"Manager")
karan=Programmer("karan",346,"proggy",["python,"cpp"])
shubh=Programmer("karan",124,"gamer","java")
print(karan.printprog())
print(karan.printdetails())


#we will use super later