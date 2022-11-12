# string function

# capitalize

# s = "team brainworks"
# s = s.capitalize()
# print(s)

# Upper
# s = "team brainworks"
# s = s.upper()
# print(s)

# Lower case
# s = "TEAM BRAINWORKS"
# s = s.lower()
# print(s)

# title()
# name = "aniruddha gavade"
# name = name.title()
# print(name)

# casefold()
# str_ = "Python is | language # @"
# str_ = str_.casefold()
# print(str_)

# swapcase()
# str_ = "Python is a programming language, PYTHON is used for Machine learning"
# str_ = str_.swapcase()
# print(str_)

# strip()
# str_ = " Python Developer  "
# str_ = str_.strip()
# print(str_)

# lstrip()
# str_ = " Python Developer  "
# str_ = str_.lstrip()
# print(str_)

# rstrip()
# str_ = " Python Developer  "
# s1 = str_.rstrip()
# print(s1)

# replace()
# str_ = "Hello python developers and java developers"
# a = str_.replace("python", "Data science").replace("developers", "students")
# print(a)

# str1 = "Python is programming language, Python have most libraries, Python is used for machine learning"
# str_ = str1.replace("P", "J", 2)
# print(str_)

# Count()
# s1 = "hello python programmer"
# s = s1.count("h")
# print(s)

# s = "hello hython hacker"
# s1 = s.count("h", 0, 2)
# print(s1)

# index()
# index(substring, [start, end indx])
# s1 = "welcome to goa singham"
# str_ = s1.index("goa", 1, -1)
# print(str_)

# # endswith()
# str_ = "welcome to team brainworks"
# a = str_.endswith("s")
# print(a)

# # startswith()
# str1 = "Hello, python developers."
# a = str1.startswith("H")
# print(a)

# # Split()
# a = "We are python developers at team brainworks"
# a.split(
#


# # Tuple function
# 1. count()
# tup_ = (3, 5, 7, 2, 1, 8, 3, 4, 2, 7, 6)
# x = tup_.count(3)
# print(x)

# 2. index()
# tup_ = (3, 5, 7, 2, 1, 8, 3, 4, 2, 7, 6)
# x = tup_.index(2)
# print(x)

# 3. len()
# tup_ = (3, 5, 7, 2, 1, 8, 3, 4, 2, 7, 6)
# x = len(tup_)
# print(x)

# 4. min()
# tup_ = (3, 5, 7, 2, 1, 8, 3, 4, 2, 7, 6)
# x = min(tup_)
# print(x)

# 5. max()
# tup_ = (3, 5, 7, 2, 1, 8, 3, 4, 2, 7, 6)
# x = max(tup_)
# print(x)

# 6. copy()  # 'tuple' object has no attribute 'copy'
# tup_ = (3, 5, 7, 2, 1, 8, 3, 4, 2, 7, 6)
# a = tup_.copy()
# print(a)

# x = 0
# while x <= 18:
#     x = x + 3
# print(x)
# ______________________________________________________________________________________________________________________


# lst = [-2, -1, 0, 1, -2, 3, 4, -3, 2]
# print(sorted(lst, key=abs))

# o/p = [0, -1, 1, -2, -2, 2, -3, 3, 4]

# lst_ = sorted(lst)
# print(lst_)
# ______________________________________________________________________________________________________________________

"""Key funxtions.
Both list.sort() and sorted have a key parameter to specify a function (or other callable)
to be called on each list elements prior to making comparisons.
For example, here's a case-insensitive string comparison:"""

# a = sorted("This is a test string from Andrew".split(), key=str.lower)
# print(a)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # A common pattern is to sort complex objects using of the object's indices as keys. For example:

# student_tuples = [
#     ("john", "A", 15),
#     ("dave", "B", 12),
#     ("jane", "B", 10)
# ]
# sort_ = sorted(student_tuples, key=lambda x: x[0])
# print(sort_)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# The same technique works for objects with named attributes. For example:


