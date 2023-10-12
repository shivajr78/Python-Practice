
# def percent(marks):
#     return (sum(marks)/300)*100


# marks1 = [45,70,66,71]
# percentage1 = percent(marks1)

# marks2 = [51,59,62,74]
# percentage2 = percent(marks2)

# print(percentage1 , percentage2)

# #Quick quiz

# def wish():
#     return "Have a Good Day"

# print("Shiva "+wish())

# def wish(name,Roll):
#     return print("Have a Good Day "+ name + Roll)

# def sum(sum1, sum2):
#     return sum1 + sum2

# wish("Harry ",'008')

# s = sum(24,6)
# print(s)


################ Default parameter value

def greet(name = "Shiva"):  #function take default here
    return print("Have a Good day "+name)
greet() #When nothing pass to function