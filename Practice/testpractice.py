# lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# x=int(input("enter the number which you want to serach:"))

# count=0
# for i in lst:
#     if (i==x):
#         count=count+1
#         print("number of occurences of x is ",count)
#     # if (i not in lst): 
#     else:
#         print("type num which is in list")

# # _______________________________________________________________________________
# # Sort the values of first list using second list. 

# l = ["f", "l", "y", "r", "s", "j", "b", "c", "a"]
# m = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
# # def sort_list(l1, l2):
#     list_zip = zip(l2, l1)
#     output1 = [x for _, x in sorted(list_zip)]
#     return output1

# print("The values of first list using second list")
# print(sort_list(l1, l2))


# l = ['a', 'c', 'e', 'e', 'm', 'q', 'y']
# m = [1, 8, 6, 2, 9, 2, 6]

# lst = zip(l, m)
# final = list(lst)
# print(final)

# sorted_list = sorted(final, key=lambda x: (x[0], x[1]))
# print(sorted_list)
# # # _____________________________________________________________________________

# # a = "'Python' is programming language for Normal peoples, and 'Pyhon' is a language for Legends."
# # print(a)
# # _____________________________________________________________________________________________________________

# l1 = ["f", "l", "y", "r", "s", "j", "b", "c", "a"]
# l2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
# key1=dict(zip(l1,l2))
# print(key1)
# l1.sort(key=key1.get)
# print(l1)
# ______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# # We are creating our own social network application and need to have a hashtag generator program.
# Complete the program to output the input text starting with the hashtag (#).
# Also, if the user entered several words, the program should delete the spaces between them.

# s = input("Enter the name for hashtag: ")

# def hash(text):
# 	s1 = s.replace(" ", "")
# 	return "#" + s1

# print(hash(s))
# ______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# You are given a program with two inputs: one as password and the second one as password repeat. Complete and call the given function to output "Correct" if password and repeat are equal, and output "Wrong", if they are not.

# password = input("Enter the password: ")
# repeat = input("repeat the password: ")

# def validate(text1, text2):
# 	if text1 == text2:
# 		print("Correct")
# 	else:
# 		print("Wrong")

# validate(password, repeat)
# ________________________________________________________________________________________________________________________________________________

# num = int(input("enter the number:"))

# factorial = 1

# for i in range (1,(num+1)):
#     factorial = factorial * i

# print(f"Factorial of {num} = {factorial}")

# _________________________________________________________________________________________________________________________________

#
# s = "aniruddha"
# x = "-".join(s)
# print(x)

# s = "ankur"
# if i in s:
#     print(i, end="-")

# a = "nitin"
# b = ''
# # op > n-i-t-i-n
# for i in a:
#     b = b + i + "-"
# print(b.strip("-"))

# 9822503261

# # find the length of string
# str_="vijaynagar"
# z="ab"
# x=z.join(str_) # here x print vabiabjabaaby
# x1=x.count(z)+1
# #count function return how many time z occured in str. 4 time occured then add 1 i.e 4+1=5
# print(x)
# print(x1)


#
# s = "Djka1sjsjs2anns4ksmsm3"
# a = ""
# for i in s:
#     if i.isnumeric() + i.isalpha():
#         a += i
#         b = list(a)
#         b.sort()
# print(b)


# s = "Djka1sjsjs2anns4ksmsm3"
# a = "".join(sorted(s))
# print(a)

# import re
# str_ = "5an2ki3taims5"
# x = re.findall("[0-9]",str_)
# y = re.findall("[a-z]",str_)
# print("".join(x)+"".join(y))


# list1 = [11, 22, 33, 44]
# enumerate_list = enumerate (list1)
# print ("Enumerated list now looks like:", list (enumerate_list)) #print the index and corresponding value for enumerated list1 for i, item in enumerate (list1): print ("Index = ", i,": "," value = ", item)

#
# d = {}
# num_students = int(input("enter the no of student: "))
# for i in range(num_students):
#     name = input("Enter the name of student: ")
#     y = eval(input("enter the list of marks of student: "))
#     marks = sum(list(y))/len(y)
#     d[name] = marks
# print(d)
# # while True:
#     name = input("enter the name of student: ")
#     marks = d.get(name,-1)
#     if marks >= 80:
#         print(name,"has A Grade")
#     elif marks >= 60:
#         print(name,"has B Grade")
#     elif marks >= 40:
#         print(name,"has C Grade")
#     elif marks == -1:
#         print("student not found")
#     option = input("do u want to check another student marks:[yes/no] ")
#     if option == "no":
#         break
# print("thank u")

# for i in range(23, 24):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")
# a = 25
# l = [x*a for x in range(1, 11)]
# print(l)

# a = [f"{x} is even" if x%2 == 0 else f"{x} is odd" for x in range(10)]
# print(a)

# s = {7, 3, 9, 4, 8, 2}
# s.add(5)
# print(s)

# 1st method - Using list
# d = {"A": 1, "B": 2, "C": 3}
# k = list(d.keys())
# print(k)

# d = {"A": 1, "B": 2, "C": 3}
# k = list(d)
# print(k)

