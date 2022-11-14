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

# letters = [i for i in "Aniruddha"]
# print(letters)

# list comprehension python vs python lambda functions.

# # Using map() with lambda function
# l_ = list(map(lambda x: x, "Aniruddha"))
# print(l_)

# l_ = [x for x in "Saurabh"]
# print(l_)

# Filter() with lambda function
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
# lst_ = filter(lambda x: x % 2, lst1)
# print(list(lst_))

# lst_ = [1, 2, 3, 4, 5, 6, 7, 8]
# lst1 = [x for x in lst_ if x % 2]
# print(list(lst1))

# # reduce() with lambda function
from functools import reduce
import functools

# lst_ = [1, 2, 3, 4, 5]
# n1 = reduce(lambda x, y: x*y, lst_)
# print(n1)

# fact_ = reduce(lambda x, y: x*y, range(1, 6))
# print(fact_)

# x = 5
# fact_ = reduce(lambda x, y: x*y, [1, 1] if x == 0 else range(1, x + 1))
# print(fact_)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return functools.reduce(lambda x,y: x*y, range(1,n+1))
#
#
# print(factorial(5))

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


# """They can be constructed from other iterables. if you dont know what iterabless are,
# If the iterable contains dupicate elements, they'll be  removed automatically in the constructed set objects."""

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

# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])
#
#
# string_test('Hello World')

# str_ = "Hello World"
# for i in str_:
#     if i.isupper():
#         v = str_.count(i)
#         print(i, "=", str_.count(i))
#     else:
#         n = str_.count(i)
#         print(i, "=", set(n))

# from collections import Counter
#
# count_letter = "Hello World"
# for i in count_letter:
#     if i.isupper():
#         print(dict(Counter(i)))
#     else:
#         print(dict(Counter(i)))
# print(dict(Counter(count_letter)))


# import collections
# print(collections.Counter("Hello World"))
#
#
# text_ = "Hello World"
# str_upp = [(x, ":", text_.count(x)) for x in text_ if x.isupper()]
# print("list_cap = ", str_upp)
# str_low = [(x, ":", text_.count(x)) for x in text_ if x.islower()]
# print("list_low = ", str_low)

# l_ = "Hello World"
# e = {}
# o = {}
# for i in l_:
#     if i.isupper():
#         e[i] = e.get(i, 0)+1
# for k, v in e.items():
#     print(k, ":", v)
# for x in l_:
#     if x.islower():
#         o[x] = o.get(x, 0)+1
# for q,f in o.items():
#     print(q, ":", f)

# str_ = "aniruddha gavade"
# d1 = {}
# d2 = {}
# for i in str_:
#     if i.isupper():
#         d1[i] = d1.get(i, 0) + 1
# for k, v in d1.items():
#     print(k, ":", v)
# for j in str_:
#     if j.islower():
#         d2[j] = d2.get(j, 0) + 1
# for q, f in d2.items():
#     print(q, ":", f)

# __________________________________________________________________________________________________________________

# wrd_ = input("Enter the word: ")
# d = {}
# for x in wrd_:
#     d[x] = d.get(x, 0) + 1
# for k, v in d.items():
#     print(k, v)
#
#
# a = "wonder"
# print(f"{a:_^20}")

# __________________________________________________________________________________________________________________
# def func():
#     global value
#     value = "Local"
#
#
# value = "Global"
# func()
# print(value)
# __________________________________________________________________________________________________________________

# a = 3
# b = 1
# print(a, b)
# a, b = b, a
# print(a, b)
# __________________________________________________________________________________________________________________

# data = [
#     {"dsi": 'abc', 'asv': 'uk1'},
#     {"dsi": 'abc', 'asv': 'uk1'},
#     {'dsi': 'test', 'asv': 'us1'},
#     {'dsi': 'test', 'asv': 'us2'}
# ]

# # >>> o/p
# [{"dsi":'abc','asv':'uk1'},
#     {'dsi':'test','asv':['us1','us2']}]

#
# data1 = [
#     {'dsi': 'test', 'asv': 'us1'},
#     {"dsi": 'abc', 'asv': 'uk1'},
#     {"dsi": 'abc', 'asv': 'uk1'},
#     {'dsi': 'test', 'asv': 'us2'},
#     {"dsi": 'max', 'asv': 'up1'},
#     {'dsi': 'max', 'asv': 'up2'}
# ]
# same = []
# dupli = []
# lst = [i for i in data1[0].keys()]
# for i in range(len(data1)):
#     for j in range(i):
#         if data1[i] == data1[j]:
#             same.append(data1[i])
#         elif data1[i][lst[0]] == data1[j][lst[0]] and data1[i][lst[1]] != data1[j][lst[1]]:
#             dupli.append([data1[i], data1[j]])
# for k in dupli:
#     d1 = k[0]
#     d2 = k[1]
#     d = {}
#     for i, j in zip(d1.keys(), d2.keys()):
#         if d1[i] == d2[j]:
#             d.setdefault(i, d1[i])
#         else:
#             d.setdefault(i, [d1[i], d2[j]])
#     same.append(d)
# print(same)

# Q. Reverse the string without changing the index of symbol/special character.

# def rev(word_):
#     index = 5
#     for i in range(len(word_)-1, int(len(word_)/2)-1, -1):
#         if word_[i].isalnum():
#             rev_in = word_[i]
#             while True:
#                 index += 1
#                 if word_[index].isalnum():
#                     word_[i] = word_[index]
#                     word_[index] = rev_in
#                     break
#     return word_
#
#
# str_ = "Brain$work&"
# rev_str = rev(list(str_))
# print("".join(rev_str))


