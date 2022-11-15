# # Q. 1 Code for numbers divisible by 5 between 1 and 100 suing list comprehension
#
# lst_ = [x for x in range(1, 101) if x % 5 == 0]
# print(lst_)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # list comprehension
# ip = [2, 4, 5, 6, 8]
# op = [x**2 for x in ip]
# print(op)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import json

# # Q. Write  a program for convert dictionary to json dict = {'a':1, 'b':2, 'c':3, 'd':4}
# dict_ = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4
# }
# v = json.dumps(dict_, indent=4)
# print(v)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # Q. Write  a program for convert Json dict to dictionary dict = {'a':1, 'b':2, 'c':3, 'd':4}
# op = json.load(open('C:\\practice\\written mock\\dict_.json', 'r'))
# print(op)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # Q. Convert Json data into python dictionary.
# with open('data.json') as json_file:
#     data = json.load(json_file)
#     print(data)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # Q. Convert Json string into python dictionary.
#
# v = '{"make": "Audi", "Model": "A8l", "Version": 4.0}'
# op = json.loads(v)
# print(op)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Pattern
'''
****$
***$$
**$$$
*$$$$
$$$$$
'''
# for i in range(1, 6):
#     print("*"*(5-i) + "$"*(i))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ip = [(1, 23), (72, 3), (8, 10), (18, 3), (7, 8)]
# # op = '0, 1, 2, 3, 7, 8'
# lst = []
# for i in ip:
#     for j in i:
#         for k in str(j):
#             if k.isnumeric():
#                 lst.append(k)
# print(",".join(sorted(set(lst))))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# res = set()
# {res.update(str(i[0]) + str(i[1])) for i in ip}
# res = sorted(res)
# print(",".join(res))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Using Pythom 're' module  find 10 digit mobile number from below string.
'''strn = Hello my name is XYZ My contact number is 1234567890 I am from Pune.'''


import re


# Function to extract all the numbers from the given string
# def getNumbers(str):
#     lst_ = re.findall(r'[0-9]{10}', str)
#     return lst_


# str = "Hello my name is XYZ My contact number is 1234567890 I am from Pune"
# lst_1 = getNumbers(str)
# print(*lst_1)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++

# lst = re.findall(r'[0-9]{10}', str)
# print(*lst)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Q. Write The program for factorial of the number.

from functools import reduce

# fact_ = reduce(lambda x, y: x*y, range(1, 6))
# print(fact_)
# _____________________________________________________________________

# x = 5
# fact_ = reduce(lambda x, y: x*y, [1, 1] if x == 0 else range(1, x+1))
# print(fact_)
# _____________________________________________________________________


# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return num * fact(num-1)
#
#
# v = fact(5)
# print(v)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# str_ = 'aabbbccddddaaaaa'
# v = {x: str_.count(x) for x in str_}
# print(v)

# str_ = 'aabbbccddddaaaaa'
# v = [str_.count(x) for x in set(str_)]
# print(v)

# str_ = 'aabbbccddddaaaaa'
# dict_ = {}
# for i in str_:
#     if i in dict_:
#         dict_ += 1
#     else:
#         dict_ += 1
# print(dict_)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# str_ = "a4b7n8c33"

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ip = [(1, 2), (3, 4), (5, 6), (27, 1), (7, 8)]
# v = re.sub(r'[ [\] (\), ]','',str(ip))
# b = [int(x) for x in set(v)]
# print(sorted(b))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

lst = [3, 1, 2, 10, 1]
op = reduce(lambda x, y: x + [x[-1] + y], lst, [0])[1:]
print(op)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# A = [3, 1, 2, 10, 1]
# b = 0
# for i in A:
#     b = b+i
#     print(b, end=" ")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# arr=[3,1,2,10,1]
# s=0
# output=[]
# for i in arr:
#     s=s+i
#     output.append(s)
# print(output)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
