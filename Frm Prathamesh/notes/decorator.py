# decorator - the decorators are used to modify the behaviour of function
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
#
# def decorator_func(func):
#     print("decorator function1")
#
#     def inner(x, y):
#         print("inner function")
#         return func(x, y)
#
#     print("decorator function2")
#
#     return inner
#
#
# @decorator_func
# def multiply_func(a, b):
#     print(a * b)
#
#
# multiply_func(5, 2)

# ----------------------------------------------------------------------------------------------------------------------
# def decor(func):
#     print("decor")

#     def inner(str1, str2):
#         print("inner")
#         str3 = str1.upper()
#         str4 = str2.capitalize()
#         print("inner2")
#         func(str3, str4)
#     print("decor2")
#     return inner
#
#
# @decor
# def string(a, b):
#     print("string")
#     print(a, b)
#
#
# string("hello !", "good morning")

# ----------------------------------------------------------------------------------------------------------------------
#
# def func(var):              # func(addition(a,b))
#     def inner(a, b):
#         print("enhancing method :")
#         if a < b:
#             a, b = b, a
#             ans = var(a, b)
#             return ans
#     return inner
#
# @func
# def addition(a, b):
#     ans = a / b
#     return ans
#
#
# print(addition(2, 5))  # func(addition(a,b))
# # ----------------------------------------------------------
#
#
# def func(var):
#     def inner(a, b):
#         print("enhancing method :")
#         if a < b:
#             a, b = b, a
#         return var(a, b)
#
#     return inner
#
# @func
# def addition(a, b):
#     ans = a / b
#     print(ans)
#
#
# addition(2, 5)  # func(addition(a,b))


# ----------------------------------------------------------------------------------------------------------------------

# code for testing decorator chaining
# def decor1(func):
#     def inner2():
#         print("inner2")
#         func()
#         # print("inner2")
#
#     return inner2
#
#
# def decor(func):
#     def inner1():
#         print("inner1")
#         func()
#         # print("inner1")
#
#     return inner1
#
#
# @decor1
# @decor
# def num():
#     print("hello")
#
#
# num()

# ----------------------------------------------------------------------------------------------------------------------
# decorator chaining
#
# def decor1(var):         # var = inner2 of decor2
#     def inner1():
#
#         print("=====")
#         print(var())
#         print("=====")
#
#     return inner1
#
#
# def decor2(var):         # var = func ie. decor2(func)
#     def inner2():
#         print("*****")
#         print(var())
#         print("*****")
#         return "hello prathamesh"
#     return inner2         # this inner2 returned to decor2(func)
#
#
# @decor1
# @decor2
# def func():
#     # print(func)
#     # print(decor1)
#     # print(decor2)
#     return "good morning"
#
#
# func()        # decor1(decor2(func))  >>>  decor1(inner2)  >>>  inner1()

# ----------------------------------------------------------------------------------------------------------------------

# import logging
#
#
# def log(func):
#     """
#     Log what function is called
#     """
#     def wrap_log(*args, **kwargs):
#         name = func.__name__
#         logger = logging.getLogger(name)
#         logger.setLevel(logging.INFO)
#
#         # add file handler
#         fh = logging.FileHandler("%s.log" % name)
#         fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#         formatter = logging.Formatter(fmt)
#         fh.setFormatter(formatter)
#         logger.addHandler(fh)
#
#         logger.info("Running function: %s" % name)
#         result = func(*args, **kwargs)
#         logger.info("Result: %s" % result)
#         return func
#     return wrap_log
#
#
# @log
# def double_function(a):
#     """
#     Double the input parameter
#     """
#     return a*2
#
#
# if __name__ == "__main__":
#     value = double_function(2)
#     print(value)

# ----------------------------------------------------------------------------------------------------------------------
# PROPERTY DECORATOR
# ----------------------------------------------------------------------------------------------------------------------
#
# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = f'{self.first}.{self.last}@gmail.com'
#
#     def full_name(self):
#         return f'{self.first} {self.last}'
#
#
# emp_1 = Employee('John', 'Smith')
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.full_name())
# print('-------------------------------------')
#
# # but if we change first name then first name will change but email will take old first name
# this is because if we change a value of an attribute of a class then other attributes which are derived from that
# class won't automatically update.

# emp_1.first = 'Tim'
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.full_name())
# print('-------------------------------------')
#
# here @property decorator comes into picture
# property decorator allow us to define a method, but we can access it as an attribute

# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def full_name(self):
#         return f'{self.first} {self.last}'
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@gmail.com'
#
#
# emp_1 = Employee('John', 'Smith')
# emp_1.first = 'Will'
# print(emp_1.first)
# print(emp_1.email)     # here we are accessing a method just like we can access an attributes
# print(emp_1.full_name())
# print('-------------------------------------')
#
# # now if we want to change the name of person then every time we need to call that method and pass new attributes
# emp_1.first = 'Virat'
# emp_1.last = 'Kohli'
# print(emp_1.full_name())
# print('-------------------------------------')


# here setter method comes into picture
# using setter method we can change the name very easily, and even we can validate our code
# for that we use decorator @method_name.setter and define setter method with same name

# ----------------------------------------------------------------------------------------------------------------------
# # @property decorator acts like getter, setter and deleter
# ----------------------------------------------------------------------------------------------------------------------

# #  We use getters & setters to add validation logic around getting and setting a value.
# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@gmail.com'
#
#     @property
#     def full_name(self):
#         return f'{self.first} {self.last}'
#
#     @full_name.setter
#     def full_name(self, name):
#         first, last = name.split(' ')
#         # here we validate the code, if length of first and last is greater than or equal to 4 characters then only
#         # set the first and last attributes
#         if len(first) >= 4 and len(last) >= 4:
#             self.first = first
#             self.last = last
#
#
# emp_1 = Employee('John', 'Smith')
# print(emp_1.full_name)
# print('-------------------------------------')
#
# # here we can change all the attributes using @property decorator
# emp_1.full_name = 'Kim Jeo'
# print(emp_1.full_name)
# emp_1.full_name = 'Virat Kohli'
# print(emp_1.full_name)

# ----------------------------------------------------------------------------------------------------------------------
# encapsulation using @property decorator
# ----------------------------------------------------------------------------------------------------------------------

# class Exam:
#     def __init__(self, marks):
#         self.__marks = marks
#
#     @property
#     def percent(self):
#         return (self.__marks / 600) * 100
#
#     @property
#     def get_marks(self):
#         return self.__marks
#
#     @percent.setter
#     def percent(self, value):
#         if 0 <= value <= 600:
#             self.__marks = value
#         else:
#             print('Invalid input')
#
#
# e = Exam(500)
# print(e.get_marks)
# print(e.percent)
# print('----------------------')
# e.percent = 550
# print(e.get_marks)
# print(e.percent)
# print('----------------------')
# e.percent = 650
# print(e.get_marks)
# print(e.percent)


# def method1(var):
#     def inner1():
#         print("-------")
#         print(var())
#         print('-------')
#     return inner1
#
#
# def method2(var1):
#     def inner2():
#         print('=======')
#         print(var1())
#         print('=======')
#         return 'hello Prathamesh'
#     return inner2
#
# @method1
# @method2
# def meinFunc():
#     return "Good Morning !"
#
# meinFunc()

# ==============================================================================================================
# def outer(var):
#     print('enhancing method')
#
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#             ans = var(a, b)
#             print(f'{ans}')
#     return inner
#
#
# @outer
# def add(x, y):
#     return x / y
#
#
# add(3, 10)

# def func(var):              # func(addition(a,b))
#     def inner(a, b):
#         print("enhancing method :")
#         if a < b:
#             a, b = b, a
#             ans = var(a, b)
#             return ans
#     return inner
#
# @func
# def addition(a, b):
#     ans = a / b
#     return ans
#
#
# print(addition(2, 5))  # func(addition(a,b))
# ______________________________________________________________________________________________________________________

# def display_info(func):
#
#     def inner():
#         print("Executing", func.__name__, "function")
#         func()
#         print("finish executing")
#
#     return inner
#
#
# @display_info
# def printer():
#     print("hello world !")
#
#
# printer()
# ______________________________________________________________________________________________________________________

# Invoicing system.

# def decor_invoice(func):
#     def wrap(num):
#         print("***")
#         func(num)
#         print("***")
#         print("END OF PAGE")
#     return wrap
#
#
# @decor_invoice
# def invoice(num):
#     print("Invoice no: ", num)
#
# invoice(input("Enter the invoice number: "))

# ______________________________________________________________________________________________________________________

# def decor(fib_):
#     def inner():
#         b = fib_()
#         for i in b:
#             if i > 100:
#                 break
#             print(i)
#     return inner
#
#
# @decor
# def fib_():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b
#
#
# fib_()
