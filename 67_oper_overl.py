class Employee:
    def __init__(self,name,salary,place):
        self.name=name
        self.salary=salary
        self.place=place
    def printdetails(self):
        return f"the name is {self.name} and salary is {self.salary} and place is {self.place} ."
    def __add__(self,other):
        return self.salary+other.salary
    def __truediv__(self,other):
        return self.salary/other.salary

Rohan=Employee("rohan",180,"mumbai")
Karan=Employee("karan",90,"delhi")


print(Rohan+Karan)
print(Rohan/Karan)



# str and repr copy it from code