# #Q1
# def readFile(filename):
#     try:
#         with open(filename,"r") as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f"File {filename} is not found")

# readFile("1.txt")
# readFile("2.txt")
# readFile("3.txt")

# # Q2

# list = [9, 8, 1, 3, 6, 8, 2, 4, 7, 8]
# for index, item in enumerate(list):
#     if index == 2 or index == 4 or index ==6:
#         #print(index,item)
#         print(f"The {index+1}th Element is {item}")

# #Q3

# num = int(input("Enter the number: "))

# table = [num*i for i in range(1,11)]
# print(table)

# #Q4

# a = int(input("Enter num a : "))
# b = int(input("Enter num b : "))

# try:
#     print(a/b)
# except:
#     print("Infinite")

#Q5

num = int(input("Enter the number: "))

table = [num*i for i in range(1,11)]
print(table)
with open("tables.txt","a") as f:
    f.write(str(table))
    f.write('\n')