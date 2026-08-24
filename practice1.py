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


#Create a simple calculator:-
def calc():
    print("simple calculator")
    print("operations: +, -, *, /")

    no_1 = int(input("Enter your first number :"))
    op = input("Enter operation :")
    no_2 = int(input("Enter your second number :"))

    if(op == "+"):
        result = no_1 + no_2
    elif(op == "-"):
        result = no_1 - no_2
    elif(op == "*"):
        result = no_1 * no_2
    elif(op == "/"):
        if(no_2 == 0):
            print("Error: Cannot divide by zero.")
            return 
        result = no_1 / no_2
    else:
        print("Invalid operation.")
        return
    print("Result :",result)

calc() 


#Convert Celsius to Kelvin:-
temp = float(input("Enter temperature in celsius :"))

kelv = temp + 274

print("temperature in kelvin is :",kelv) 


#Find the area of circle:-
radius = float(input("Enter the radius of your circle :"))

perimeter = (2 * 3.14 * radius)
area = (3.14 * radius * radius)

print("perimeter of your circle is :",perimeter)
print("area of your circle is :",area) 


#Calculate student grade from marks:-
marks = int(input("Enter your marks :"))

if(marks >= 90):
    print("you are pass and got A grade. Your marks:",marks)
elif(marks >= 80):
    print("you are pass and got B grade. Your marks:",marks)
elif(marks >= 70):
    print("you are pass and got C grade. Your marks:",marks)
elif(marks >= 60):
    print("you are pass and got D grade. Your marks:",marks)
elif(marks >= 50):
    print("you are pass and got E grade. Your marks:",marks)
else:
    print("you are fail and got F grade. Your marks:",marks)    


print("---------------THANKS FOR USEING ME---------------")                    





students = []


# Add Student
def add_student():
    name = input("Enter student name: ")

    maths = int(input("Enter Maths marks: "))
    physics = int(input("Enter Physics marks: "))
    chemistry = int(input("Enter Chemistry marks: "))

    student = {
        "name": name,
        "maths": maths,
        "physics": physics,
        "chemistry": chemistry
    }

    students.append(student)

    print("\nStudent added successfully! ✅")


# Calculate result
def calculate_result(student):
    total = (
        student["maths"]
        + student["physics"]
        + student["chemistry"]
    )

    percentage = total / 3

    return total, percentage


# Show all students
def show_students():

    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n===== All Students =====")

    for student in students:

        total, percentage = calculate_result(student)

        if percentage >= 33:
            result = "PASS"
        else:
            result = "FAIL"

        print("\nName:", student["name"])
        print("Maths:", student["maths"])
        print("Physics:", student["physics"])
        print("Chemistry:", student["chemistry"])
        print("Total:", total)
        print("Percentage:", round(percentage, 2), "%")
        print("Result:", result)


# Search student
def search_student():

    name = input("\nEnter student name to search: ")

    found = False

    for student in students:

        if student["name"].lower() == name.lower():

            total, percentage = calculate_result(student)

            print("\n===== Student Found =====")
            print("Name:", student["name"])
            print("Maths:", student["maths"])
            print("Physics:", student["physics"])
            print("Chemistry:", student["chemistry"])
            print("Total:", total)
            print("Percentage:", round(percentage, 2), "%")

            if percentage >= 33:
                print("Result: PASS")
            else:
                print("Result: FAIL")

            found = True
            break

    if found == False:
        print("\nStudent not found ❌")


# Find topper
def find_topper():

    if len(students) == 0:
        print("\nNo students found.")
        return

    topper = students[0]

    for student in students:

        student_total, topper_total = (
            calculate_result(student)[0],
            calculate_result(topper)[0]
        )

        if student_total > topper_total:
            topper = student

    total, percentage = calculate_result(topper)

    print("\n===== 🏆 Topper =====")
    print("Name:", topper["name"])
    print("Total:", total)
    print("Percentage:", round(percentage, 2), "%")


# Subject toppers
def subject_toppers():

    if len(students) == 0:
        print("\nNo students found.")
        return

    maths_topper = students[0]
    physics_topper = students[0]
    chemistry_topper = students[0]

    for student in students:

        if student["maths"] > maths_topper["maths"]:
            maths_topper = student

        if student["physics"] > physics_topper["physics"]:
            physics_topper = student

        if student["chemistry"] > chemistry_topper["chemistry"]:
            chemistry_topper = student

    print("\n===== Subject Toppers =====")

    print(
        "Maths Topper:",
        maths_topper["name"],
        "-",
        maths_topper["maths"]
    )

    print(
        "Physics Topper:",
        physics_topper["name"],
        "-",
        physics_topper["physics"]
    )

    print(
        "Chemistry Topper:",
        chemistry_topper["name"],
        "-",
        chemistry_topper["chemistry"]
    )


# Main program
while True:

    print("\n")
    print("===== Student Result System =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Subject Toppers")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        find_topper()

    elif choice == "5":
        subject_toppers()

    elif choice == "6":
        print("\nProgram closed. 👋")
        break

    else:
        print("\nInvalid choice ❌")