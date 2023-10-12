# #Q.1

# num = int(input("Enter the number: "))
# for i in range(1,11):
#     print(str(i*num))

# #Q.2

# l1 = ["Harry","Sohan","Sachin","Rahul"]

# for name in l1:
#     if name.startswith('S'):
#         print("Hello "+name)

# #Q.3

# i = 1
# while i<10:
#     print(i)
#     i = i+1
#     if(i==5):
#         break

# #Q.4

# num = int(input("Enter the number : "))
# prime = True 
# for i in range(2,num):
#     if(num % i == 0 and num != 2):
#         prime = False
#         break
# if prime:
#     print("This is an prime Number")
# else:
#     print("Not a prime number")

# #Q.6
# num = int(input("Enter the number : "))

# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial * i
# print(f"The Factorial of {num} is {factorial}")

# #Q.5
# n = int(input("Enter the number : "))

# sum = 0
# for i in range(1,n+1):
#     sum = sum + i

# print(f"The Sum of first {n} is {sum}")

# #Q.8

# n = 4

# for i in range(5):
#     print("*" * (i+1))

# #Q.7
# n = 3
# for i in range(3):     #for Rows
#     print(" " * (n-i-1),end = "")
#     print("*" * (2*i+1),end = "")
#     print(" " * (n-i-1))

# #Q.9

# n = 3
# for i in range(3):     #for Rows
#     print("*" * (i),end = "")
#     print("*" * (i-1),end = "")
#     print("*" * (i+1),)

num = int(input("Enter the number: "))
for i in range(1,11):
    table = str(i*num)
    