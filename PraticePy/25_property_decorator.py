class Employee:
    company = "MicoSoft"
    Salary = 5600
    SalaryBonus = 400

    @property               #-->Getter function
    def totalSalary(self):
        return self.Salary + self.SalaryBonus  #Total Salary is Return

    @totalSalary.setter     #-->Setter function
    def totalSalary(self,value):
#Here this func calculate Bonus form given output total salary     
        self.SalaryBonus = value - self.Salary

e = Employee()
print(e.totalSalary)
e.totalSalary =  5800   # Provide Output total Salary to user
print(e.Salary)         #Salary from output total salary is return
print(e.SalaryBonus)    #Bonus from output total salary is return

