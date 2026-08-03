print("---------------WELCOME SIR/MAM---------------")

#Print number from 1 to 100:-
a = 1

while a <= 100:
    print(a)
    a += 1

print("Loop is ended.")

#Print even number from 1 to 100:-
b = 2

while b <= 100:
    print(b)
    b += 2

print("Loop is ended.")

#Print odd number from 1 to 100:-
c = 1

while c <= 100:
    print(c)
    c += 2

print("Loop is ended.") 

#Find sum of numbers from 1 to n:-
n = int(input("Enter the number :"))
sum = 0
d = 1

while d <= n:
    sum += d
    d += 1
print("sum is :",sum)

print("Loop is ended.")     

#Find factorial of a number:-
num_1 = int(input("Enter your first number :"))
fact = 1
e = 1
while e <=num_1:
    if(num_1 == 0 or num_1 == 1):
        print("1")
    else:
        fact *= e
        e += 1
print("factorial is :",fact)

print("Loop is ended.")

#Count digits in a number:-
f = input("Enter your number :")

print("No. of digits in your number is :",len(f)) 

#Reverse a number:-
g = int(input("Enter your number :"))
reverse = 0

while g > 0:
    digit = g % 10
    reverse = reverse * 10 + digit
    g = g // 10
print("reversed number =",reverse)

print("Loop is ended.") 

#Generate fibonacci series:-
num_2 = int(input("Enter your number :"))
h = 0
i = 1
fibo = 0

while fibo < num_2:
    print(h," ")
    j = h + i
    h = i
    i = j
    fibo += 1

print("\nLoop is ended.")    

#Check prime number:-
num_3 = int(input("Enter your number :"))

if(num_3 > 1):
    is_prime = True

    for k in range(2, num_3):
        if num_3 % k == 0:
            is_prime = False
            break

    if is_prime:
        print(num_3,"is a prime number.")
    else:
        print(num_3,"is not a prime number.")

else:
    print(num_3,"is not a prime number")                 

#Print all prime numbers in a range:-
start = int(input("Enter your starting number :"))
end = int(input("Enter your ending :"))

print("Prime numbers are :")

for l in range(start, end + 1):
    if(l > 1):
        prime = True

        for m in range(2, l):
            if l % m == 0:
                prime = False
                break

        if prime:
            print(l)    

print("---------------THANKS FOR USEING ME---------------")            