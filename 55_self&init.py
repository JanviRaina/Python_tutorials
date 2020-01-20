class Employee:
    no_of_leaves=3
    #this way func can be used for various objects
    def printdetails(self):
        return f"Name is {self.name} and salary is {self.salary} and role is {self.job}"


harry=Employee()
sarry=Employee()

harry.name="Harry"
harry.salary=345
harry.job="cook"

sarry.name="Sarry"
sarry.salary=678
sarry.job="instructor"


print(sarry.printdetails())