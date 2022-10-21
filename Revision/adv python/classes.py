# creating the dog class
# Each instance created from the Dog class will store a name and an age,
# and we'll give the ability to sit() and roll_over().


# class Dog:
#     """A simple attempt to model a dog"""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """simulate a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting.")
#
#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f"{self.name} rolled out")
#
#
# my_dog = Dog("Simba", 5)
#
# print(f"My dog's name is {my_dog.name}")
# print(f"My dog is {my_dog.age} years old")


# ______________________________________________________________________________________________________________________

# Polymorphism

# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         print("Area of Circle is: ", self.pi * self.radius * self.radius)
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def calculate_area(self):
#         print("Area of Rectangle: ", self.length * self.width)
#
#
# def area(shape):
#     # call action
#     shape.calculate_area()
#
#
# # create object
# cir = Circle(5)
# rect = Rectangle(10, 5)
#
# # call common function
# area(cir)
# area(rect)
# ______________________________________________________________________________________________________________________

