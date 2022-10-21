# # making an object from class is called instantiation, and we work with instance of class.
# # All classes in python are built from single super class called object class.
#
# class Dog:
#     def bark(self):
#         print("dog is barking")
#
#     def run(self):
#         print("dog is running")
#
# # Making an Instance from a Class
#
#
# dog = Dog()
# # method calling using class and passing object (i.e. instance) as a self argument.
# # we need to call method using class_name.method_name(object_name) ==> this is one way to call method inside class.
# Dog.run(dog)
# Dog.bark(dog)
#
# # ====================================================================================================================

# # the __init__ method is special method that python runs automatically when we create a new instance based on that
# # class. self parameter is required in method definition because when python calls this method later (after creating
# # instance of that class), and method call will automatically pass the self argument.
# # every method call associated with instance automatically passes self, which is reference to instance itself; which
# # gives access for individual instance to use all attributes and methods inside the class.
#
#
# class Man:
#     # defining class variable
#     gender = "male"
# # we can access class variable using class as well as instance. if we change class variable using class, change will
# # reflect throughout the class. And if we change class variable using instance, change will reflect in that particular
# # instance only.
#
#     def __init__(self, name, age):
#         """Initialize the name and age attributes."""
# # any variable prefixed with self is available to every method in class, and we'll be able to access these variable
# # with any instance created from the class.
# # self.name = name takes the value associated with the parameter name and assigns it to the variable name, which is
# # then attached to the instance being created.
# # variables that are accessible through instances are called "attributes".
#         self.name = name
#         self.age = age
#
# # instances we create later will have access to these methods(walk, speak).
#     def walk(self):
#         print(f"Man whose name is {self.name} is walking.")
#         print(f"{self.name} is {self.age} years old.")
#         print(f"his gender is {Man.gender}")
#
#     def speak(self):
#         print(f"Man whose name is {self.name} is speaking.")
#         print(f"{self.name} is {self.age} years old.")
#
#
# # Making an Instance from a Class
#
# # we tell Python to create person whose name is 'Shyam' and whose age is 30. When Python reads this line, it calls
# # the __init__() method in Man with the arguments 'Shyam' and 30. The __init__() method creates an instance
# # representing this particular person and sets the name and age attributes using the values we provided.
# # Python then returns an instance representing this person.
# # We assign that instance to the variable person.
#
# # one can create as many instances from a class
# # here we create two persons named with Shyam and Ravi. Each person has a separate instance with its own set of
# # attributes, capable of doing same set of actions.
# # even if we used the same name and age for the second person, Python would still create a separate instance from
# # the Man class
#
# person = Man("Shyam", 30)
# person1 = Man("Ravi", 25)
#
# # accessing attributes ==> once python find an instance it looks for the attributes associated with it.
# print(f"His name is {person.name} and he is {person.age} years old.")
# print(f"His name is {person1.name} and he is {person1.age} years old.")
#
# # method calling using instance.
# # to call a method, give the name of the instance and the method you want to call, separated by a dot.
# person.walk()
# person1.speak()
# person1.gender = "M"
# print(person.gender)
# print(person1.gender)
# Man.gender = "MALE"
# print(person.gender)
# print(person1.gender)


# # ====================================================================================================================

# # working with classes and instances
# class Car:
#     def __init__(self, make, model, year):
#         """initialize attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
# # Setting a Default Value for an Attribute
#         self.odometer = 0
#
#     def get_descriptive_name(self):
#         """return a neatly formatted descriptive name"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def get_odometer_reading(self):
#         """print statement showing car's mileage"""
#         print(f"my car has {self.odometer} miles on it.")
#
#     def update_odometer(self, mileage):
#         self.odometer = mileage
#
# # we can extend the method update_odometer() to do additional work so that every time odometer reading is modified
# # make sure no one can roll back the odometer reading
#
#     def update_odometer_conditional(self, mileage):
#         if mileage > self.odometer:
#             self.odometer = mileage
#         else:
#             print("you can't roll back an odometer.")
#
#     def increment_odometer(self, mileage):
#         self.odometer += mileage
#
#
# my_car = Car("audy", "a4", 2022)
# print(my_car.get_descriptive_name())
# my_car.get_odometer_reading()
#
# # modifying value of attributes
# # [1] Modifying an Attribute’s Value Directly -- simple way to modify the value of an attribute is to access the
# # attribute directly through an instance
#
# my_car.odometer = 25
# my_car.get_odometer_reading()
#
# # [2] Modifying an Attribute’s Value Through a Method -- instead of accessing the attribute directly, you pass the new
# # value to a method that handles the updating internally and call a method with argument
#
# my_car.update_odometer(22)
# my_car.get_odometer_reading()
#
# my_car.update_odometer_conditional(21)
# my_car.get_odometer_reading()
# my_car.update_odometer_conditional(25)
# my_car.get_odometer_reading()
#
# # [3] Incrementing an Attribute’s Value Through a Method
# # sometimes we need to increment attributes value by certain amount rather than changing whole value.
#
# my_car.increment_odometer(5)
# my_car.get_odometer_reading()


