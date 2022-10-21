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
# b = a.split()
# print(b)

# a = "We are python developers at team brainworks"
# b = a.split("developers")
# print(b)

# # find()
# txt = "We are python developers at team brainworks"
# x = txt.find("o")
# print(x)

# txt = "We are python developers at team brainworks"
# x = txt.find("e", 2, 10)
# print(x)

# txt = "We are python developers at team brainworks"
# print(txt.find("z"))

# # isalnum()
# s1 = "data cloud"
# s1_ = s1.isalnum()
# print(s1_)

# # isdecimal()
# s = '12356346'
# print(s.isdecimal())

# # isdigit()
# nn = '12235756'
# print(nn.isdigit())

# # islower()
# n = 'data engineer'
# print(n.islower())

# # isupper()
# n = 'PYTHON DEVELOPER'
# print(n.isupper())

# # istitle()
# a = "345Working As professional"
# print(a.istitle())

# # isnumeric()
# s = "123556sa"
# print(s.isnumeric())

# # center()
# s = "python class"
# v = s.center(22, "V")
# print(v)

# # join()
# s1 = ("peter", "england", "tom", "holland")
# x = "@".join(s1)
# print(x)

# m1 = {"name": "Ankur", "surname": "Solwande", "car": "BMW"}
# s1 = "Brand "
# x = s1.join(m1)
# print(x)

# # zfill()
# str_ = '789346'
# x = str_.zfill(10)
# print(x)

# # rfind()
# txt = "well its fine at all."
# x = txt.rfind("at")
# print(x)

# # rpartition()
# txt = "I could eat apples all day, apples are my favourite fruit"
# x = txt.rpartition("apples")
# print(x)


# # List function
# 1. append()
# fruits = ["apple", "banana", "cherry"]
# fruits.append("guava")
# print(fruits)

# extend()
# lst_ = [1, 2, 3, 4, 56, 5, 7, 8, 7, 12]
# vsr = ["arfg", "t3qr", "fgqwrg"]
# lst_.extend(vsr)
# print(lst_)

# lang = ["Marathi"]
# lang_tup = ("Urdu", "Gujrati")
# lang_set = {"Bengoli", "Punjabi"}
# lang.extend(lang_tup)
# print("New list of languages: ", lang)
# lang.extend(lang_set)
# print("Newer languages list: ", lang)

# a = [1, 2]
# a2 = [3, 4]
# b = (5, 6)
# a2.extend(b)
# # a2.append(b)
# print(a2)
# print(type(a2))

# # sort()
# cars = ["BMW", "Merc", "RR", "Audi"]
# cars.sort()
# print(cars)

# cars = ["BMW", "Merc", "RR", "Audi"]
# cars.sort(reverse=True)
# print(cars)

# # A function that returns the length of the value:
# def myFunc(e):
#     return len(e)
#
#
# cars = ["bmw", "merc", "audi", "ford"]
# cars.sort(reverse=True, key=myFunc)
# print(cars)

# # A function that returns the 'year' value:
# def myFunc(e):
#     return e['year']
#
#
# cars = [
#     {'car': 'Ford', 'year': 2005},
#     {'car': 'BMW', 'year': 2007},
#     {'car': 'Audi', 'year': 2002},
#     {'car': 'Jaguar', 'year': 2000}
# ]
# cars.sort(reverse=True, key=myFunc)
# print(cars)

# sorted()
# a = ("b", "g", "a", "c", "d", "h", "e")
# x = sorted(a)
# print(x)

# a = ["b", "g", "a", "c", "d", "h", "e"]
# x = sorted(a)
# print(x)

# a = [1, 22, 4]
# x = sorted(a)
# print(x)

# # reverse()
# fruits = ["apple", "jackfruit", "banana", "Cherry"]
# fruits.reverse()
# print(fruits)

# # insert()
# fruits = ["apple", "cherry", "guava", "banana"]
# fruits.insert(len(fruits)//2, "grapes")
# print(fruits)

# # pop()
# fruits = ["apple", "banana", "cherry"]
# fruits.pop()
# print(fruits)

# # remove()
# cars = ["Fiesta", "Harrier", "Creta", "Verna"]
# cars.remove("Creta")
# print(cars)

# cars = ["Fiesta", "Harrier", "Creta", "Verna"]
# del cars[2]
# print(cars)

# count()
# fruits = ["apple", "banana", "cherry", "guava", "banana", "cherry", "banana"]
# count_ = fruits.count("banana")
# print(count_)

# fruits = ["apple", "banana", "cherry", "guava", "banana", "cherry", "banana"]
# count_ = 0
# for i in fruits:
#     count_ = count_ + 1
# print(count_)

# letter = 'a'
# myString = 'aardvark'
# myList = []
#
# for i in myString:
#     myList.append(i)
#
# count = 0
#
# for i in myList:
#     if i == letter:
#         count = count + 1
#
#     else:
#         continue
#
# print(count)

# from collections import Counter
# letter_ = 'a'
# str_ = 'AniruddhaSanjayGavade'
# count_ = Counter(str_)[letter_]
# # print(count_)
# # count_ = count_[letter_]
# print(count_)

# letter_ = 'banana'
# str_ = ["apple", "banana", "cherry", "guava", "banana", "cherry", "banana"]
# count_ = sum(i == letter_ for i in str_)
# print(count_)

# lst_ = [121, 2, 121, 11, 21, 12, 121]
# num_ = 121
# count_ = sum(1 for i in lst_ if i == num_)
# print(count_)

