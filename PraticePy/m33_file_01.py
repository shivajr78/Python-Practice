def greet(name):
    print(f"Good Morning,{name}")

print(__name__) # it will print file name where function are using
if __name__ == "__main__": #if we function in other file.so this requried don't run this much of funtion in that file
    n = input("Enter the Name : ")
    greet(n)
