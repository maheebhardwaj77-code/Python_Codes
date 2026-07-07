print("--------------WWELCOME SIR/MAM---------------")


#Swap two variables:-
a = 12
b = 18

print("----------BEFORE SWAPING----------")
print("value of a is :",a)
print("value of b is :",b)

a, b = b, a

print("----------AFTER SWAPING-----------")
print("new_value of a is :",a)
print("new_value of b is :",b)


#check if a number is even or odd:-
num = int(input("enter your number :"))

if(num % 2 == 0):
    print("yes,",num,"is even number.")
else:
    print("no,",num,"is odd number.") 


#Check if a number is positive, negative or zero:-
num1 = int(input("enter your number :"))

if(num1 == 0):
    print(num1,"is equal to zero.")
elif(num1 > 0):
    print(num1,"is positive number.")
else:
    print(num1,"is negative number.")   


#Find the largest of two numbers:-
num_1 = int(input("Enter your first number :"))
num_2 = int(input("Enter your second number :"))

if(num_1 > num_2):
    print(num_1,"is greater than",num_2,".")
elif(num_1 == num_2):
    print("both number the equal to :",num_1)
else:
    print(num_2,"is greater than",num_1,".")


#Find the largest of three number:-
x = int(input("Enter your first number :"))
y = int(input("Enter your second number :"))
z = int(input("Enter your third number :"))

if(x > y):
    if(x > z):
        print(x,"is the greatest number.")
    else:
        print(z,"is the greatest number.")

elif(y > x):
    if(y > z):
        print(y,"is the greatest number.")
    else:
        print(z,"is the greatest number.") 

elif(x == y):
    if(x > z):
        print("x and y both are equal and greater than z.")   
    else:
        print("x and y are equal but z is greater number.")

elif(y == z):
    if(y > x):
        print("y and z are equal and greater than x.")
    else:
        print("y and z are equal but x is greater number.")

elif(x == z):
    if(x > y):
        print("x and y are equal and greater than y.") 
    else:
        print("x and z are equal but y is greater number.")                                      

else:
    print("all number are equal.") 


#Check if a year is a leap year:-
year = int(input("Enter your selected year :"))

if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("yes,",year,"is leap year.")

else:
    print("no,",year,"is not leap year.")    