# s = 'Brain$work&'
#
# list_ = list(s)
#
# i = 0
# j = len(list_) - 1
#
# while i < j:
#     if not list_[i].isalnum():
#         i += 1
#     elif not list_[j].isalnum():
#         j -= 1
#     else:
#         list_[i], list_[j] = list_[j], list_[i]
#         i += 1
#         j -= 1
# output_ = ''.join(list_)
# print(output_)


# seq = 'Brain$work&'
# seq = "123$456%789*0^/"
#
# l1 = [x for x in seq if x.isalnum()][::-1]
# l2 = [seq.index(y) for y in seq if y.isalnum() == False]
#
# for z in l2:
#     l1.insert(z, seq[z])
#
# print(''.join(l1))

# ______________________________________________________________________________________________________________________

# import re
#
# input = "brain$work&"
# # input = "&Bainw$orks"
# lst1 = [i for i in input if i.isalpha()][::-1]
# lst3 = re.findall("[\W]", input)
# lst2 = [input.index(i) for i in input if i in lst3]
# for i in range(len(lst2)):
#     lst1.insert(lst2[i], lst3[i])
# print("".join(lst1))
# ______________________________________________________________________________________________________________________

# Guessing the output

# for i in range(10):
#     if i == 6:
#         break
#     else:
#         print(i)
# else:
#     print("hello world")
# ______________________________________________________________________________________________________________________
# str_ = "AaBbCcDdEeFf"
# var = "c"
# while var in str_:
#     str_ = str_[:-1]
#     print(var, " ")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# p=[1,2]
# q=0
# r=[]
# if p or q and r:
#     print("True")
# else:
#     print("False")

# print(True and False)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# lst=[1,2]
# for i in lst:
#     lst.append(i)
# print(lst)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# lst=["there","are","a",["one","two"],"that","we","will"]
# print(lst[3:4])
# print(lst[3:4][0])
# print(lst[3:4][0][1][2])
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def func(n,lst=[]):
#     lst.append(lst.append(lst.append(n)))
#     return lst
# for i in range(4):
#     lst2=func(i)
# print(lst2)

# for i in [1,2,3,4][::-1]:
#     print(i)

# for i in sorted([5,3,8,5]):
#     print(i)

# for i in [10,4,2,7].sort():
#     print(i)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# cnt = 0
# for i in range(5):
#     while i < 3:
#         if i == 1:
#             break
#         cnt += 10
#         i += 1
#     else:
#         cnt += 1
# else:
#     cnt += 20
# print(cnt)
# ______________________________________________________________________________________________________________________

# str_="hello world"
# while str_:
#     print("hello")
#     str_=str_[1::2]
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# d = input("Enter your string: ")
#
# e = []
#
# for i in d:
#     if i.isalpha():
#         e.append(i)
#     else:
#         if (ab.index(e[-1]) + int(i)) >= 26:
#             e.append(ab[(ab.index(e[-1]) + int(i)) - 26])
#         else:
#             e.append(ab[(ab.index(e[-1]) + int(i))])
#
# e = ''.join(e)
#
# print(e)
# ______________________________________________________________________________________________________________________
# input_ = "Sachin Ramesh Tendulkar "
#
# # Op= "S. R. Tendulkar"
# for i in input_:
#     if i.isupper():
#         print(i + ".", end=" ")
# ______________________________________________________________________________________________________________________

# string1 = 'AD44EG2H2J'
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

# ______________________________________________________________________________________________________________________
# str = "Sachin Ramesh Tendulkar"
#
# lst = str.split()
#
# l = len(lst)
# lst1 = []
# for i in range(l):
#     if i < l-1:
#         lst1.append((lst[i])[0])
#     else:
#         lst1.append(lst[i])
# print(". ".join(lst1))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ip = input("Enter the name: ")
# op = ip.split(" ")
# res = ''
# for i in range(len(op)):
#     if i <= len(op) - 2:
#         res = res + op[i][0] + '. '
#     else:
#         res = res + op[i]
#
# print(res)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# input_string = input("Enter the name: ")
#
# lst = input_string.split()
#
# output = [lst[x][0] + '.' if (x < len(lst) - 1) else lst[x] for x in range(len(lst))]
# result_ = ' '.join(output)
# print(result_)

# ______________________________________________________________________________________________________________________

# input_ = input("enter the Name: ")
# l_ = input_.split()
# print(l_)
# op_ = [l_[x][0] + "." if (x < len(l_)-1) else l_[x] for x in range(len(l_))]
# res = " ".join(op_)
# print(res)
# ______________________________________________________________________________________________________________________

# data = {"dsi":'abc','asv':'uk1'}
# verb = {"dsi":'abc','asv':'uk1'}
# # term_ = {'dsi':'test','asv':'us1'}
#
# t = {**data, **verb}
# print(t)
# ______________________________________________________________________________________________________________________
#
# def remove_nth(a):
#     i = a.rfind('r')
#     res_ = a[:i]
#     res_1 = a[i + 1:]
#     return res_ + res_1
#
#
# a = "AniruddhaAnir"
# print(remove_nth(a))
# ________________________________________
# l = ["rohit", "vikram", "rohit"]
# word = "rohit"
# n = 2
# count = 0
# for i in range(len(l)):
#     # print(i)
#     if l[i] == word:
#         count += 1
#     if count == n:
#         # print(i)
#         l.pop(i)
#         break
#
# print("New List: ", l)


# n=int(input('enter number for factorial'))
# fact=1
# while(n>0):
#     fact=n*fact
#     n=n-1
# print('factorial is ',fact)

# n=int(input("Enter number:"))
# fact=1
# while(n>0):
#     fact=fact*n
#     n=n-1
# print("Factorial of the number is: ")
# print(fact)
# _____________________________________________________________________________
