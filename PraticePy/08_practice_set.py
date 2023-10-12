# #Q1

# def greater_iter(num1,num2,num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3

# g = greater_iter(2,45,222)
# print("The greater is", +g)

# #Q2
# #°F = °C × (9/5) + 32

# def freh(cel):
#     return (cel * (9/5)) + 32 

# f = freh(45)
# print("The frehrehit temperature is ",f)

# #Q4

# print("Hello Vivek",end = " ")
# print("Hello Rahul",end = " ")
# print("Hello Rinku",end = " ")

# #Q5

# def factorial_recursive(n):
#     return n*((n+1)/2)

# f = factorial_recursive(6)
# print(f)

# #Q6

# n = 6
# for i in range(n):
#     print("*" * (n-i))

# #Q7
# def convert_iter(inch):
#     return (inch * 2.54)

# c = convert_iter(5)
# print(c)

#Q8
# this = "        Harry is a good coder           "
# print(this)
# print(this.strip())

# def remove_and_strip(string,word):
#     newStr = string.replace(word,"")
#     return newStr.strip()

# line = "               Harry was a good coder                 "
# new = remove_and_strip(line,'was')
# print(new)

#Q9
def table_recursive(num):
    for i in range (1,11):
        print(num*i)

table_recursive(12)
