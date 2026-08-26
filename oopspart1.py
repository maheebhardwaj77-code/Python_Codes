#OOPS in python:-
class Student:
    college_name = "ABC college"
    def __init__(self, fullname, marks):
        self.name = fullname 
        self.marks = marks
    def welcome(self):
        print("welcome student", self.name )
    def get_marks(self):
        return self.marks

s1 = Student("mahee", 94)       
s1.welcome()
print(s1.get_marks())

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
s_3.hello()

#Abstraction and Encapsulation:-
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clt = False

    def start(self):
        self.clt = True
        self.acc = True
        print("car started")    

car1 = Car()
car1.start()     

#create account class with 2 attributes- balance and account no:-
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount 
        print("Rs", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance   

cus1 = Account(100000, 10234)
cus1.debit(2000)
cus1.credit(10000)
cus1.debit(5000)
cus1.debit(50)

print("fuck off")