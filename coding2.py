print("hello guys")
A = int(input("A :"))
G = input("M OR F :")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")

elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")

elif(A == 5 and G == "M"):
    print("fee is 300")

else:
    print("no fee") 

#Single Line Conditional Statements:-
age = int(input("age :"))
vote = "yes can give vote" if age >= 18 else "no you can't give vote"
print(vote)

#Clever If statements:-
marks = int(input("marks :"))
result = ("fail", "pass")  [marks >= 40]
print(result)

#Type Casting:-
a = 4
b = "5"
c = int(b)
sum = a + c
print(sum)

#WAP a program to input 2 number and print their sum:-
num1 = int(input("num1 :"))
num2 = int(input("num2 :"))
addition = num1 +num2
print("the addition of these two number is :",addition) 

#WAP to input side of a square and print its area:-
side = int(input("side :"))
permeter = 4 * side
area = side * side
print("the permeter of square is :",permeter)
print("the area of square is :", area)

#WAP to input 2 floating point number and print their average:-
numf1 = float(input("numf1 :"))
numf2 = float(input("numf2 :"))
average = (numf1 + numf2) / 2
print("the average is :",average)

#WAP to input 2 int number a and b. Print true if a is greater than or equal to b. If not print false:-
first = int(input("first :"))
second = int(input("second :"))
print(first >= second)  

#String and its rule:-
str1 = "mahee" #concatenation in strings
str2 = "bhardwaj"
final = (str1 + " " + str2)
print(final)
len1 = len(str1) #length of string
len2 = len(str2)
final_len = len(final)
print(len1)
print(len2)
print(final_len)
final_ch = final[4] #indexing
print(final_ch)
print(final[2:9]) #slicing
print(final[4:7])
print(final[-11:-5])
print(final[-10:-5])
print(final.endswith("waj"))     #returns true if string ends with substr
print(final.capitalize())        #capitalizes 1st char
print(str1.replace("ee", "i"))   #replaces old value with new value
print(str2.find("a"))            #return the index number of word
print(final.count("a"))          #counts the occurrence of substr

#WAP to input user's name and print its length:-
user1 = input("user name :")
user1_len = len(user1)
print("length of user's name :", user1_len)

#Nesting:-
my_age = int(input("My age is :"))
if(my_age >= 18):
    if(my_age >=80):
        print("over eaged")
    else:
        print("can drive")
else:
    print("minor")

#WAP to check if a number entered by the user is odd or even:-
number = int(input("enter the number :"))
if(number % 2  == 0):
    print("entered number is even")
else:
    print("entered number is odd")

#WAP to find the greatest of 3 number entered by the user:-
x = int(input("enter x :"))
y = int(input("enter y :"))
z = int(input('enter z :'))
if(x > y):
    if(x > z):
        print("x is greatest number :",x)
    else:
        print("z is graetest number :",z)
elif(y > z):
    print("y is greatest number :",y)

#Lists:-
roll_no = [98, 54, 32, 54, 89, 23]
print(roll_no)
print(roll_no[2]) #indexing
print(type(roll_no)) #type list
print(len(roll_no)) #length of list
roll_no[3] = "87" #changment in list allowed
print(roll_no)
print(roll_no[1:4]) #list slicing
print(roll_no[ :3])
roll_no.append(100) #add one element at the end
print(roll_no)
print(roll_no.remove(89)) #remove any element
print(roll_no)

#Tuples:-
tup = (34, 56, 35, 78, 89, 100)
print(tup)
print(tup[3]) #indexing
print(len(tup)) #length of tuples
print(type(tup)) #type tuples
print(tup[2:5]) #tuples slicing
print(tup[1:3])
print(tup.index(78)) #finding index number

#WAP to ask the user to enter name of their 3 favorite movirs and store them in list:-
movie1 = input("enter name :")
movie2 = input("enter name :")
movie3 = input("enter name :")
movie = [movie1, movie2, movie3]
print(movie) 

print("Har Har Mahadev")