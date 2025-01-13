# #1 Write a python program to calculate the area of a rectangle.Take length and width as input and use multiplication.
l = float(input('Enter the length of rectangle:'))
b = float(input('Enter the breadth of the rectangle:'))
a = l * b
print('Area = ', a)

#2 Create a program to calculate the remainder when 25 is divided by 7.

print('Remainder = ', 25%7)

#3 Write a program to check if a number is greater than, less than or equal to another number.

first = int(input('Enter first number:'))
second = int(input('Enter second number:'))
if first > second:
    print('The first number is greater')
elif second > first:
    print('The second is greater')
else:
    print('They are equal')