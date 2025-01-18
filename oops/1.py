# Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer:
    company = "microsoft"
    def __init__(self,name,role,salary):    # constructor function to initialize the object values
        self.name = name
        self.role = role
        self.salary = salary

emp1 = Programmer("Nikhitha","SDE",200000)  # passing values to the constructor
print(emp1)
print(emp1.name)
print(emp1.role)
print(emp1.salary)
print(Programmer.company)
print(emp1.company)
    