# lst_ = [121, 2, 121, 11, 21, 12, 121]
# num_ = 121
# len_ = list(filter(lambda x: x == num_, lst_))
# count_ = len(len_)
# print(count_)

# letter_ = 'a'
# str_ = 'AniruddhaSanjayGavade'
# len_ = list(filter(lambda x: x == letter_, str_))
# count_ = len(len_)
# print(count_)

# # clear()
# cars = ["Altroz", "Harrier", "Nexon", "Punch", "Tiago"]
# cars.clear()
# print(cars)

# # copy()
# cars = ["Altroz", "Harrier", "Nexon", "Punch", "Tiago"]
# x = cars.copy()
# print(x)

# # index()
# cars = ["Altroz", "Harrier", "Nexon", "Punch", "Tiago"]
# a = cars.index("Punch")
# print(a)

# List comprehension
'''Some of the programming languages have a syntactic construct
list comprehension for creating lists on the basis of existing lists.
Python is such language. In other words, list comprehensions are used for converting
one list into another list or creating a list from other iterables.
A list comprehension consists of:
Input sequence
A variable to store member of input sequence
Predicate expression
Output expression that produces the output list based on the input
sequence and also satisfies the predicate.'''

# [expression for item in list if conditional]
# When compared to a normal Python lists syntax, the above syntax is equivalent to

# for item in list_:
# if conditional:
# expression

# x = [i for i in range(1, 15)]
# print(x)

# cubes_ = [i**3 for i in range(1, 11)]
# print(cubes_)

# lst_ = [2, 4, 7, 5]
# new_lst = [i*2 for i in lst_]
# print(new_lst)

# lst_ = ["this", "is", "python", "tutorial", "from", "intellipaat"]
# new_lst = [i[0] for i in lst_]
# print(new_lst)

# str_ = "this is python tutorial from intellipaat"
# x = str_.split()
# # print(x)
# n = [i[0] for i in x]
# print(n)

# letters_ = []
# for i in 'Intellipaat':
#     letters_.append(i)
# print("letters: ", letters_)

# letters = [letter for letter in "Aniruddha"]
# print(letters)

# list comprehension python vs python lambda functions.

# # Using map() with lambda function
# l_ = list(map(lambda x: x, "Aniruddha"))
# print(l_)

# l_ = [x for x in "Saurabh"]
# print(l_)

# Filter() with lambda function
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
# lst1 = list(map(int, lst1))
# lst_ = filter(lambda x: x % 2, lst1)
# print(list(lst_))

# lst_ = [1, 2, 3, 4, 5, 6, 7, 8]
# lst1 = [x for x in lst_ if x % 2]
# print(list(lst1))

# # reduce() with lambda function
# from functools import reduce
# lst_ = [1, 2, 3, 4, 5]
# n1 = reduce(lambda x, y: x*y, lst_)
# print(n1)

# recursive_lambda = (lambda func: lambda *args: func(func, *args))
# # print(recursive_lambda(lambda self, x: x * self(self, x - 1) if x > 0 else 1)(5))
# # Or, using the function verbatim:
# print(recursive_lambda(lambda a, b: b*a(a, b-1) if b > 0 else 1)(5))

# fact_ = (lambda func: lambda *args: func(func, *args))
# print(fact_(lambda a, b: b*a(a, b-1) if b > 0 else 1)(6))
# print(fact_(lambda self, x: x * self(self, x-1) if x > 0 else 1)(6))

# factorial_ = (lambda func: lambda *args: func(func, *args))
# print(factorial_(lambda x, y: y*x(x, y-1) if y > 0 else 1)(5))
# print(factorial_(lambda self, x: x * self(self, x-1) if x > 0 else 1)(5))

# ______________________________________________________________________________________________________________________


# def double(x):
#     return x * 2
#
#
# my_list = [1, 2, 3, 4, 5, 6]
# n_lst = list(map(double, my_list))
# print(n_lst)

# ----------------------------------------------------------------------------------------------------------------------


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
# ______________________________________________________________________________________________________________________

# Set and frozenset
# containers of distinct elements.
# They are both containers of distinct hashable elements.
"""They can be constructed from other iterables. if you dont know what iterabless are, 
If the iterable contains dupicate elements, they'll be  removed automatically in the constructed set objects."""

# l1 = [3, 6, 8, 9, 3]
# l2 = [4, 2, 6, 8]
#
# l1 = int("".join([str(x) for x in l1]))
# l2 = int("".join([str(x) for x in l2]))
#
# print([int(x) for x in str(l1 + l2)])
# ______________________________________________________________________________________________________________________

# import pyttsx3
#
# book = open(r"book.txt")
# book_text = book.readlines()
# engine = pyttsx3.init()
# for i in book_text:
#     engine.say(i)
#     engine.runAndWait()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# reverse the int value without using string
# x = 83475
# c = 0
#
# while x > 0:
#     digit = x % 10
#     c = c * 10 + digit
#     x = x // 10
#
# print(c)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# x = [4, 6, 8, 24, 12, 2]
#
# for i in range(len(x)):
#     for j in range(i + 1, len(x)):
#
#         if x[i] > x[j]:
#             x[i], x[j] = x[j], x[i]
# print(x[::-1])
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# lst_ = []
#
# for i in range(1, 11):
#     if (i == 1) or (i > lst_[-1]):
#         lst_.append(i)
# print(lst_[::-1])
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# string = input("enter your string: ")
# for i in string:
#     if i in "aeiou":
#         print("*", end="")
#     else:
#         print(i, end="")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# for i in range(1):
#     print(i, end="")
# else:
#     print("executed")

