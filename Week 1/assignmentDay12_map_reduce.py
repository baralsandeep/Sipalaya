#1 Given a list of integers [1,2,3,4,5] use map to create a new list where each element is squared
num_list = [1,2,3,4,5]
square = lambda n: n**2
print (list(map(square, num_list)))



#2 From the list [10,15,20,25,30] use filter to get a new list containing only numbers divisible by 10
num_list = [10,15,20,25,30]
divisible_by_ten = lambda n: n%10 == 0
print(list(map(divisible_by_ten, num_list)))

#3 Use reduce to calculate the product of all numbers in the list [1,2,3,4,5]
num = [1,2,3,4,5]
prod = lambda x,y: x*y
from functools import reduce
print(reduce(prod, num))

