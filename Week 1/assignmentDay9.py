# Write a Python function called print_square that takes a number as an argument and prints the square of that number.
def print_square(x):
    print ( x ** 2)

num = int(input("Enter your number: "))
print_square(num)

# Write a Python function called print_list_elements that takes a list as an argument and prints each element in the list one by one.
def print_list_elements(x):
    for i in x:
        print(i, end = " ")

list = [1,2,3,4]
print_list_elements(list)

#  Write a Python function called multiply_by_two that takes a number as an argument and prints the number multiplied by 2

def multiply_by_two (x):
    print(2 * x)

num = int(input("Enter your number: "))
multiply_by_two(num)

#  make a calculator by using function where each operator has its own function

def addition(x,y):
    print ( x + y)
def subtraction(x,y):
    print(x-y)
def multiply(x,y):
    print ( x * y)
def divide(x,y):
    print(x/y)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter your operation (a for addition, s for subtraction, m to multiply, d to divide)")
if op == "+":
    addition(num1,num2)
if op == "-":
    subtraction(num1,num2)
if op == "*":
    multiply(num1,num2)
if op == "/":
    divide(num1,num2)

# Write a program to create a function that takes two arguments, name and age, and print their value.

def printit(n,a):
    print(f"Name: {n} Age: {a}")
printit("Jane", 28)
    

# # Write a program to create function func1() to accept a variable length of arguments and print their value.

def func1(*args):
    for arg in args:
        print(arg, end = " ")
    print("\n")
func1(1,2)
func1(1,2,3)
func1(1,2,3,4)



# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction.

def calculation(x,y,op):
    if op == "+":
        print( x + y)
    if op == "-":
        print(x-y)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter your operation (a for addition, s for subtraction, m to multiply, d to divide)")
calculation(num1,num2,op)