# class Students:
#     def __init__(self, name, grade, age):
#         self.name = name
#         self.grade = grade
#         self.age = age
#
#     def __repr__(self):
#         return repr((self.name, self.grade, self.age))
#
#
# student_tuples = [
#     Students("john", "A", 15),
#     Students("dave", "B", 12),
#     Students("jane", "B", 10)
# ]
#
#
# a = sorted(student_tuples, key=lambda x: x.age)
# print(a)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Using those functions, the above examples become simpler and faster.
# from operator import itemgetter
#
#
# student_tuples = [
#     ("john", "A", 15),
#     ("dave", "B", 12),
#     ("jane", "B", 10)
# ]
# a = sorted(student_tuples, key=itemgetter(2))
# print(a)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# import matplotlib.pyplot as plt
#
#
# col = 10
# row = 10
# nested_list = [[0]*col]*row
# print(nested_list)
#
# nested_list[0][9] = 1
# plt.imshow(nested_list)
# plt.show()
# ______________________________________________________________________________________________________________________

# Find the unique element(s) from a given list that only occurs once by using list comprehension.

# a = [2, 4, 4, 3, 5, 2, 3, 9, 8, 7, 6]
# print(type(*[x for x in a if a.count(x) == 1]))
# print([x for x in a if a.count(x) == 1])

# print(", ".join(str(x) for x in a if a.count(x) == 1))

# for i in a:
#     if a.count(i) == 1:
#         print(i)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# By using function with for loop

# def lonely_int(a):
#     for i in a:
#         if a.count(i) == 1:
#             result = i
#             return result
#
#
# v = [2, 4, 4, 3, 5, 2, 3]
# print(lonely_int(v))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# By using list comprehension in function

# def lonely_int(a):
#     result = [x for x in a if a.count(x) == 1]
#     for i in result:
#         return i
#
#
# v = [2, 4, 4, 3, 5, 3, 2]
# print(lonely_int(v))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# By using list comprehension and join in function.

# def lonely_int(a):
#     result = [str(x) for x in a if a.count(x) == 1]
#     return "\n".join(result)
#
#
# v = [2, 3, 4, 4, 5, 2, 3, 9]
# print(lonely_int(v))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# By using join and list comprehension in one line. # MASTER SOLUTION.

# def lonely_int(a):
#     return ", ".join(str(x) for x in a if a.count(x) == 1)
#
#
# v = [2, 4, 4, 3, 5, 3, 2, 9]
# print(lonely_int(v))
# ______________________________________________________________________________________________________________________


# def even_num(n):
#     if n < 2:
#         return n % 2 == 0
#     return even_num(n - 2)
#
#
# n = int(input("enter the number: "))
# if even_num(n):  # The true value of the bool type. Assignments to True are illegal and raise a SyntaxError.
#     # pass the number as an argument to the recursive function
#     print(n, "This is even number")
#
# else:
#     print(n, "This is odd number")
# ______________________________________________________________________________________________________________________

# for i, j in zip(range(1, 6), range(4, -1, -1)):
#     print(" " * (5 - i) + j*'* ' + i*'$ ')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# n = 5
# for i in range(1, n+1):
#     print(" " * (n - i) + "* " * (n-i) + "$ " * i)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# for i in range(5):
#     print(" " * (5 - i) + "* "*(5-(i+1)) + "$ "*(i+1))
# ______________________________________________________________________________________________________________________

# # Print first 10 natural numbers by using for loop and while loop

# # By using for loop
# for i in range(1, 11):
#     print(i)

# # By using while loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# ______________________________________________________________________________________________________________________

# # Print the following pattern.
#
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5
#
# n = 5
# for i in range(1, n + 1, 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print("")
# ______________________________________________________________________________________________________________________

# # Calculate the sum of all numbers from 1 to a given number
#
# product = [i for i in range(1, 11)]
# print("The sum of given range is: ", sum(product))
#
# from functools import reduce
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst_ = reduce(lambda x, y: x + y, a)
# print("The sum of given list is: ", lst_)
# ______________________________________________________________________________________________________________________

# # Write a program to print multiplication table of a given number
#
# n = 2
# s = [n*x for x in range(1, 11)]
# print(s)

# n = 3
# for i in range(1, 11, 1):
#     prod_ = n * i
#     print(prod_)
# ______________________________________________________________________________________________________________________

# # Display numbers from a list using loop
#
# lst_ = [12, 75, 150, 180, 145, 525, 50]
# for i in lst_:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)
# ______________________________________________________________________________________________________________________

# Count the total number of digits in a number

# num = 3456546891
# count = 0
# while num != 0:
#     num = num // 10
#     count += 1
# print("The total number of digit in the number is: ", count)
# ______________________________________________________________________________________________________________________

# Print the following pattern

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


