# n1 = int(input("Enter the number 1 : "))
# n2 = int(input("Enter the number 2 : "))
# n3 = int(input("Enter the number 3 : "))
# n4 = int(input("Enter the number 4 : "))

# if(n1>n2 and n1>n3 and n1>n4 ):
#     print("The Greater Number is Number 1 that is ",n1)

# elif(n2>n1 and n2>n3 and n2>n4 ):
#     print("The Greater Number is Number 2 that is ",n2)

# elif(n3>n2 and n3>n1 and n3>n4 ):
#     print("The Greater Number is Number 3 that is ",n3)

# elif(n4>n2 and n4>n3 and n4>n1 ):
#     print("The Greater Number is Number 3 that is ",n3)

# #Q2
# sub1 = int(input("Enter the marks : "))
# sub2 = int(input("Enter the marks : "))
# sub3 = int(input("Enter the marks : "))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("You are Fail Due to less marks in a subject ")

# elif(sub1 + sub2 + sub3)/3 < 40 :
#     print("You are Fail due to Total Percentage is less than 40% ")

# else:
#     print("Congarualtion! You Pass the exam")

# #Q3
# text = input("Enter the text : ")

# if("make a lot of money" in text):
#     spam = True

# elif("buy now" in text):
#     spam = True

# elif("subscribe this" in text):
#     spam = True

# elif("click this" in text):
#     spam = True

# else:
#     spam = False

# if(spam):
#     print("This is an Spam")

# else:
#     print("Not a Spam")\

# #Q4
# letter = input("enter the user name : ")

# print(len(letter))

# if(len(letter)<10):
#     print("Short")
# else:
#     print("Long")

# #Q5
# Names = ["Shiva","Vinay","Sanju","Mahesh","Ajay","Vijay"]
# Name  = input("Enter the username: ")

# if(Name in Names):
#     print("We have your user id")

# else:
#     print("Not Found")

# #Q6

# Marks = int(input("Enter your total marks : "))

# if(Marks > 90):
#     print("Excellent!")
# elif(Marks > 80):
#     print("Grade : A")
# elif(Marks > 70):
#     print("Grade : B")
# elif(Marks > 60):
#     print("Grade : C")
# elif(Marks > 50):
#     print("Grade : D")
# else:
#     print("Fail!")

#Q7

post = ''' Harry is good coder. Harray had a youtube channel that is 
what called codewithharray. and love access his course playlist'''

print(post.find("Harry"))

