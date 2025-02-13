# 1Create a class called Person with attributes name and age. Create an instance of the class and print the name and age of the person.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)
per = Person("John", 45)
per.show()

#2 Add a method greet to the Person class that prints a greeting message including the person's name.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)
    def greet(self):
        print(f"Hello {self.name} How are you? ")
per = Person("John", 45)
per.show()
per.greet()

# 3 Write a function that takes a list of shapes(Circle,Square etc) and calls their area()method, demonstrating polymorphism.

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




#4 Create a function describe_animal() that takes an object of any class and calls its sound() method. Define classes Cat and Bird with their own implementations of the sound() method. Pass objects of both classes to describe_animal().
class Cat:
    def sound(self):
        return 'meow'

class Bird:
    def sound(self):
        return 'chirp'

def describe_animal(animal):
    print(animal.sound())

cat=Cat()
describe_animal(cat)
bird=Bird()
describe_animal(bird)

#5 Define a base class Shape with a method area(). Create two derived classes Circle and Rectangle that implement the area() method differently. Instantiate objects of both classes and call their area() methods.
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
circle=Circle(5)
print('Area of circle is:',circle.area())

rectangle=Rectangle(4,6)
print('Area of rectangle is:',rectangle.area())