# # ====================================================================================================================
#
# constructor in python
# A constructor is a special type of method (function) which is used to initialize the object.
# it is used to initialize/assign values to the data members of the class when an object of the class is created.
# Constructor definition is executed when we create the object of this class.
# In python, the __init__() method is called as constructor and is always called when an object is created.
#
# How it works
# # ====================================================================================================================

# class Employee:
#     no_of_emps = 0
#     raise_percentage = 1.04
#
#     def __init__(self, name, last, pay):
#         self.name = name
#         self.last = last
#         self.pay = pay
#         self.email = name.lower() + "." + last.lower() + "@gmail.com"
#
#         Employee.no_of_emps += 1
#
#     def get_name(self):
#         return f'{self.name} {self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_percentage)
#
#     @classmethod
#     def set_raise_amt(cls, raise_percentage):
#         cls.raise_percentage = raise_percentage
#
#     @classmethod                                   # this class method work as a constructor
#     def from_string(cls, string):
#         name, last, pay = string.split("-")
#         return cls(name, last, pay)
#
#     @staticmethod
#     def is_weekday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True
#
#
# emp1 = Employee("Prathamesh", "Sawant", 150000)
# emp2 = Employee("Uday", "Sarode", 160000)
#
# print(emp2.email)
# print(emp2.get_name())
# print(emp1.pay)
# print()
# print(Employee.raise_percentage)
# print(emp1.raise_percentage)
# print(emp2.raise_percentage)
# print()
# Employee.raise_percentage = 1.06       # if we change class variable using class, change will reflect throughout
#                                        # class
# print(Employee.raise_percentage)
# print(emp1.raise_percentage)
# print(emp2.raise_percentage)
# print()
# emp1.raise_percentage = 1.10           # if we change class variable using instance, change will reflect only for that
#                                        # instance and it won't get change again if we change class variable using
#                                        # class later
# print(Employee.raise_percentage)
# print(emp1.raise_percentage)
# print(emp2.raise_percentage)
# print()
# Employee.raise_percentage = 1.06
# print(Employee.raise_percentage)
# print(emp1.raise_percentage)
# print(emp2.raise_percentage)
# print()
# Employee.set_raise_amt(1.08)            # accessing class method using class
# print(Employee.raise_percentage)
# print(emp1.raise_percentage)
# print(emp2.raise_percentage)
# print()
# emp2.set_raise_amt(1.09)                # we can also access class method using instance
# print(Employee.raise_percentage)
# print(emp1.raise_percentage)
# print(emp2.raise_percentage)

# ------------------------------------------------------------------------------------------------------------------------
# class method as a constructor
# ------------------------------------------------------------------------------------------------------------------------

# emp_str_1 = 'rohit-patil-150000'
# emp_str_2 = 'aniruddha-gavade-150000'
#
# emp3 = Employee.from_string(emp_str_1)
# print(emp3.email)

# ------------------------------------------------------------------------------------------------------------------------
# static method
# ------------------------------------------------------------------------------------------------------------------------

# instance method automatically passes the instance as first argument and class method automatically passes the class
# as a first argument.
# on the other hand, static method don't pass anything neither instance nor class. In fact, they are just regular
# function but, we include them in class because they have some logical connection with class.

# import datetime
# new_date = datetime.date(2022, 06, 02)
# print(Employee.is_weekday(new_date))

# ----------------------------------------------------------------------------------------------------------------------

# accessing instance method from another class


# class A:
#     def __init__(self):
#         print('constructor of class A')
#
#     def abc(self):
#         print("method abc")
#
#
# class B:
#     def __init__(self):
#         self.a = A()     # you can use self.a instance anywhere in class B to access methods in class A
#         print('constructor of class B')
#         self.a.abc()
#
#     def pqr(self):
#         self.a.abc()
#         print('method pqr')
#
#     def xyz(self):
#         ab = A()    # this ab instance is valid only in xyz method.
#         ab.abc()
#
#
# b = B()
# b.pqr()
# b.xyz()

# ------------------------------

# class A:
#     def __init__(self):
#         self.ab = B()
#         self.ab = C()  # it considers the latest class for instance ab
#         self.ab.abc()
#         print('constructor of class A')
#
#     def abc(self):
#         print("method abc of class A")
#
#
# class B:
#     def __init__(self):
#         print('constructor of class B')
#
#     def abc(self):
#         print('method abc of class B')
#
#
# class C:
#     def __init__(self):
#         print('constructor of class C')
#
#     def abc(self):
#         print('method abc of class C')
#
#
# a = A()

# ------------------------------------------------------------------------------------------------------------------------
# Monkey patching
# ------------------------------------------------------------------------------------------------------------------------

# # Changing the object's attributes and behaviors from outside the class during runtime is called monkey patching.
#
# class Test:
#
#     def method_1(self):
#         print('Testing code')
#
#     def get_data(self):
#         self.method_1()
#
#
# t = Test()
# print('Before monkey patching')
# t.get_data()
#
#
# def method_2(self):
#     print('Testing code from outside')
#
#
# print('After monkey patching')
# Test.method_1 = method_2
#
# t.get_data()
