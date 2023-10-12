try:
    i = int(input("Enter the number:"))
    c = 1/i

except Exception as e:
    print(f"Please Enter Vaild Value as Exception is Occur {e}")

else: # this will run as try function run and if exception fun run than else does not run
    print("We Were Sucessfull!")

print("Thankyou for using the code....")