# 2nd method- Using iterable unpacking operator.
# d = {"A": 1, "B": 2, "C": 3}
# x = [*d.keys()]
# print(x)

# d = {"A": 1, "B": 2, "C": 3}
# x = [*d]
# print(x)

# 3rd method- Using keys() Function.
# d = {"A": 1, "B": 2, "C": 3}
# x = d.keys()
# print([k for k in x])

# 4th method
# d = {"A": 1, "B": 2, "C": 3}
# *x, = d
# print(x)

# s = "Learning Python Is Very Easy"
# a = []
# for i in s:
#     s.istitle()
# print(s)


# x = "b4a1d3"
# print(sorted(x))

# a = ""
# b = ""
# for i in x:
#     if i.isalpha():
#         a += i
#
# for j in x:
#     if j.isnumeric():
#         b += j
#
# print(sorted(b) + sorted(a))

# ______________________________________________________________________________________________________________________

# class BalanceException(Exception):
#     pass


# def checkbalance():
#     n = int(input("withdraw money: "))
#     money = 10000
#     withdraw = n
#     try:
#         balance = money - withdraw
#         if balance < 2000:
#             raise BalanceException("insufficient Balance")
#         print("Your remaining balance: ", balance)
#     except BalanceException as be:
#         print(be)
# checkbalance()
# _____________________________________________________________________________________________________-

# class TooOldException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
#
# class TooYoungException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
#
# age=int(input("Age-"))
# if age > 60:
#     raise TooOldException("can't give bride because too old")
# elif age<18:
#     raise TooYoungException("can't marriage under Age")
# else:
#     print("perfectly matched")

# a = "12,564.768,324.98786"
# b = a.maketrans
# a = a.translate(b(",.", ".,"))
# print(a)

# a = "12,564.768,324.98786"
# #
#
#
# def swap(str1):
#     str1 = str1.replace(",", "b")
#     str1 = str1.replace(".", ",")
#     str1 = str1.replace("b", ".")
#     return str1
#

# print(swap(a))

# nested list

# x = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# for i in x:
#     print(i, type(i))
#     for j in i:
#         print(j)
# ______________________________________________________________________________________________________________________

# x = [1, 2, 3, 4, 5, 6, 7]
# a, b, c, d, e, f, g = x
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# ______________________________________________________________________________________________________________________

# l1 = [1, 2, 3, 4, 5, 6, 7]
# print(l1)
# l1.append(9)

# s = {12, 23, 34, 45, 43, 231}
# s.add(89)
# print(s)

# l1 = [1, 2, 3, 4, 5, 6, 7]
# l1.remove(3)
# print(l1)

# l1 = [1, 2, 3, 4, 5, 6, 7]
# del l1[4]
# print(l1)

# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2 = [3, 45, 6, 7, 8, 9, 2, 4]
# l1.extend(l2)
# print(l1)

# str_ = "a10b3c9d9v12"
# op = ""
# for i in str_:
#     if i.isalpha():
#         i = i.replace(i, " ")
#     op = op+i
# ans = op.split()
# lst2 = []
# for i in ans:
#     lst2.append(int(i))
# lst = list(filter(lambda x: x.isalpha(), str_))
# res = list(map(lambda a, b : a*b, lst, lst2))
# print("".join(res))
# ______________________________________________________________________________________________________________________

# l1 = [[1, 2, 3], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17]]
# result1 = [[15, 2, 3], [12, 4, 5], [9, 7, 8], [6, 10, 11], [3, 13, 14], [1, 16, 17]]

#
# lst_ = [2, 4, 5, 7, 8, [45, 76, 44]]
# for i, j in zip(range(len(lst_)), lst_):
#     if type(j) == int:
#         print(i, " ", j)
#     if type(j) == list:
#         for k in range(len(j)):
#             print(i, k, j[k])
# ______________________________________________________________________________________________________________________

# l1 = [10, 20, 30, 40, 10, 20, 30, 50, 10]
# print(l1)
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)
# ______________________________________________________________________________________________________________________

# n1 = 20
# n2 = 30
# print(n1 * n2)

# n1 = 40
# n2 = 30
# print(n1 + n2)
# ______________________________________________________________________________________________________________________

# def mult_or_sum(n1, n2):
#     # calculate product of two number
#     prod_ = n1 * n2
#     if prod_ <= 1000:
#         return prod_
#     else:
#         return n1 + n2
#
#
# result = mult_or_sum(20, 30)
# print("The result is: ", result)
#
# result = mult_or_sum(40, 30)
# print("the result is: ", result)
# ______________________________________________________________________________________________________________________

# previous_number = 0
# for i in range(10):
#     print(f"Current Number {i} Previous number {previous_number} sum: {i + previous_number}")
#     previous_number = i
# ______________________________________________________________________________________________________________________

# str_ = input("enter the word: ")
# print("Main string: ", str_)
#
# size_ = len(str_)
#
#
# for i in range(0, size_ - 1, 2):
#     print("index[", i, "]", str_[i])
# ______________________________________________________________________________________________________________________

# str_ = input("enter word: ")
# x = list(str_)
# for i in x[::2]:
#     print(i)
# ______________________________________________________________________________________________________________________

