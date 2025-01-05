# QUESTION 1: HOW WOULD YOU EXTRACT THE FIRST 5 CHARACTERS OF THE STRING "HELLO WORLD " USING SLICING?

# string1 = "HELLO WORLD"
# print(string1[:5])

#QUESTION 2 : GIVEN THE STRING "PYTHONPROGRAMMING", HOW WOULD YOU SLICE AND EXTRACT THE LAST 4 CHARACTERS?

# string2 = "PYTHONPROGRAMMING"

# print (string2[-4:])

# #OR
# length = len(string2)
# print(string2[length-4::1])

#QUESTION 3: FOR THE STRING "abcdefg", HOW CAN YOU SLICE THE STRING TO GET EVERY SECOND CHARACTER STARTING FROM THE FIRST?

# string3 = "abcdefg"
# print(string3[1::2])

#QUESTION 4: HOW CAN YOU REVERSE THE STRING "Palindrome" USING SLICING?

# string4 = "Palindrome"
# print(string4[::-1])

#QUESTION 5 : WHAT WILL BE THE RESULT OF THE SLICING OPERATION s[3:] IF s  = "DataScience"?

#aScience

#QUESTION 6: HOW WOULD YOU EXTRACT EVERY SECOND CHARACTER IN REVERSE ORDER FROM THE STRING "abcdefgh"?

# string6 = "abcdefgh"
# print(string6[-2::-2])

#QUESTION 7: FOR THE STRING "ArtificialIntelligence", HOW WOULD YOU EXTRACT THE SUBSTRING "Intelli" USING SLICING?

# string7 = "ArtificialIntelligence"
# index = string7.find("I")
# print(string7[index:index+7:1])

# Q8: Given two strings str1 = "Hello" and str2 = "World", concatenate them to form a new string "HelloWorld".

# str1 = "Hello"
# str2 = "World"
# str8 = str1 + str2
# print(str8)

# Q9: Extract the substring "loWor" from the string str = "HelloWorld" using slicing.

# string9 = "HelloWorld"
# print(string9[3:8:])

## Q10: Convert the string str = "apple,banana,cherry" to a list of fruits.

# str10 = "apple,banana,cherry"
# list10 = str10.split(",")
# print(list10)

# Q11: a="my name is rita" use all method of string give

# a="    my name is rita    "
# print(a.upper())
# print(a.lower())
# print(a.swapcase())

# print(a.strip()) #strip removes extra whitespaces at the beginning and the end of the string and if a character is given as an argument, it can remove them too.

# print(a.strip("a")) #if the characters to be removed are defined, and the same characters given, match the string value, then, those characters at the start and end of the string will be eliminated and the rest of the string will be returned.
# #here there are no a's at the start and end, so the original string remains unchanged

# print(a.strip().capitalize()) #capitalizes first word


# print(a.count("a"))
# print(a.count(" ")) #total number of whitespaces

# print(a.find("a")) #returns the first index of where the character is found, not others.

# print(a.replace("rita", "sita"))

# print(a.title().strip()) #converts into TitleCase

# print(a.removeprefix("my"))

# print(a.strip().removeprefix("my")) #strip first strips and then the first character becomes "m". then removeprefix removes "m".The previous line of code prints the original string because "m" is not the first chracter of the string. Removeprefix can only remove the argument character if it is at the first.

# #same for removesuffix
# print(a.removesuffix("rita"))

# print(a.strip().removesuffix("rita"))

# 1)assign the value 10 to a variable called x and print its value. 

# x = 10
# print(x)

# # 3)Given three numbers x = 12, y = 15, and z = 10, calculate and print their average. 

# x  = 12
# y = 15
# z = 10
# print((x+y+z)/3)

# # 4)Given P(principal amount), R(rate of interest), and T(time in years), calculate the simple interest using the formula SI= (P * R * T) / 100 and print the result

# P = 100
# T = 1
# R = 20
# SI = P*T*R/100
# print(SI)


# 1)Given two strings str1 = "Hello" and str2 = "World", concatenate them with a space in between and print the result.(i.e=adding)

# string111 = "Hello"
# string222 = "World"
# print(string111 + " " + string222)

# # 2)Given a string str = "PythonProgramming", find and print the length of the string.

# string22= "PythonProgramming"
# print(len(string22))

# 3)Given a string str = "HelloWorld", extract and print the substring "World" using slicing

# string33 = "HelloWorld"
# index = string33.find("W")
# print(string33[index:index+5:])

# 4)Convert the string str = "python" to uppercase and print the result.

# print("python".upper())
# # 5)Convert the string str = "PYTHON" to lowercase and print the result.

# print("PYTHON".lower())

# # 6)Reverse the string str = "Python" and print the result.

# print("Python"[::-1])