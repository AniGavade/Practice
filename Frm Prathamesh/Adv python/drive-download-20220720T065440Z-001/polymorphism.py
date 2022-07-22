# Polymorphism word came from two greek words, poly means many and morphos means forms.
# if a variable, object or method perform different behaviour according to situation is called polymorphism.
# it allows us to define methods in the child class with the same name as defined in their parent class.

# ------------------------------------------------------------------------------------------------------------------------
# overloading
# ------------------------------------------------------------------------------------------------------------------------

# Overloading is the ability of function / operator to behave in different ways based on the parameters that are passed
# to function. Normally in python, we don't have the same names for different methods. But overloading is a method to
# do the different functionalities with the same name i.e. method differ their parameters to pass the method.

# method overloading


# class Person:
#     def hello(self, name= None):
#         self.name = name
#         if (self.name != None):
#             print(f"Hello {self.name}")
#         else:
#             print("Hello")
#
#
# obj = Person()
# obj.hello()                    # here we are calling hello method with zero parameters
# obj.hello("Aniruddha")         # here we are calling hello method with one parameter


# class Addition:
#     def add(self, *x):
#         print('addition is : ', sum(x))
#
#
# a = Addition()
#
# a.add()
# a.add(5)
# a.add(5, 10)


# class Shape:
#     # function with two default parameters
#     def area(self, a, b=0):
#         if b > 0:
#             print('Area of Rectangle is:', a * b)
#         else:
#             print('Area of Square is:', a ** 2)
#
#
# square = Shape()
# square.area(5)
#
# rectangle = Shape()
# rectangle.area(5, 3)

# ------------------------------------------------------------------------------------------------------------------------

# constructor overloading

# class Car:
#     def __init__(self, *name):
#         self.name = name
#         for i in self.name:
#             print('This is', i)
#
#
# c = Car('ferrari', 'lambo')
# c = Car('pagani')

#
# class Car1:
#     def __init__(self, name1='ferrari', name2='lambo'):
#         self.name1 = name1
#         self.name2 = name2
#         print(f'I have both cars {name1} as well as {name2}')
#
#
# car = Car1()
# car = Car1('pagani')
# car = Car1('Thar', 'Honda city')

# ------------------------------------------------------------------------------------------------------------------------

# operator overloading

# class Operator:
#     def __init__(self):
#         pass
#
#     def plus(self, x, y):
#         print('using + operator we can add two numbers')
#         print(f'addition of {x} and {y} is {x + y}')
#
#         print('another use of + operator is to concatenate two string')
#         name1 = input('enter 1st name')
#         name2 = input('enter 2ne name')
#
#         print(name1 + name2)
#
# obj = Operator()
# obj.plus(5, 10)

# ----------------------------------------------------------------------------------------------------------------------
# method overriding
# ----------------------------------------------------------------------------------------------------------------------


# class Car:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
#         self.odometer = 0
#
#     def describe_vehicle(self):
#         name = f"{self.name} {self.model} {self.year}"
#         return name.title()
#
#     def odometer_reading(self):
#         print(f"odometer running is {self.odometer}")
#
#     def update_odometer(self, mileage):
#         if self.odometer < mileage:
#             self.odometer = mileage
#             print(f"odometer running is {self.odometer}")
#         else:
#             print("you cannot roll back odometer.")
#
#     def fill_gas(self):
#         print("this car requires to fill gas.")
#
#
# class ElectricCar(Car):
#
#     def __init__(self, name, model, year, battery_size):
#         super().__init__(name, model, year)
#
#         # defining new attributes and methods for child class
#         self.battery_size = battery_size
#
#     def describe_battery_size(self):
#         print(f"This car has a {self.battery_size}-kW battery.")
#
#     def fill_gas(self):
#         print("no need to fill gas since this is electric car.")

# When you use inheritance, you can make your child classes retain what you need and override anything you don’t need
# from the parent class.

#
# my_tesla = ElectricCar('tesla', 'model-s', 2022)
# description = my_tesla.describe_vehicle()
# print(description)
# my_tesla.describe_battery_size()
# my_tesla.fill_gas()

# ------------------------------------------------------------------------------------------------------------------------
# duck typing philosophy
# ------------------------------------------------------------------------------------------------------------------------

# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")
#
#     def max_speed(self):
#         print("Max speed 350")
#
#
# class BMW:
#     def fuel_type(self):
#         print("Diesel")
#
#     def max_speed(self):
#         print("Max speed is 240")
#
#
# ferrari = Ferrari()
# bmw = BMW()
#
# # iterate objects of same type
# for car in (ferrari, bmw):
#     # call methods without checking class of object
#     car.fuel_type()
#     car.max_speed()

# ------------------------------------------------------------------------------------------------------------------------

# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")
#
#     def max_speed(self):
#         print("Max speed 350")
#
# class BMW:
#     def fuel_type(self):
#         print("Diesel")
#
#     def max_speed(self):
#         print("Max speed is 240")
#
# # normal function
# def car_details(obj):
#     obj.fuel_type()
#     obj.max_speed()
#
# ferrari = Ferrari()
# bmw = BMW()
#
# car_details(ferrari)
# car_details(bmw)


