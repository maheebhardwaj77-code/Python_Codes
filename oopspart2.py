#oops part2 in python:-
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg marks is :", sum/3)

s_1 = Student("Mahee", [99, 98, 96])         
s_1.get_avg()
s_2 = Student("samarth", [10, 20, 30])
s_2.get_avg()        
s_3 = Student("happy", [40, 50, 40])
s_3.get_avg()
del s_2

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account(12345, "mahee")
print(acc1.acc_no)        
print(acc1.reset_pass()) 

class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

p1 = Person() 
print(p1.welcome())

#Inheritance:-
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")    

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.type)


#Multiple Inheritance:-
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varC)

class Person:
    name = "anonymous"

   # def changeName(self, name):
    #    Person.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)   
print(Person.name)    

class Teacher:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

tea1 = Teacher(34, 50, 98)
print(tea1.percentage)   
tea1.math = 70
print(tea1.percentage) 

class complex:
    def __init__(self, real, img):
        self.real = real 
        self.img = img

    def showNumber(self):
        print(self.real,"i+", self.img,"j")

    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal, newimg)

num1 = complex(1, 5)
num1.showNumber()       
num2 = complex(4, 7)
num2.showNumber()   
num3 = num1 + num2 
num3.showNumber()

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = (3.14 * self.radius * self.radius)
        print(self.radius,"radius circle have area this",area) 

    def get_perimeter(self):
        perimeter = (2 * 3.14 * self.radius)
        print("the perimeter of circle whose radius",self.radius,"is",perimeter)       

c1 = Circle(20)
c1.get_area()
c1.get_perimeter()

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)  

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer","IT","1000000")

    def get_Details(self):
        print("name =",self.name)
        print("age =",self.age)

e1 = Engineer("mahee","19")
e1.showDetails()    
e1.get_Details()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order("chips", 20)
order2 = Order("kurkure", 25) 
print(order1 > order2)   