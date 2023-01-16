# # string permutation
# # from itertools import permutations as permute
#
#
# def str_permutation(s, i, n):
#     if i == n:
#         print("".join(s))
#     else:
#         for j in range(i, n):
#             s[i], s[j] = s[j], s[i]
#             str_permutation(s, i+1, n)
#             s[i], s[j] = s[j], s[i]
#
#
# a = "day"
# x = len(a)
# s = list(a)
# print(str_permutation(s, 0, x))
# ======================================================================================================================

# Check the string is permuted or not?


# str_1 = "aniruddha gavade"
# str_2 = "ahddurina edavag"
#
#
# def is_permutation(str_1, str_2):
#     str_1 = str_1.replace(" ", "")
#     str_2 = str_2.replace(" ", "")
#     if len(str_1) != len(str_2):
#         return False
#     for i in str_1:
#         if i in str_2:
#             str_2 = str_2.replace(i, "")
#     return len(str_2) == 0
#
#
# print(is_permutation(str_1, str_2))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# decorator

# def upper():

# def uppercase(fun):
#     def wrapper():
#         res = fun()
#         modified = res.upper()
#
#         return modified
#
#     return wrapper
#
#
# @uppercase
# def gen_message():
#     return 'Hello there!'
#
#
# msg = gen_message()
# print(msg)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def decor1(func1):
#     def check():
#         print("Lets check")
#         func1()
#         print("Here")
#     return check
#
# @decor1
# def data():
#     print("It exist")
#
# data()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def deco(func):
#     def exec():
#         print("Now executing")
#         func()
#         print("Executed")
#     return exec
#
#
# @deco
# def who_is_developer():
#     print("I am developer")
#
#
# who_is_developer()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def decor1(func):
#     def inner1():
#         print("inner1")
#         func()
#         print("inner1***")
#     return inner1
#
#
# def decor2(func):
#     def inner2():
#         print("inner2")
#         func()
#         print("inner2***")
#     return inner2
#
#
# @decor2
# @decor1
# def num():
#     print("Hello")
#
#
# num()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Operators in pyton
# 1. arithmetic operators.
# 2. Assignment operators.
# 3. Comparison operators.
# 4. Logical operators.
# 5. Identity operators.
# 6. Membership operators.
# 7. Bitwise operators.

# 1. arithmetic operators.
# using mathematical terms. eg. +, -, *, /, **, //, %
# + is use for sum of two values and concatenate two strings.
# - is use for subtraction
# * is use for multiplication
# / is use for divide.
# ** is use for power of the value.
# // is use for floor division.
# % is use for modulus.

# 2. Assignment operator.
# Operator      Example     Same As
#    =           x = 5       x = 5
#    +=         x += 3      x = x + 3
#    -=         x -= 3      x = x - 3

# 3. Comparison Operator.
# Operator              Example             Same As
#   ==                   Equal              x == y
#   !=                 Not Equal            x != y
#   >                 Greater than          x > y
#   <                   Less than           x < y
#   >=          Greater than or equal to     x >= y
#   <=          Less than or equal to        x >= y

# 4. Logical operators.
# Operator                     Example                             Same As
#   and         Return True if both statements are True         x<5 and x>10
#   or          Return True if one of the statement is True     x<5 or x<4
#   not         reserves the result, returns False if True.     not(x<5 and x>10)

# 5. Membership Operator.
# Operator                    Description                          Example
#    in         returns True if sequence with the specified         x in y
#                     value is present in the object
#  not in       Returns True if a sequence with the specified     x not in y
#                     value is not present in the object

# 6. Identity Operator.
# Operator                      Description                              Example
#    is         Returns True if both variables are the same object        x is y
#  is not       Returns True if both variables are not the same object    x is not y

# 7. Bitwise Operator
# Operator      Name        Description
#    &          AND           x & y
#    |          OR            x | y
#    ^          XOR           x ^ y
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Data types.
# 1. Numeric
#     1.1. Integers
#     1.2. Float
#     1.3. Complex
# 2. Sequence.
#     2.1. List
#     2.2. Tuple
#     2.3. string
# 3. Dict
# 4. Set


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # String function
# # Capitalize()
#
# str_ = "aniruddha"
# a = str_.capitalize()
# print(a)

# # uppercase()
# str_ = "aniruddha"
# a = str_.upper()
# print(a)

