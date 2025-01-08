#1 Given a list my_list[10,20,30,40,50] access the third element and store it in a variable third_element
# my_list = [10,20,30,40,50] 
# third_element = my_list[2]
# print(third_element)

# #2 Create a new list containing the first three elements of the list my_list

# my_list=[10,20,30,40,50]
# new_list = my_list[:3] #upto index 2
# print(new_list)

# #3 Convert the str='apple,banana,cherry' to a list of fruits
# string1 = 'apple,banana,cherry'
# fruits_list = string1.split(",")
# print(fruits_list)

# #4 Replicate the list my_list=[1,2,3] three times to form a new list [1,2,3,1,2,3]
# my_list = [1,2,3]
# my_list.extend(my_list);
# print(my_list)

# #5 List a=['hello',45.67,89.90,45,45,'apple','orange']
#add value 34 to the list
# a=['hello',45.67,89.90,45,45,'apple','orange']
# a.append(34) #append is used to add a single value.

# #add multiple value to the list
# a.extend(['Namaste',85]) #extend to add multiple values, the parameters to append and extend is a list
# print(a)

# #using slicing extract app from the given list
# print (a[5][:3])

# #remove random value from the list(45)
# a.remove(45)
# print(a)

# #remove all data from the list
# a.clear()
# print(a)

# #clear deletes the content of the list
# # del(a) deletes the whole list.

# #6 Given two list a and b add these two list in third list and print the third list
# a=[1,2,3,4]
# b=['a','b','c','d']
# third = a+b
# print(third)

#7 Given two tuple1 and tuple 2 concatenate them to form a new tuple
# a=(1,2,3,4)
# b= ('a','b','c','d')
# c= a+b
# print(c)

#8 Given the tuple my_tuple, slice the tuple to get the last three elements
# my_tuple=(10,20,30,40,50)
# print(my_tuple[-3::1])

# #9 Find the length of the tuple my_tuple=['a','b','c','d']
# my_tuple=['a','b','c','d']
# print(len(my_tuple))

# #10 Given a list a=[3,5,32,4,52,13,4,6,71] sort in ascending and descending order using both method
# a=[3,5,32,4,52,13,4,6,71]

# #sort
# a.sort() #ascending order
# print(a) 
# a.sort(reverse=True) #descending order
# print(a)

# #sorted
# sa=sorted(a) #ascending
# print(sa)
# ra =sorted(a,reverse=True) #descending
# print(ra)