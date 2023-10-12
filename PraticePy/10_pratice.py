# #Q1

# class C2dVec:
#     def __init__(self,i,j):
#         self.icap = i   #--> eq 1
#         self.jcap = j   #--> eq 2\

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"


# class C3dVec(C2dVec):
#     def __init__(self,i,j,k):
#         super().__init__(i,j) #calling eq 1 & 2 by function
#         self.kcap = k

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
# v2d = C2dVec(2, 4)
# v3d = C3dVec(3, 6, 9)

# print(v2d)
# print(v3d)


# #Q2 Multilevel Inheritance

# class Animal:
#     animalType = "Mammal"

# class Pets:
#     colour = "White"

# class Dog:
#     @staticmethod
#     def bark():
#         print("Bow Bow!!")

# d = Dog()
# d.bark()



# #Q3

# class Employee:                      # formula for Salary Increment :
#     company = "MicroSoft"          #salaryAfterIncrement = salary*increment
#     salary  =  4000
#     increment = 1.5

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary * self.increment

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,sai):   # sai = salaryAfterIncrement
#         self.increment = sai/self.salary


# e = Employee()
# print(e.salaryAfterIncrement)
# print(e.increment)   # return old increment
# e.salaryAfterIncrement = 1000   # Giving new salary
# print(e.increment)   # return new increment acc to given Salary


# #Q4    Complex number (a+bi)(c+di) = (ac-bd) + (ad+bc)i

# class Complex:

#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i

#     def __add__(self,c):
#         return Complex(self.real + c.real , self.imaginary + c.imaginary)

    
#     def __mul__(self,c):
#         mulReal = self.real * c.real - self.imaginary * c.imaginary #(ac-bd)
#         mulImg = self.real * c.imaginary + self.imaginary * c.real  #(ad+bc)i
#         return Complex(mulReal,mulImg)

#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"   #formula for adding to complex number 


# c1 = Complex(3, 2)
# c2 = Complex(1, 7)

# print(c1 + c2)
# print(c1 * c2)

# #Q5
# class Vector:
#     def __init__(self, vec):
#        self.vec = vec

#     def __str__(self):
#         str1 = "" 
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index +=1
#         return str1[:-1] #[:-1]:used coz + sign will not return at in output
 
#     def __add__(self, vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return Vector(newList)

#     def __mul__(self, vec2):
#         sum = 0
#         for i in range(len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum


# v1 = Vector([1, 4, 6])
# v2 = Vector([1, 6, 9])

# print(v1+v2)
# print(v1*v2)

# #Q6

# class Vector:
#     def __init__(self,vec):
#         self.vec = vec

#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

# v1 = Vector([1,4,6])
# v2 = Vector([1,6,9])

# print(v1)
# print(v2)

#Q7
class Vector:
    def __init__(self, vec):
       self.vec = vec

    def __str__(self):
        str1 = "" 
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1] #[:-1]:used coz + sign will not return at in output
 
    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

        
    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 6, 7])
v2 = Vector([1, 6, 9])

print(len(v1))
print(len(v2))
