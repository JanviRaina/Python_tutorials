# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         self.email=f"{fname}.{lname}@codewithharry.com"
    
#     def explain(self):
#         return f"the cmployee is {self.fname} {self.lname}"
#     def printemail(self):
#         pass

# emp1=Employee("emp1","sharma")
# emp2=Employee("emp2","raina")

# emp1.fname="janu"

# print(emp1.email)                 email doesnt change

#this problem is solved by setter
# the code below works using email func
# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         # self.email=f"{fname}.{lname}@codewithharry.com"
    
#     def explain(self):
#         return f"the cmployee is {self.fname} {self.lname}"
#     def email(self):
#         return f"{self.fname}.{self.lname}@codewithharry.com"

# emp1=Employee("emp1","sharma")
# emp2=Employee("emp2","raina")

# emp1.fname="janu"

# print(emp1.email())



# Now using setters

class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@codewithharry.com"
    
    def explain(self):
        return f"the cmployee is {self.fname} {self.lname}"
    def email(self):
        return f"{self.fname}.{self.lname}@codewithharry.com"

emp1=Employee("emp1","sharma")
emp2=Employee("emp2","raina")

emp1.fname="janu"

print(emp1.email())