# # lowecase()
# str_ = "ANIRUDDHA"
# a = str_.lower()
# print(a)

# # title()
# # str_ = "aniruddha"
# str_ = "ANIRUDDHA"
# a = str_.title()
# print(a)

# # casefold()
# str_ = "ANIRUDDHA"
# a = str_.casefold()
# print(a)

# # swapcase():
# str_ = "Hello amigos, How are You"
# a = str_.swapcase()
# print(a)

# # strip()
# a = " Aniruddha "
# s = a.strip()
# print(s)

# # rstrip()
# a = " Aniruddha "
# s = a.rstrip()
# print(s)

# # lstrip()
# a = " Aniruddha "
# s = a.lstrip()
# print(s)

# # replace()
# a = "Hello their we are looking for new developer."
# s = a.replace("Hello", "Hey")
# print(s)

# # count()
# a_ = "Hello their we are looking for new developer."
# s = a_.count("e")
# print(s)

# a = "Hello their we are looking for new developer."
# s = a.count("e", 4, 15)
# print(s)

# # index()
# # index(substring, start, end index)
# a = "Hello their we are looking for new developer."
# s = a.index("we", 3, 15)
# print(s)

# # endswith()
# a = "Hello their we are looking for new developer."
# s = a.endswith("w")
# print(s)

# # startswith()
# a = "Hello their we are looking for new developer."
# s = a.startswith("h")
# print(s)

# # split()
# a = "Hello their we are looking for new developer."
# s = a.split()
# print(s)
# print(type(s))

# # find()
# a = "Hello their we are looking for new developer."
# s = a.find()
# print(s)

# # isalnum()
# s = "1python"
# a = s.isalnum()
# print(a)

# # isalpha()
# s = "python"
# a = s.isalpha()
# print(a)
# print(type(a))

# # isdecimal()
# s = "1698"
# a = s.isdecimal()
# print(a)

# # isdigit()
# s = "16.98"
# a = s.isdigit()
# print(a)

# # istitle()
# s = "python"
# a = s.istitle()
# print(a)

# # isnumeric()
# s = "1698"
# a = s.isnumeric()
# print(a)

# # center()
# s = "1698"
# a = s.center(12, "*")
# print(a)

# # join()
# a = ("ani", "rud", "dha")
# s = "".join(a)
# print(s)

# a = "Aniruddha"
# b = "Gavade"
# s = " ".join([a, b])
# print(s)
# print(type(s))

# dict_ = {"name": "Aniruddha", "City": "Pune", "State": "Maharashtra"}
# separator_ = "/"
# ans = separator_.join(dict_)
# print(ans)

# # List function (methods)
# # append()
# fruits = ["apple", "banana", "Cherry"]
# fruits.append("Jackfruit")
# print(fruits)

# fruits = ["apple", "banana", "Cherry"]
# vegetables = ["Methi", "Coriander", "Lal_math"]
# fruits.append(vegetables)
# print(fruits)

# # extend()
# fruits = ["apple", "banana", "Cherry"]
# vegetables = ["Methi", "Coriander", "Lal_math"]
# fruits.extend(vegetables)
# print(fruits)

# # sort()
# fruits = ["apple", "banana", "Cherry"]
# fruits.sort()
# print(fruits)

# fruits = ["apple", "banana", "Cherry"]
# fruits.sort(reverse=True)
# print(fruits)


# def func(num):
#     return len(num)
#
#
# fruits = ["apple", "banana", "cherry"]
#
# fruits.sort(reverse=True, key=func)
# print(fruits)


# def func(e):
#     return e["Year"]
#
#
# cars = [
#     {"car": "Ford", "Year": 2005},
#     {"car": "Audi", "Year": 2015},
#     {"car": "VW", "Year": 2019},
#     {"car": "BMW", "Year": 2011},
# ]
# cars.sort(key=func)
# print(cars)

# # sorted()
# a = ("b", "g", "a", "d", "f", "c", "h", "k")
# x = sorted(a)
# print(x)

# decorator
# it is just a function that takes another function as argument, add some functionality
# and then returns another function.

def decorator_func(func):
    def wrapper_func():
        print("Wrapper function work")
        return func
    return wrapper_func()


@decorator_func
def main():
    print("This is  work of decorator")


main()
