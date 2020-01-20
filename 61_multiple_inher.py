# class CoolProgrammer(Employee,Player):
class Employee:
    no_of_leaves=89

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name} and salary is {self.salary} and a job is {self.role}"


class Player:
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printdetails(self):
        return f"The name is {self.name} and sport is {self.game} "

class CoolProgrammer(Employee,Player):
    pass



harry=Employee("Harry",678,"trainer")
rohan=Employee("Rohan",90,"dancer")
shubham=Player("Shubhnam",['cricket','football'])
arti=CoolProgrammer("ARTI",6790,"coolprogy")
det=arti.printdetails()
print(det)
