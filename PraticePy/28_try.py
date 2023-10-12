while(True):
    print("Press q to quit")
    a = input("Enter Your Number : ")
    if a == 'q':
        break

    try: #if input is string it try once than go to except function
        print("Trying...")
        a = int(a) #converting input from string form to int form
        if(a>6):
            print("a is greater than 6")
    
    except Exception as e:  #it will output the reason of error but does crash your program
         #it is used to display the reason why error is thrown
        print(f"your output resulting an error because : {e}")

print("Thanks for playing the Game")