# ______________________________________________________________________________________________________________________
# # Program to reverse the number
#
#
# # By using if else statement
#
# number = 6876378
# reversed_number_string = str(number)[:: - 1]
# if type(number) == float:
#     reversed_number = float(reversed_number_string)
# elif type(number) == int:
#     reversed_number = int(reversed_number_string)
# print(reversed_number)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# BY USING WHILE LOOP

# number = 678901
# reversed_number = 0
# while number != 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number //= 10
#
# print(reversed_number)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # By using function
#
# def reverse(num):
#     str_ = str(num)
#     str_new = str_[::-1]
#     ans = int(str_new)
#     return ans
#
#
# num = int(input("enter the number: "))
# print(reverse(num))
# ______________________________________________________________________________________________________________________

# instance variable
# class Student:
#     school = 'brainworks'
#
#     def __init__(self, rollno, name):
#         self.rollno = rollno
#         self.name = name
#
#     def show(self):
#         print("",self.rollno)
#         print("",Student.school)
#
#
# s1=Student(12,'ani')
# s1.show()
#
# s2=Student(23,'pra')
# s2.show()
#
# print(s1.school)
# print(Student.school)
# print(s2.school)


# class Ankit:
#     a = 10
#
#     def show(self):
#         print(Ankit.a)
#
#
# obj1 = Ankit()
# obj2 = Ankit()
# obj3 = Ankit()
#
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
#
# obj2.a = 50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
#

# class Ankit:
#     def __init__(self):
#         self.a = 10
#
#     def show(self):
#         print(self.a)
#
#
# obj1 = Ankit()
# obj2 = Ankit()
# obj3 = Ankit()
#
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
#
# Ankit.a = 50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
#
# obj4 = Ankit()
# print(obj4.a)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Monster:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     @classmethod
#     def change_name(cls, given_name):
#         cls.name = given_name
#
#
# mon = Monster("Ankur", 33)
# print(mon.name)
# mon.change_name("Ankit")
# print(mon.name)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class disp:
#     x = 10
#
#     def __init__(self):
#         self.y = 20
#
#
# t1 = disp()
# t2 = disp()
# t3 = disp()
# t4 = disp()
# print("----------------------------")
# print(t1.x, t1.y)
# print(t2.x, t2.y)
# print(t3.x, t3.y)
# print(t4.x, t4.y)
# print("----------------------------")
# disp.x = 999
# t2.y = 800
# print(t1.x, t1.y)
# print(t2.x, t2.y)
# print(t3.x, t3.y)
# print(t4.x, t4.y)
# print("-------------------")
# t3.y = 90
# print(t1.x, t1.y)
# print(t2.x, t2.y)
# print(t3.x, t3.y)
# print(t4.x, t4.y)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# creating class and object in python

# class Employee:
#     # class variable
#     company_name = 'Silver Vally'
#
#     # constructor to initialize the object
#     def __init__(self, name, salary):
#         # instance variable
#         self.name = name
#         self.salary = salary
#
#     # instance method
#     def show(self):
#         print("Employee: ", self.name, self.salary, self.company_name)
#
#
# # create first object
# emp1 = Employee('Nitin', 25000)
# emp1.show()
# # create second object
# emp2 = Employee("Sagar", 28000)
# emp2.show()
# ______________________________________________________________________________________________________________________

# def fun(a, l_=[]):
#     l_.append(a)
#     return l_
#
#
# x = fun(1)
# y = fun(2, [])
# z = fun(3)
#
# print(x)
# print(y)
# print(z)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Letter combinations of phone number.
# ______________________________________________________________________________________________________________________

# c = input("Enter the word: ")
# v = c[::-1]
# if v == c:
#     print("The word is palindrome.")
# else:
#     print("The word is not palindrome.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def pal(s):
#     v = s[::-1]
#     if v == s:
#         print("The word is palindrome.")
#     else:
#         print("The word is not palindrome.")
#
#
# s = input("Enter the word: ")
# print(pal(s))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def pal(s):
#     n = len(s)
#     for i in range(n):
#         if s[i] != s[n-i-1]:
#             return "This is not a palindrome number"
#         return "This is a Palindrome word"
#
#
# s_ = input("Enter the word: ")
# print(pal(s_))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def pal(s):
#     temp = ''.join(reversed(s))
#     if s == temp:
#         return True
#     else:
#         return False
#
#
# s_ = input("Enter the word: ")
# print(pal(s_))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ______________________________________________________________________________________________________________________

