# #Q2

# name = input("Enter the Name : ")
# marks = input("Enter the Marks : ")
# phone = input("Enter the Phone Number : ")

# a = "The name of Student is {}, his marks are {} and Phone number is {} ".format(name,marks,phone)
# print(a)

# #Q3
# #list must be string so, converted it by str(i*7)

# l = [str(i*7) for i in range(1,11)]

# a = "\n".join(l)  
# print(a)

# #Q4
# def Divisible_by_5(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False

# l = [5,11,13,20,26,30,35,55,95,99,110,155,225]

# print(list(filter(Divisible_by_5,l)))

#Q5
from functools import reduce
l = [1,2,4,5,0,7]

a = reduce(max,l)
print(a)