#1 Create a parent class person with attributes name and age.
#Create a child class Student that inherits person and adds an attribute grade. Display the details using a method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self. age)
class Student(Person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade = grade
    def show(self):
        super().show()
        print(self.grade)
stu = Student("Jane", "29", "B")
stu.show()

#2 Implement multiple inheritance where ClassA and ClassB have methods methodA() and methodB(), respectively. The child class ClassC should inherit both and call methods from both parents
class A:
    def __init__(self):
        pass
    def methodA(self):
        print("My name is class1")
class B:
    def __init__(self):
        pass
    def methodB(self):
        print("My name is class2")
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def methodC(self):
        print("My name is class3")
c = C()
c.methodA()
c.methodB()
c.methodC()



#3 Use super() method in a child class to call the parent class constructor and method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self. age)
class Student(Person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade = grade
    def show(self):
        super().show()
        print(self.grade)
stu = Student("Jane", "29", "B")
stu.show()

#4 Write a function that takes a list of shapes (Circles,Square,etc) and calls their area method
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        self.area = 3.14 * self.r ** 2
        return self.area
class Rectangle:
    def __init__(self, l , b):
        self.l = l
        self.b = b
    def area(self):
        self.area = 3.14 * self.l * self.b
        return self.area
class Square:
    def __init__(self, l):
        self.l = l
    def area(self):
        self.area = 3.14 * self.l ** 2
        return self.area
def area_calc(shapes):
    for shape in shapes:
        print(f"The area of {shape.__class__.__name__} is {shape.area()}")
circ = Circle(5)
rect = Rectangle(9,8)
squa = Square(7)
shapes_list = [circ, rect, squa]
area_calc(shapes_list)

#5 Create a class Student with private attributes name and grade. Write methods to set and get the values of these attributes.
class priv():
    def __init__(self):
        pass
    def setValues(self, name, grade):
        self.__name = name
        self.__grade = grade
    def getValues(self):
        print(self.__name, self.__grade)
student = priv()
student.setValues("Jane", "C")
student.getValues()


#6 Write a class Car with private attributes make and year. Add methods to update the year only if it is greater than the current value
class Car:
    def __init__(self,make,year):
        self.__make=make
        self.__year=year
    def update(self,current_year):
        if current_year>self.__year:
            self.__year = current_year
    def show(self):
        print(self.__make, self.__year)
c=Car('Maruti',2001)
c.update(2010)
c.show()

#7 Write a class BankAccount with private attriutes acc_num and balance.Add methods to:
#deposit money(validate that the amount is positive)
#withdrawmoney(ensure sufficient balance)
#view the current balance
class BankAC:
    def __init__(self,__acc_num,__balance):
        self.__acc_num=__acc_num
        self.__balance=__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            return 'You cant deposit.'
    def withdraw(self,amount):
        if amount>self.__balance:
            return 'You dont have that much money'
        else:
            self.__balance-=amount
    def details(self):
        print('Balance:',self.__balance)
a=BankAC(9876,2345)
a.deposit(1234)
a.withdraw(12345)
a.details()

#8 Implement a class Employee with a private attribute salary and methods to:
#set the salary(with the condition that it must be greater than zero)
#get the salary

class Employee:
    def __init__(self):
        pass
    def setSalary(self,amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Salary must be greater than 0")
    def getSalary(self):
        print(f"Salary of person : {self.__salary}")
e = Employee()
e.setSalary(-10)
e.setSalary(20)
e.getSalary()


