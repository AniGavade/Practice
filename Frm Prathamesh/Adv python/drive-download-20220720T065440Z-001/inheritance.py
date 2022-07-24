# # Inheritance allows us to define a class that inherits all the methods and properties from another class.
# # When one class inherits from another, it takes on the attributes and methods of the first class. The original class
# # is called the parent class, and the new class is the child class.
#
#
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
# my_car = Car('audi', 'a4', 2021)
#
# print(my_car.describe_vehicle())
# my_car.odometer_reading()
# my_car.odometer = 10
# my_car.odometer_reading()
# my_car.update_odometer(8)
# my_car.update_odometer(12)
# my_car.fill_gas()
#
# # ----------------------------------------------------------------------------------------------------------------------
#
#
# class ElectricCar(Car):
# # The __init__() Method for a Child Class
# # When you’re writing a new class based on an existing class, you’ll often want to call the __init__() method from the
# # parent class. This will initialize any attributes that were defined in the parent __init__() method and make them
# # available in the child class.
# # The super() function is a special function that allows you to call a method from the parent class. This line tells
# # Python to call the __init__() method from Car, which gives an ElectricCar instance to all the attributes defined in
# # that method.
#
# # this __init__() method takes in the information required to make a Car instance.
#     def __init__(self, name, model, year, battery_size):
#         super().__init__(name, model, year)
#
#         # defining new attributes and methods for child class
#         self.battery_size = battery_size
#
#     def describe_battery_size(self):
#         print(f"This car has a {self.battery_size}-kW battery.")
#
# # --------------------------------------------------------------------------------------------------------------------
# # method overriding
# # --------------------------------------------------------------------------------------------------------------------
# # You can override any method from the parent class that does not fit what you’re trying to model with the child class.
# # You just define a method in the child class with the same name as the method you want to override in the parent class.
# # Python will disregard the parent class method and only pay attention to the method you define in the child class.
#     def fill_gas(self):
#         print("no need to fill gas since this is electric car.")
#     # if you wish to call same method from parent class you can use super() method.
#         super().fill_gas()
#
# # When you use inheritance, you can make your child classes retain what you need and override anything you don’t need
# # from the parent class.
#
#
# my_tesla = ElectricCar('tesla', 'model-s', 2022, 75)
# description = my_tesla.describe_vehicle()
# print(description)
# my_tesla.describe_battery_size()
# my_tesla.fill_gas()

# ----------------------------------------------------------------------------------------------------------------------
# Instances as Attributes
# ----------------------------------------------------------------------------------------------------------------------

# class Battery:
#     def __init__(self, battery_size = 75):
#         self.battery_size = battery_size
#
#     def describe_battery_size(self):
#         print(f"This car has a {self.battery_size}-kW battery.")
#
#     def get_range(self):
#         if self.battery_size == 75:
#             limit = 260
#         elif self.battery_size == 100:
#             limit = 300
#         print(f"range of this car is {limit} KM")
#
#
# class ElectricCar(Car):
#     def __init__(self, name, model, year):
#         super().__init__(name, model, year)
#         self.battery_size = Battery()
#
#     def fill_gas(self):
#         print("no need to fill gas since this is electric car.")
#
#
# my_tesla = ElectricCar("audy", "a-4", 2022)
# my_tesla.battery_size.describe_battery_size()
# my_tesla.battery_size.get_range()

# ------------------------------------------------------------------------------------------------------------------------
# super() - super method is a special method that calls method from parents class to child class.
# it is helpful in method overriding concept.
# ------------------------------------------------------------------------------------------------------------------------


# class Bird:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is a bird.")
#
#     def fly(self, name):
#         self.name = name
#         print(f"{self.name} can fly.")
#
#
# class Parrot(Bird):
#     def __init__(self, name):
#         self.name = name
#         print(f"This bird's name is {self.name}.")
#         super().__init__(name)               # calling constructor of class Bird from Parrot (child) class.
#         super().fly(name)                    # calling fly method of class Bird from Parrot (child) class.
#
#
# p = Parrot("parrot")

# ------------------------------------------------------------------------------------------------------------------------
# Types of Inheritance :
# ------------------------------------------------------------------------------------------------------------------------


# 1. Single Inheritance : If a class derived from single base class is called Single Inheritance.

# class A:
#     a = 100
#     def show(self):
#         print("show method")
#
#
# class B(A):
#     def disp(self):
#         print("disp method")
#
#
# b = B()
# print(b.a)
# b.show()
# b.disp()
# ------------------------------------------------------------------------------------------------------------------------
# 2. Multilevel Inheritance : If a class inherits features from another child class is called Multilevel Inheritance.
#
# class A:
#     a = 100
#     def __init__(self):
#         print("class A constructor")
#     def show(self):
#         print("show method")
#
#
# class B(A):
#     def __init__(self):
#         print("class B constructor")
#     def disp(self):
#         print("disp method")
#
#
# class C(B):
#     def __init__(self):
#         print("class C constructor")
#     def disp2(self):
#         print("disp2 method")
#
#
# c = C()            # initialising object of class C
# print(c.a)
# c.show()
# c.disp()
# c.disp2()


# # -----------------------------------
#
# class A:
#     a = 100
#     def __init__(self):
#         print("class A constructor")
#     def show(self):
#         print("show method of class A")
#
#
# class B(A):
#     def __init__(self):
#         print("class B constructor")
#     def show(self):
#         print("show method of class B")
#     def show1(self):
#         print("show1 method of class B")
#
#
# class C(B):
#     def __init__(self):
#         print("class C constructor")
#     def show(self):
#         super(C, self).show()      # calls specified method from immediate parent class i.e. here C's parent class is B
#         super(C, self).show1()
#         super(B, self).show()      # calls specified method from immediate parent class i.e. here B's parent class is A
#         print("show method of class C")
#
# c = C()
# c.show()

