try:
    i = int(input("Enter the number:"))
    c = 1/i

except Exception as e:
    print(f"Please Enter Vaild Value as Exception is Occur {e}")
    exit() #@


finally: #return conclution of code
    print("We are Done!")
    

print("Thankyou for using the code....")