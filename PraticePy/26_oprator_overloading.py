class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets Add")
        return self.num + num2.num

    def __mul__(self, num3):
        print("Lets Multiply")
        return self.num * num3.num


n1 = Number(6)
n2 = Number(3)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)
