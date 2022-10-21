
# # Inheritance in python
"""The process of inheriting the properties of the parent class into a child
class is called Inheritance"""

# class BaseClass:
#     # body of base class
# class DerivedClass(BaseClass):
#     # Body of derived class
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # Types of Inheritance
# # 1. Single inheritance
# # 2. Multiple inheritance
# # 3. multilevel inheritance
# # 4. Hierarchical inheritance
# # 5. Hybrid inheritance

# # 1. Single Inheritance
# Parent class ==> Child class

# Ex.


# #  Base class
# class Vehicle:
#     def vehicle_info(self):
#         print("Inside vehicle class")
#
#
# # child class
# class Car(Vehicle):
#     def car_info(self):
#         print("Inside Car class")
#
#
# # create object of Car
# car = Car()
#
# # access vehicle's info using car object
# car.vehicle_info()
# car.car_info()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Multiple inheritance
# - One child can inherit from multiple parent classes. so here is one child class and multiple parent class.

# Parent Class,  Parent class
#           \      /
#            \    /
#          Child Class

# Ex.
# Parent Class 1
class person:
    def person_info(self, name, age):
        print('Inside the Person class')
        print("Name: ", name, "Age: " age)


# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print()