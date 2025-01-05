# #String is a collection of one or more characters and it in enclosed inside a quotation.

# a = """We are Sipalaya.
# We are located in Kathmandu.
# Welcome here."""

# print("Data type of a is " + str(type(a)))

# b = "Sipalaya"
# #len(b) gives the length of the string
# print(len(b))

# #Indexing: Regular indexing starts from 0 and reverse indexing starts from -1
# print(b[2])
# print(b[-1])
# print(b[-2])

# #Slicing is done to access a part of a string
# #Syntax of slicing: [start:end:step]
# s = "What is slicing?"

# print(s[0:4:])
# #To access slicing
# #Step is set to 1 by default.
# #Find the difference here.
# print(s[8:15:]) 
# print(s[14:7:-1]) #Reverse of slicing 

# print(s[2:])
# #Prints everything from index 2 to the end

# print (s[:7])

# print(s[::-1])
# #Prints in reverse


#String functions
#Strings are immutable.

# f = "Welcome to Sipalaya."

# #Upper
# g = f.upper()
# #f is immutable so it is stored in next variable.
# print(g)

# #Lower
# h = f.lower()
# print(h)

# #Swapcase, upper to lower and lower to upper
# i = f.swapcase()
# print(i)

# #Capitalize
# j = f.capitalize()
# print(j)

# #Count number of characters inside a string
# k = f.count("a")
# print(k)

# #Find
# l = f.find('w') #Capital w is present not small w.
# print(l) # so it gives result -1 if a character is not present in a string.





