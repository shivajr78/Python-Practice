
# #************************ Single Inheritance ********************

# class Employee:                         #Base or parent Class
#     company = "Microsoft"

#     def showDetails(self):
#         print("He is an Softwar Engineer")

# class Programmer(Employee):             #Child or Derived Class
#     language = "Python"
#     company = "Google"
    
#     def getlanguage(self):
#         print(f"The language he used {self.language}")

#     def showDetails(self): #over writed function
#         print("He is an Softwar Engineer")

# e = Employee()
# e.showDetails()
# p = Programmer()
# p.showDetails()    #Employee class is now base class of programmer class
# p.getlanguage()
# print(p.company)


# #************************ Multiple Inheritance *****************

# class Employee:
#     company = "Microsoft"
#     eCode =  124

# class Freelancer:
#     company = "Visa"
#     level  = 0

#     def upgradeLevel(self):
#         self.level = self.level+1

# class programmer(Employee,Freelancer): #here first class that class get first parioty
#     name = "Shiva"

# p = programmer()
# p.upgradeLevel()
# print(p.company)

#************************ Multilevel Inheritance ****************

class Person:
    Country = "India"
    def takeBreak(self):
        print("I am Breathing...")

class Employee(Person):
    company = "MicroSoft"
    def getSalary(self):
        print(f"Salary is {self.salary}")


    def takeBreak(self):
        print("I'm an Employee, So i take rest...")

class Programmer(Employee):
    company = "Google"

    def getSalary(self):
        print(f"No Salary to Programmer!")

    def takeBreak(self):
        print("I'm an Programmer, So i take rest++...")

p = Person()
p.takeBreak()
e = Employee()
e.takeBreak()
pr = Programmer()
pr.takeBreak()
print(pr.company)
print(pr.Country)