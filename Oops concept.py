class Monisha():
    num = 100
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    def Addition(self):
        return self.num1+self.num2+Monisha.num

obj=Monisha(50,100)
print(obj.Addition())

#inheritance- below is the child class. Monisha is the parent class.
class Childcls(Monisha):
    num3=500

    def __init__(self):
        Monisha.__init__(self,50,100)

    def Summation(self):
        return self.Addition()+Childcls.num3

obj1=Childcls()
print(obj1.Summation())

#strings

str1= "brisha"
str2= ".com"
print(str1[0:3])
print(str1[3:6])
str3 = str1 + str2
print(str3)

print(str3.split("."))
s= " brisha "
print(s.rstrip())
