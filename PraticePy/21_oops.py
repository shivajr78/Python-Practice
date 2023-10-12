# a = 12
# b = 16

# print("The Sum of a and b is",a+b)


# class Number:
#     def sum(self):
#         return self.a + self.b

# num = Number()
# num.a = 12
# num.b = 16
# s =  num.sum()
# print(s)



# class RailwayForm:         #class or uh can say Application

#     #formType = "ReservationForm"

#     def printData(self):     #obj is an instantiation in class
#         print(f"The Name : {self.name}")
#         print(f"The Train :{self.train}")

# shivaApplication = RailwayForm()      #object or uh can details
# shivaApplication.name = "Shiva.jr" 
# shivaApplication.train = "Pursotham Express"

# RailwayForm.printData(shivaApplication)


# class Empolyee:
#     company = "Google"
#     salary = 1000

# Shiva = Empolyee()
# Vinay = Empolyee()

# Shiva.salary = 50000
# Vinay.salary = 40000

# print(Shiva.company)
# print(Vinay.company)

# Empolyee.company = "Microsoft" #changing by using class name
# print(Shiva.company)
# print(Shiva.salary)
# print(Vinay.company)
# print(Vinay.salary)

# ############ FOR Self Parameter ###########

# class Employee:
#     company = "Microsoft"

#     @staticmethod #it is used run without use of self in function but it not run with self
#     def greet():
#         print("Good morning! Shiva")

#     def getsalary(self,signature): #Here self is just adopt the value which is given by below function
    
#         print(f"Salary in {self.company} is upto {self.salary}\n{signature}")


# Shiva = Employee()
# Shiva.salary = 100000
# Shiva.greet()
# Shiva.getsalary("Thanks!")  #Employee.getsalary(Shiva)


############ FOR Constructor ################

class Employee:
    company = "Microsoft"

    def __init__(self,name,salary,subunit): #Automatically Run the function
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is Created!")


    def getDetails(self):
        print(f"The Empolyee Name : {self.name}")
        print(f"The Empolyee Salary : {self.salary}")
        print(f"The Empolyee Subunit : {self.subunit}")

Shiva = Employee("Shiva","80k","Software Engineer")
Shiva.getDetails()
