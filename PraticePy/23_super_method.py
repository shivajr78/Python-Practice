class Person:
    Country = "India"

    def __init__(self):
        print("Initialzing Person...\n")
    
    def takeBreak(self):
        print("I am Breathing...")

class Employee(Person):
    company = "MicroSoft"

    def __init__(self):
        super().__init__()
        print("Initialzing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")


    def takeBreak(self):
        super().takeBreak()
        print("I'm an Employee, So i take rest...")

class Programmer(Employee):
    company = "Google"

    def __init__(self):
        super().__init__()
        print("Initialzing Programmer...\n")

    def getSalary(self):
        print(f"No Salary to Programmer!")

    def takeBreak(self):
        super().takeBreak()
        print("I'm an Programmer, So i take rest++...")

#p = Person()

#e = Employee()

pr = Programmer()

#############################################
# class Employee:

#     def __init__(self,aname,aage,asalray):
#         self.name = aname
#         self.age = aage
#         self.salary = asalray

# shiva = Employee("Harry",24,80000)
# print(shiva.age)