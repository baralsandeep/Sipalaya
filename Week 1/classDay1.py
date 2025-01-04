# variable
number = 6

name = "Sipalaya"

#write a program to receive first char from your name
print("The first character of your name is:")
print(name[0])

# Data types
print("Data type of the variable number is")
print(type(number))

print("Data type of the variable name is")
print(type(name))

grade = 3.2
print("Data type of variable grade is ")
print(type(grade))

data = 4 + 2j
print("Date type of variable data is ")
print(type(data))

data1 = True
print("Data type of variable data1 is ")
print(type(data1))

x = [12,67, "Sipalaya", True]
print("Data type of variable x is")
print(type(x))

print(x[0])

print("Length of x is " + str(len(x)))
# String cannot be concatenated to a integer as len(x) returns an integer. We then convert it to string using str(len(x))

#adds an item to the end of the list
x.append(23)
print(x)