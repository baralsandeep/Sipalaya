#1 Create a function that takes two numbers as input and returns their sum
num1=int(input('enter first number'))
num2=int(input('enter second number'))
def add(num1,num2):
    return num1+num2
print(add(num1,num2))

#2 Write a function factorial that computes the factorial of a number using recursion
num=int(input('enter a number'))
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
print(factorial(num))

#3 Define a function that checks whether a given string is a palindrome.
def palindrome(string):
    str=string.lower()
    return str==str[::-1]
print(palindrome('madam')) #True
print(palindrome('hello')) #False

#4 Write a function max_of_three that takes three numbers and returns the largest of the three.
n1=int(input('enter a number'))
n2=int(input('enter second number'))
n3=int(input('enter third number'))
def maximum(n1,n2,n3):
    return max(n1,n2,n3)
print(maximum(n1,n2,n3))

#5 Create a function that takes a number as input and returns True if the number is prime otherwise false
def num(number):
    if number<=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
print(num(5)) #True
print(num(10)) #False

#6 Write a function fibonacci that takes a number n and returns the first n terms of the Fibonacci sequence as a list.	
a=int(input('enter number'))
def fibonacci(a):
    if a<=0:
        return[]
    elif a==1:
        return[0]
    elif a==2:
        return[0,1]
    fib_sequence=[0,1]
    for i in range(a-2):
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
    return fib_sequence
print(fibonacci(a))

#7 Define a function count_vowels that takes a string as input and counts the number of vowels in the string.
str=input('enter a string')
def count_vowels(a):
    vowels='aeiouAEIOU'
    count=0
    for i in str:
        if i in vowels:
            count+=1
    return count
print(count_vowels(str))

#8 Write a function that takes a string and returns the reversed string.
string=input('enter a string')
def revesre(string):
    return string[::-1]
print(revesre(string))

#9 Write a function that takes a list and returns a new list with duplicates removed.
def remove_duplicate(list):
    return (set(list))
list=[1,2,2,3,4,4,5]
print(remove_duplicate(list))

#10 Write a function sort_list that takes a list of numbers and returns the list sorted in ascending order.
list=[7,9,2,3,5]
def sort_list(list):
    return sorted(list)
print(sort_list(list))