# # remove first n character from a sting
# def remove_word(word, n):
#     print("Original String: ", word)
#     x = word[n:]
#     return x
#
#
# print("removing character from a string")
# print(remove_word("Shriyash", 4))
# print(remove_word("Shriyash", 2))


# str_ = "a7bb12c2d10"
# op=""
# for i in str_:
#     if i.isalpha():
#         i=i.replace(i," ")
#     op=op+i
# ans=op.split()
# lst2=[]
# for i in ans:
#     lst2.append(int(i))
# lst=list(filter(lambda x:x.isalpha(),str_))
# res=list(map(lambda a,b:a*b,lst,lst2))
# print("".join(res))


# import re
#
# str_ = "a7b12c2d10"
#
# l4 = []
# l1 = re.findall("\d+", str_)
# for i in l1:
#     l4.append(int(i))
# # print("l4 is: ", l4)
# l = []
# a = []
#
# for i in str_:
#     if i.isalpha():
#         l.append(i)
# print(l)
#
# for i, j in zip(l, l4):
#     a.append(i * j)
# # print("a: ", a)
#
# s = ''.join(a)
# print(s)
# ______________________________________________________________________________________________________________________
# lst_ = [1, 2, 3, 4, 5, 6]
# new_lst = []
# for i in range(len(lst_)-1, -1, -1):
#     new_lst.append(lst_[i])
# print(new_lst)
# ______________________________________________________________________________________________________________________

# # what is iterator

# lst_ = [4, 7, 0, 3]
#
# # get an iterator using iter()
# iter_ = iter(lst_)
#
# # iterate through it using next()
#
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))
# ______________________________________________________________________________________________________________________

# Create a string made of the first middle and lst character.

# str_ = "Aniruddha"
# print("main string: ", str_)
# result_ = str_[0]
#
# l1 = len(str_)
# middle_ = int(l1 / 2)
# result_ += str_[middle_]
# result_ += str_[l1 - 1]
# print("New string: ", result_)
# ______________________________________________________________________________________________________________________
# # create a string made of the middle three characters.


# def get_middle_three_char(str_):
#     middle_ = int(len(str_) / 2)
#     result_ = str_[middle_ - 1: middle_ + 2]
#     print("Middle three characters are: ", result_)


# get_middle_three_char("aniruddha")
# get_middle_three_char("JayShiRam")
# ______________________________________________________________________________________________________________________
# # Append new string in the middle of a given string

# def append_middle(s1, s2):
#     middle_ = int(len(s1) / 2)
#     x = s1[:middle_:]
#     x = x + s2
#     print(x)
#     x += s1[middle_:]
#     print("after appending new string in middle: ", x)
#
#
# append_middle("atul", "mohan")


# s1 = input("enter the first name: ")
# s2 = input("enter the second name: ")
#
# middle_ = int(len(s1) // 2)
# print("middle:", middle_)
# x = s1[:middle_:]
# print(x)
# x += s2
# print(x)
# x += s1[middle_:]
# print("after appending new string in middle: ", x)
# ______________________________________________________________________________________________________________________

# # create a new string of the first, middle and last character of each input string.


# lst_ = [34, 56, 39, 87, 54]
# for i, j in enumerate(lst_):
#     print("index is {} and the number is {}".format(i, j))
# ______________________________________________________________________________________________________________________
# # Merge two dictionaries in a single expression.

# first = {1: 'travis', 2: "Tom", 3: "nitin"}
# second = {2: 'saurabh', 4: "pankaj"}

# allCombine = {**first, **second}
# print(allCombine)

# def merge_dicts(dict1, dict2):
#     dict3 = dict1.copy()
#     dict3.update(dict2)
#     return dict3
#
# print(merge_dicts(first, second))
# ______________________________________________________________________________________________________________________

# List comprehension
# lst_ = [(i, chr(64 + i)) for i in range(1, 5)]
# print(lst_)

# Dict comprehension
# dict_ = dict([(i, chr(65 + i)) for i in range(5)])
# print(dict_)

# dict_ = {i: chr(65 + i) for i in range(5)}
# print(dict_)


# dict_ = {i: i ** 2 for i in range(1, 11)}
# print(dict_)
# ______________________________________________________________________________________________________________________

# # return multiple values from a function.

# def multValues(n1, n2):
#     return n1 * n2, n2/n1
#
#
# prod_, div_ = multValues(22, 43)
# print("product", prod_, "division {:.2f}".format(div_))
# ______________________________________________________________________________________________________________________

#  CREATE A FUNCTION WITH  VARIABLE LENGTH OF ARGUMENTS.

# def func_(*args):
#     for i in args:
#         print(i)
#
#
# func_(20, 30, 40)
# func_(260, 300)
# func_("Abra ka Dabra")
# ______________________________________________________________________________________________________________________

# # a = [[2, 3]]*3
# a = [[2, 3], [2, 3], [2, 3]]
# # print(a)
# a[3][0] = 3
# print(id(a[0]))
# print(id(a[1]))
# print(id(a[2]))
# # print(a)
# ______________________________________________________________________________________________________________________


