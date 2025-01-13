# Create a dictionary with the following key-value pairs: (name , age, and city ). 

new_dict = {
    "name": "John",
    "age" : 40,
    "city": "Manhattan"
}

# Given the dictionary person = {'name': 'Bob', 'age': 30, 'city': 'Los Angeles', 'job': 'Doctor'}, access and
#  print the values associated with the keys 'name' and 'job'

dict2= {'name': 'Bob', 'age': 30, 'city': 'Los Angeles', 'job': 'Doctor'}
print(dict2["name"])
print(dict2["job"])

# 3)Given the dictionary person = {'name': 'John', 'age': 28, 'city': 'Chicago'}, add a new key-value pair 'job': 'Teacher' to the dictionary. Then update the value of the 'age' key to 29.

person = {'name': 'John', 'age': 28, 'city': 'Chicago'}

person["job"]="Teacher"
person["age"]= 29
print(person)

# 4)Create a nested dictionary to store the details of two people. and access one dictionary keys and value

employee = {
    "e1":{
        "name":"John",
        "age":34
    },
    "e2":{
        "name":"Jane",
        "age":48
    }
}
print(employee["e1"])

# 5)Given two dictionaries dict1 = {'a': 1, 'b': 2, 'c': 3} and dict2 = {'b': 4, 'c': 5, 'd': 6}, find the common keys between the two dictionaries.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

common = dict1.keys() & dict2.keys()
print(common)

# 6)Given the dictionary person = {'name': 'Sarah', 'age': 35, 'city': 'Miami', 'job': 'Lawyer'}, remove the key-value pair with the key 'city

person = {'name': 'Sarah', 'age': 35, 'city': 'Miami', 'job': 'Lawyer'}

person.pop("city")
print(person)