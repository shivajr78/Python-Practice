# #Q1

# class Programmer:
#     company = "Microsoft"

#     def getDetails(self):
#         print(f"The Employee Name : {self.name}")
#         print(f"The Employee salary: {self.salary}")
#         print(f"The Employee subunit : {self.product}")


# info = Programmer()
# info.name =  "Shiva"
# info.salary = 80000
# info.product = "Skype"
# info.getDetails()

# #Q2

# class Calculator:
#     def __init__(self, num):
#         self.number = num

#     @staticmethod
#     def greet():
#         print("Hello!")

#     def square(self):
#         print(f"The square of {self.number} is : {self.number **2}")
#     def cube(self):
#         print(f"The cubic of {self.number} is : {self.number **3} ")
#     def squareRoot(self):
#         print(f"The squareRoot of {self.number} is : {self.number // 2} ")

# a = Calculator(16)
# a.square()
# a.cube()
# a.squareRoot()
# Calculator.greet()

# #Q3

# class Sample():
#     a = "Shiva"

# obj = Sample()
# obj.a = "Aakash"  #Here we change the value

# #sample.a = "Harry" # to for change above a value

# print(Sample.a)  # return shiva that above declared
# print(obj.a)    # return Aakash that declare in obj

#Q5

class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"Train Name : {self.name}")
        print(f"Seats Availble : {self.seats}")

    def infoFare(self):
        print(f"Ticket price : Rs.{self.fare}")

    def bookTicket(self):
        if(self.seats > 0):
            print(f"Your Ticket has been Booked Sucessfully!,With Seat No.{self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry You can't Book the Ticket.As Seats are not availble!")


info = Train("02801-Pursotham Express",740,2)
info.getStatus()
info.bookTicket()
info.bookTicket()
info.bookTicket()
info.getStatus()
#info.infoFare()