# # -----------------------------------
#
# class A:
#     a = 100
#     def __init__(self):
#         print("class A constructor")
#     def show(self):
#         print("show method")
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()              # calling class A constructor
#         print("class B constructor")
#     def disp(self):
#         print("disp method")
#
#
# class C(B):
#     def __init__(self):
#         super().__init__()              # calling class B constructor
#         print("class C constructor")
#     def disp2(self):
#         print("disp2 method")
#
#
# c = C()            # initialising object of class C
# print(c.a)
# c.show()
# c.disp()
# c.disp2()

# ------------------------------------------------------------------------------------------------------------------------
#
# 3. Hierarchical Inheritance : If multiple child classes derived from single parent class is called Hierarchical
#                               Inheritance

#
# class A:
#     a = 100
#     def __init__(self):
#         print("class A constructor")
#     def show(self):
#         print("show method")
#
#
# class B(A):
#     def __init__(self):
#         print("class B constructor")
#     def disp1(self):
#         print("disp1 method")
#
#
# class C(A):
#     def __init__(self):
#         print("class C constructor")
#     def disp2(self):
#         print("disp2 method")
#
#
# b = B()
# c = C()
# b.show()
# b.disp1()
# c.show()
# c.disp2()
#
# # -------------------------

# class A:
#     a = 100
#     def __init__(self):
#         print("class A constructor")
#     def show(self):
#         print("show method")
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()              # calling class A constructor
#         print("class B constructor")
#     def disp1(self):
#         print("disp1 method")
#
#
# class C(A):
#     def __init__(self):
#         super().__init__()              # calling class B constructor
#         print("class C constructor")
#     def disp2(self):
#         print("disp2 method")
#
#
# b = B()
# c = C()
# b.show()
# b.disp1()
# c.show()
# c.disp2()
#
# # ------------------------------------------------------------------------------------------------------------------
#
# # 4. Multiple Inheritance :

# class Animal:
#     def __init__(self, Animal):
#         print(Animal, 'is an animal.')
#
# #
# class Mammal(Animal):
#     def __init__(self, mammalName):
#         print(mammalName, 'is a warm-blooded animal.')
#         super().__init__(mammalName)
#
# class NonWingedMammal2(Mammal):
#     def __init__(self, NonWingedMammal2):
#         print(NonWingedMammal2, "can't fly in sky.")
#         super().__init__(NonWingedMammal2)
#
#     def showAnimal(self, animal):
#         self.animal = animal
#         print(animal)
#
# class NonWingedMammal(Mammal):
#     def __init__(self, NonWingedMammal):
#         print(NonWingedMammal, "can't fly.")
#         super().__init__(NonWingedMammal)
#
#
# class NonMarineMammal(Mammal):
#     def __init__(self, NonMarineMammal):
#         print(NonMarineMammal, "can't swim.")
#         super().__init__(NonMarineMammal)
#
#
# class Dog(NonMarineMammal, NonWingedMammal, NonWingedMammal2):
#     def __init__(self):
#         print('Dog has 4 legs.')
#         super().__init__('Dog')
#
#
# d = Dog()
# print('')
# bat = NonMarineMammal('Bat')
# d.showAnimal("Cat")
# print(Dog.__mro__)
# print(NonWingedMammal.__mro__)

# Method Resolution Order (MRO)
# MRO is the order in which methods should be inherited in the presence of multiple inheritance.
# You can view the MRO by using the __mro__ attribute.
# Here is how MRO works:
# A method in the derived calls is always called before the method of the base class.
# In our example, Dog class is called before NonMarineMammal or NoneWingedMammal. These two classes are called before
# Mammal, which is called before Animal, and Animal class is called before the object.
# If there are multiple parents like Dog(NonMarineMammal, NonWingedMammal), methods of NonMarineMammal is invoked first
# because it appears first.


# # -----------------------------------------------------------------------------------------------------------------


# class Game:
#     def __init__(self, game):
#         self.game = game
#         print(self.game, "is very popular game.")
#
#
# class IndoorGame(Game):
#     def __init__(self, IndoorGame):
#         print(IndoorGame, "is part of game.")
#         super().__init__(IndoorGame)
#
#
# class OutdoorGame(Game):
#     def __init__(self, OutdoorGame):
#         print(OutdoorGame, "is played on open ground.")
#         super().__init__(OutdoorGame)
#
#
# class PopularGame(OutdoorGame, IndoorGame):
#     def __init__(self):
#         print("I love games.")
#         super().__init__("cricket")
#
#
# g = PopularGame()
# print()
# g2 = OutdoorGame("hockey")

# # -----------------------------------------------------------------------------------------------------------------
#
# class Sunil():
#     def __init__(self):
#         super().__init__()
#         print("father constructer")
#     def show(self):
#         print("Father is printed as Sunil patil")
#
# class Chhaya():
#     def __init__(self):
#         super().__init__()
#         print("mother constructer")
#     def seen(self):
#         print("Mother is printed as Chhaya patil")
#
# class Paresh(Sunil,Chhaya):
#     def __init__(self):
#         super().__init__()
#         print("son constructer")
#     def watch(self):
#         print("child is printed as paresh patil")
#
# s=Paresh()
