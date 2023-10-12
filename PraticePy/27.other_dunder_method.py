class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets Add")
        return self.num + num2.num

    def __mul__(self, num3):
        print("Lets Multiply")
        return self.num * num3.num

    def __str__(self): #Directly print the object cls element
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 1        #By default returing

n = Number(6)
print(n)

print(len(n))