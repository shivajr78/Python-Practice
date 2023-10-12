a = 54 #Global Varible
def func1():
    global a # here said Print Gobal Varible
    print(f"Print Statement 1 : {a}")
    a = 8 #Local Varible
    print(f"Print Statement 2 : {a}") # if we not use global Varible

func1()
print(f"Print Statement 3 : {a}")