try:
    a = int(input("Enter the Number : "))
    c = 1/a

    print(c)

except ValueError as e: #this will run if you enter Char or String form 
    print("Please Enter a Valid Value")
    print(e)

except ZeroDivisionError as e:  #this will run if you enter invaild int
    print("Make sure you don't divide by Zero ")    
    print(e)

print("Thanks for using this code!")