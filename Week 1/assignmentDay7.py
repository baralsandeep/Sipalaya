# Write a program that asks the user to enter a number and checks whether the number is odd or even

user_input = int(input("Enter your number: "))
if user_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Write a program that takes a score as input and assigns a grade based on the following criteria:

# 90 and above: Grade A
# 80–89: Grade B
# 70–79: Grade C
# Below 70: Grade 

score = int(input("Enter your score (0-100): "))
if score >= 90 :
    print("You are assigned grade-A")
elif score >= 80 and score < 90:
    print("You are assigned grade-B")
elif score >= 70 and score < 80:
    print("You are assigned grade-C")
else:
    print("You are assigned grade-D")



# Write a program to check if a person is eligible to vote. The eligibility age is 18 or above.

age = int(input("State your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Write a program that takes three numbers as input and prints the largest among them.

first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))
third = int(input("Enter the third number:"))

if first > second and first > third:
        print("The first number is the greatest.")

#If it comes here from the first condition, either first > second is false or first > third is false, it implies second or third is greater than first. The greater one of the second or third is greatest now.

elif second > third: 
    print("The second number is the greatest.")

#since second > third turns out to be false, we have only remaining case being third the greatest.
else:
    print("The third number is greatest.")


# Write a program to check if a given year is a leap year or not. A year is a leap year if:

# It is divisible by 4 but not divisible by 100, OR
# It is divisible by 40

year = int(input("Enter the year you want to know is a leap year: "))
if (year%4==0 and year%100!=0) or year%40==0: 
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')

# Write a program to implement a simple calculator. The program should:

# Ask the user for two numbers.
# Ask the user to choose an operation (add, subtract, multiply, divide).
# Perform the chosen operation and print the result

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
op = str(input('Choose an operation type "a" to add, "s" to subtract, "m" to multiply, "d" to divide: '))
if op =='a':
    sum=num1+num2
    print(f'The sum is {sum}')
elif op =='s':
    dif=num1-num2
    print(f'The difference is {dif}')
elif op =='m':
    prod=num1*num2
    print(f'The product is {prod}')
elif op =='d':
    quo=num1/num2
    print(f'The quotient is {quo}')
else:
    print('Operation unspecified')

# Write a program to print numbers from 1 to 100.
# If a number is divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".
# Otherwise, print the number itself

for i in range (1,101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz.")
        else:
            print ("Fizz.")
    elif i % 5 == 0:
        print("Buzz.")
    else:
        print(i)

# Given two variables x = 15 and y = 20, use conditional statements to print which variable is larger, or if they are equal.

x = 15
y = 20

if x>y:
    print("x is larger.")
elif x<y:
    print("y is larger.")
else:
    print("They are equal.")


#  Given a variable num = 7, use a conditional statement to check if the number is even or odd and print the result. 

num = 7
if num % 2 == 0:
    print("Even.")
else:
    print("Odd.")

# Write a Python Program to Check weather a candidate Eligible for Vote or not.

age = int(input("State your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Write a Python program to check weather Given Number is Divisible by 7 or Not.

num7 = int(input("Enter the number to check whether the Given Number is Divisible by 7 or Not: "))
if num7 % 7 == 0:
    print("Yes.")
else:
    print("No.")

# Check if the value 10 is not present in the tuple t = (5, 15, 20, 25).

t = (5, 15, 20, 25)
check = 10 not in t
print(check)

# Determine if the value 25 is present in the list lst = [10, 20, 30, 40, 50] using a simple conditional statement.

lst = [10, 20, 30, 40, 50]
if (25 in lst) == True:
    print("25 is present.")
else:
    print("25 is not present.")

# Check if the value 100 exists in the set s = {50, 75, 100, 125}.

s = {50,75,100,125}
if (100 in s) == True:
    print("100 exists in the set.")
else:
    print("100 is not present in the set.")