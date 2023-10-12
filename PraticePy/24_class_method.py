class Employee:
    company = "MicroSoft"
    salary = 80000
    location = "Hyderabad"

    # def changeLocation(self,New):
    #     self.__class__.location = New

    @classmethod
    def changeLocation(cls,New):#used to change the entry in obj class
         cls.location = New

e = Employee()

print(e.location)
e.changeLocation('New Delhi') 
print(e.location)