# list1 = ["a", "b", "y", "d"]
# list2 = [1, 2, 3, 4]
# # result_ = {}
# # for key in list1:
# #     for value in list2:
# #         result_[key] = value
# #         list2.remove(value)
# #         break
# result_ = {list1[i]: list2[i] for i in range(len(list1))}
# print("Dictionary from lists :", result_)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ip = "156469494949"
# # op:: {'1': '5', '5': '6', '6': '4', '4': '6', 6: '9', '9': '4', 4: '9', 9: '4'}
# v = {}
# for indx in range(len(ip)):
#     try:
#         v[ip[indx]] = ip[indx + 1]
#     except:
#         v[ip[indx]] = ip[indx - 1]
#
# print(v)
# ______________________________________________________________________________________________________________________

# l1 = ['a', 'b']
# l2 = ['c', 'd']
# l3 = ['e', 'f']
#
# # op = {'a': [[ {'c': 'e'}, {'c': 'f'}], [{'d': 'e'}, {'d': 'f'}]],
# #     'b': [[{'c': 'e'}, {'c': 'f'}], [{'d': 'e'}, {'d': 'f'}]]}

# ______________________________________________________________________________________________________________________

# ip = "BraiNwoRkS"
# # op = "raiwokBNRS"
# for i in ip:
#     if i.islower():
#         print(i, end="")
# for j in ip:
#     if j.isupper():
#         print(j, end="")


# def sort_(input_):
#     for i in input_:
#         if i.islower():
#             print(i, end="")
#     for j in input_:
#         if j.isupper():
#             print(j, end="")
#
#
# ip = "BraiNwoRkS"
# sort_(ip)

# ip = "BraiNwoRkS"
# lower_ = "".join([x for x in ip if x.islower()])
# upper_ = "".join([y for y in ip if y.isupper()])
# print(lower_+upper_)

# ip = "BraiNwoRkS"
# words = "".join(([i for i in ip if i.islower()]) + ([i for i in ip if i.isupper()]))
# print(words)
# ______________________________________________________________________________________________________________________

# string1 = 'AD44EG2H2J'
# # string1 = 'A3X4Z3'
# # string1 = 'D44j2Jm1'
# list1 = []
# digit_string = ''
# latest_char = None
#
# for ele in string1:
#     if ele.isalpha():
#         if digit_string:
#             def next_char(latest_character, int_string):
#                 ord_latest = ord(latest_character)
#                 ord_sum = ord_latest + int(int_string)
#                 if ord_sum > ord('Z'):
#                     ord_diff = ord_sum - ord('Z')
#                     ord_reminder = ord_diff % 26
#                     next_character = chr((ord('A') - 1) + ord_reminder)
#
#                     return next_character
#                 else:
#                     ord_latest = ord(latest_character)
#                     ord_sum = ord_latest + int(int_string)
#                     next_character = chr(ord_sum)
#                     return next_character
#             next_char = next_char(latest_char, digit_string)
#             list1.append(next_char)
#             digit_string = ''
#         latest_char = ele
#         list1.append(latest_char)
#
#     elif ele.isdigit():
#         digit_string += ele
#
# output = ''.join(list1)
# print(output)
# ___________________________________________________________________________________________

# "it should shift the sentence" ➞ "st ihould shift she tentence"

# str_ = "it should shift the sentence"
# lst_ = str_.split(" ")
# print(str_)
# new_lst = []
# for i in lst_:
#     new_lst.append(i[0])
# v1 = new_lst.pop()
# new_lst.insert(0, v1)
# print(new_lst)

# ________________________________________________________________________________________________

# v = [
#     [1, 2, 4, 3, "a", "b"],
#     [6, "c", 5], [7, "d"],
#     ["f", "e", 8]
]
# # ➞ [
# #   [1, 2, 3, 4, 5, 6],
# #   [7, 8, "a"],
# #   ["b", "c"], ["d", "e", "f"]


# y = [j for i in v for j in i]
# a = []
# b = []
# for x in str(y):
#     if x.isdigit():
#         a.append(x)
#     elif x.isalpha():
#         b.append(x)
# l1 = (sorted(a)+sorted(b))
# l2 = (l1[:6], l1[6:9], l1[9:11], l1[11:14])
# print(l2)


v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [x for x in v if x%2]
print(c)