#Loops in python:-
#(1)While loops:-
i = 5
while i >= 1:
    print(i)
    i -= 1

#print number from 1 to 100:-
a = 1
while a <= 100 :
    print(a)
    a += 1
print("loop is ended")

#print number from 100 to 1:-
b = 100
while b >=1 :
    print(b)
    b -= 1
print("loop is ended") 

#print the multiplication table of a number n:-
n = int(input("enter the value :"))
c = 1
while c <= 10 :
    print(n*c)
    c += 1
print("loop is ended") 

#print the element of the following list using a loop:-
tup1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx1 = 0
while idx1 < len(tup1) :
    print(tup1[idx1])
    idx1 += 1
print("loop is ended") 

#search for a number x in this tuple using loop:-
tup2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
e = 25
idx2 = 0
while idx2 < len(tup2) :
    if(tup2[idx2]  == e):
        print("found at index", idx2)
        break
    else:
        print("finding..")    
    idx2 += 1

#(2)For loop:-
nums1 = [1, 4, 9, 3, 4, 6]
for val in nums1 :
    print (val)

string = "Mqhee Bhardwaj"
for char in string:
    print(char)  
else:
    print("END") 

#Print the element of the following list uding a for loop:-
square1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for x in square1 :
    print(x)
else:
    ("end") 

#search for a number x in this tuple using for loop:-
square2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
z = 16
idx3 = 0
for y in square2 :
    if(y == z) :
        print("found at index :",idx3)
        break
    else:
        print("not found")
    idx3 += 1 

#Range() in python:-
for el in range(7):
    print(el)

for ell in range(2, 10):
    print(ell)

for elll in range(5, 51, 5):
    print(elll)    

#print number from 1 to 100 by using range:-
for no_1 in range(1, 101):
    print(no_1)

#print number from 100 to 1 by using range:-
for no_2 in range(100, 0, -1):
    print(no_2) 

#print the multiplication table of a number n:-
f = int(input("enter number :"))
for no_3 in range(1, 11):
    print(f * no_3) 

#Pass statement:-
for key in range(7, 71, 7):
    pass
print("hello dosto byeee")   

#WAP to find the sum of first n natural number:-
h = int(input("enter number :"))
sum_1 = 0
l = 1
while l <= h :
    sum_1 += l
    l += 1
print("sum is :", sum_1) 

#WAP to find the factorial of first n natural number:-
u = int(input("enter no."))
sum_2 = 1
for t in range(1, u+1):
    sum_2 *= t
print("factorial is :", sum_2)    