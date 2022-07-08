# weight = float(input("Enter your weight: "))
# height = float(input("Enter your height in m: "))
# bmi = (weight/(height**2))
# if bmi < 18.5:
#     print("Your BMI is Underweight")
# elif bmi >= 18.5 and bmi < 25:
#     print("Your BMI is Normal")
# elif bmi >= 25 and bmi < 30:
#     print("Your BMI is Overweight")
# elif bmi >= 30:
#     print("Your BMI is Obesity")
# else:
#     print("Invalid input")
#===================================================================================================

# if __name__ == '__main__':
#     n = int(input().strip())
# if n%2==1:
#     print("Weird")
# elif n%2==0 and n in range(2,5):
#     print("Not Weird")
# elif n%2==0 and n in range(6,21):
#     print("Weird")
# elif n%2==0 and n>20:
#     print("Not Weird")
#===================================================================================================

# if __name__ == '__main__':
#     n = int(input("Enter the range: "))
#     for i in range(n):
#         if i<n:
#             print(i**2)
#===================================================================================================

# x = [2, 4, 5, 7, 4]
# y = x.index(4)
# print(y)
#================================================================================================== =
# from ast import Num


# name = "aniket"
# if name == "swagat":
#     print("Swagat")
# else:
#     if name == "chetan":
#         print("chetan")
#     else:
#         if name == "avi":
#             print("Avi")
#         else:
#             if name == "aniket":
#                 print("Aniket")
#             else:
#                 print("name is not found")
#=====================================================================

# n = int(input("enter the no of students: "))
# d = {}
# for i in range(n):
#     name = input("enter the name of student: ")
#     marks = int(input("enter the marks of student: "))
#     d[name] = marks
# while True:
#     name = input("Enter Student Name to get Marks: ")
#     marks = d.get(name,-1)
#     if marks == 1:
#         print("Student Not Found")
#     else:
#         print("The Marks of", name, "are", marks)
#     option = input("Do you want to find another student marks[Yes|No]")
#     if option == "No":
#         break
#============================================================================

# import math

# r = int(input("Enter the radius of circle: "))
# area_of_circle = 3.14*(r**2)
# volume_of_circle = (4/3)*3.14*(r**3)

# print("Area of circle:", area_of_circle)
# print("Volume of sphere:", volume_of_circle)
#============================================================================

#   Vovels count.

# i = input()
# count = 0
# for j in (i):
#     if j == "a" or j == "e" or j == "i" or j == "o" or j == "u":
#         count+= 1

# print(count  )
#============================================================================

# x = ("This is some text")

# print(x.count("s"))
# print(x.upper())
# print(x.title())
# print(x.lower())
# print(x.replace("some text", "awesome"))
# print(len(x))
#===========================================================================

# def test(func, arg):
#   return func(func(arg))

# def mult(x):
#   return x * x

# print(test(mult, 2))
#==========================================================================

#Pure functions

# def mult_function(x, y):
#     temp = x + 2*y
#     return temp / 2*x + y
#==========================================================================

# impure functions

# some = []

# def impure_sentence(x, y):
#     return x, y
#==========================================================================

# function as given by users data.

#==========================================================================

#  Font Change programme

# def style(str):
#     import string
#     __import__("os").system("Python roadmap.png")
#     A = [i for i in string.ascii_uppercase]


#     a = [i for i in string.ascii_lowercase]


#     b = [chr(i) for i in range(120198, 120198+26)]


#     B = [chr(i) for i in range(120172, 120172+26)]


#     Aa, Bb = A+a, B+b
#     Aa.append(' ')
#     Bb.append(' ')
    
#     txt = ''
#     for i in str:
#         txt += Bb[Aa.index(i)]
#     print ('<style>img{display:none}</style><center>')
#     return (f'<span style="font-size:20px">{chr(43457)}{chr(3898)} {txt} {chr(3899)}{chr(43458)}</span>')

# print(style(input()))
#================================================================================================

# str = "khushboo"
# def abc(x):
#     if x in ("khu"):
#         return True
#     else:
#         return False
# result = list(filter(abc,str))
# print(result)
#================================================================================================

#Letter Frequency

# text=input()
# letter=input()
# x=text.count(letter)
# print(int((x/len(text))*100))
#===================================================================================================

# a = [2, 4, 6]

# a.append(8)
# a.remove(4)
# a.insert(0, 8)

# print(a)
# print(a.count(8))
#==================================================================================================

# lst = [2, 4, 6, 8]
# lst.reverse()
# print(lst)

# lst.sort()
# print(lst)

# print(min(lst))
# print(max(lst))
#==================================================================================================

# #list comprehension
# cubes = [i**3 for i in range (1, 7)]

# print(cubes)
#==================================================================================================

# nums = [i*2 for i in range(10) if i**2 % 2 == 0]
# print(nums)
#==================================================================================================

# nums = [10, 9, 8, 7, 6, 5]
# nums[0] = nums[1] - 5
# if 4 in nums:
#   print(nums[3])
# else:
#   print(nums[4])
#==================================================================================================

#** Defination of Success **

# def success(dedication, persistence, passion):
#     dedication += 1
#     persistence += 1
#     passion = True

#     if passion == True:
#         magic = dedication + persistence
#         return magic
#     else:
#         magic = 0
#         return magic
#==================================================================================================

# txt = input("Enter your text here: ")
# length = len(txt)-txt.count(" ")
# splits = txt.split()
# words = 0
# for splits[words] in splits:
#     words += 1
# print(length/words)
#===================================================================================================

#Dictionary ex.

# fib = {1: 1, 2: 1, 3: 2, 4: 3}
# print(fib.get(4, 0) + fib.get(7, 5))
#===================================================================================================
# num = (1, 2, 3)
# a, b, c = num
# print(a)
# print(b)
# print(c)
#===================================================================================================
# sentence = input()
# words = sentence.split()
# total = sum(map(len, words))/len(words)
# print(total)
#===================================================================================================

# Ticket office.

# data = {
#     "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64,
#     "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35,
#     "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23,
#     "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16,
#     "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
# }
# age = int(input())
# new = 0
# old = 530
# for var in data.values():
#     if var < age:
#         new += 5
#     else:
#         new += 20
# if age < 18:
#     print(int((new - old) / old * 100))
# else:
#     print(0)
#==================================================================================================================

# def function():
#     def fun2():
#          return(a*b)
#     return(fun2)
# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# c=function()
# print(c)
#===================================================================================================================

# def polynominal(x):
#     return x**2 + 5*x / 4
# print(polynominal(-4))

# #lambda
# print((lambda x: x**2 / 5*x / 4)(-4))
#===================================================================================================================

# n = int(input("Enter The number: "))
# if n % 2==1:
#     print("Weird")
# elif n % 2 == 0 and n in range(2, 5):
#     print("Not Weird")
# elif n % 2 == 0 and n in range(6, 20):
#     print("Not Weird")
# elif n% 2 == 0 and n>20 :
#     print("Not Weird")
#=====================================================================================================================

# Factorial.
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact*i
#     return fact
# num = int(input("Enter a Value: "))
# result=factorial(num)
# print(result)
#==========================================================================================================

# def greet_user():
#     """Display the simple greeting"""
#     print("Hello!")

# greet_user()
#==========================================================================================================

# def display_message():
#     print("I am learing about in this chapter")

# display_message()
#==========================================================================================================

# try:
#     num1 = 7
#     num2 = 0
#     print(num1 / num2)
#     print("Dine calculation")
# except ZeroDivisionError:
#     print("An error occured")
#     print("due to zero division")

#===========================================================================================================

# try:
#     variable = 10
#     print(variable + "hello")
#     print(variable / 2)
# except ZeroDivisionError:
#     print("An error occured")
# except (ValueError, TypeError):
#     print("error occured")

#==============================================================================================================

# z = "India is great"
# print("India" in z)

# z = "India is great"
# print("India is great" is z)

#==============================================================================================================

# try:
#     meaning = 42
#     print(meaning/0)
#     print("the meaning of life")
# except(ValueError, TypeError):
#     print("ValueError or TypeError occured")
# except ZeroDivisionError:
#     print("Devided by zero")\

#==============================================================================================================

# try:
#     word = "spam"
#     print(word / 0)
# except:
#     print("An error occured")
#==============================================================================================================

# PIN generator.

# pin = input("Enter your PIN: ")
# try:
# 	int(pin)
# 	print("PIN code is created")

# except ValueError:
# 	print("Please enter a number")

#=============================================================================================================

# try:
#     print("Hello")
#     print(1 / 0)
# except ZeroDivisionError:
#     print("Devided by zero")
# finally:
#     print("This code will run no matter what")
#===========================================================================================

#finally.

# try:
#     print(1)
# except:
#     print(2)
# finally:
#     print(3)
#============================================================================================================

# try:
#     print(1)
#     print(10 / 0)
# except ZeroDivisionError:
#     print("unknown_var")
# finally:
#     print("This is executed last")

#============================================================================================================

# # A coffee vending machine makes 5 types of coffee:

# coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

# choice = int(input("Enter the index number of coffee: "))

# try:
#     amogh = open("wake.txt", "r")
#     print(amogh.read())
# # except:
# # 	print("Invalid number")
# finally:
# 	print("Have a good day")

#===========================================================================================================

# raise statement.

# try:
#   raise ZeroDivisionError(10 / 2)

# except ZeroDivisionError:
#     raise
#     print("Raise work here")
# finally:
#     print("we are done")

# #===========================================================================================================

# name = "123"
# raise NameError("Invalid name!")

#===========================================================================================================

# num = input(":")

# if float(num) < 0:
  
#     raise ValueError("Negative!")

#===========================================================================================================

# temp = -10
# assert (temp >= 0), "Colder than absolute zero!"
#===========================================================================================================

# @ Opening files

# # write mode
# open("filname.txt", "w")

# # read mode
# open("listpractice1.txt", "r")
# open("listpractice1.txt")

# # binary write mode
# open("filename.txt", "wb")

#===========================================================================================================

# file = open("listpractice1.txt", "w")
# # do stuff to the file
# file.close()

#===========================================================================================================

## reading files

#the contents of a file that has been opened in text mode can be read using the read method.

# file = open("abcd.txt", "r")
# cont = file.read()
# print(cont)
# file.clolse()

#===========================================================================================================

# # Let's learn about list comprehensions! You are given three integers x, y, and z representing the dimensions
# # of a cuboid along with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid 
# # where the sum of i+j+k is not equal to n. Here, 0<i<x; 0<j<y; 0<k<z. Please use list comprehensions rather 
# # than multiple loops, as a learning exercise.

# #Program

# x = int(input("Enter the 1st number: "))
# y = int(input("Enter the 2nd number: "))
# z = int(input("Enter the 3rd number: "))
# n = int(input("Enter the 4th number: "))
# ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
# print(ans)

#==========================================================================================================

# # Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# # You are given n scores. Store them in a list and find the score of the runner-up.

# n = int(input())
# arr = map(int, input().split())
# arr = list(arr)
# x = max(arr)
# y = -9999999
# for i in range(0,n):
#     if arr[i]<x and arr[i] > y:
#         y = arr[i]

# print(y)

#==========================================================================================================

# # Finding the percentage.

# n = int(input("Enter the number: "))
# student_marks = {}
# for _ in range(n):
#     line = input().split()
#     name, scores = line[0], line[1:]
#     scores = map(float, scores)
#     student_marks[name] = scores
# query_name = input("Enter a name of student: ")
# marks=0
# for i in student_marks[query_name]:
#     marks=marks+i
# avg=marks/3
# print("%.2f"%avg)

#===========================================================================================================

# def add_five(x):
#     return x + 5

# nums = [11, 22, 33, 44, 55]
# result = list(map(add_five, nums))
# print(result)
#===========================================================================================================
# map and lambda.

# nums = [11, 22, 33, 44, 55]

# result = list(map(lambda x: x+5, nums))
# print(result)
#===========================================================================================================
#list filter and lambda.

# nums = [11, 22, 33, 44, 55]

# result = list(filter(lambda x: x%2==0, nums))
# print(result)
#===========================================================================================================

# Generators.

# def countdown():
#     i=5
#     while i > 0:
#         yield i
#         i -= 1

# for i in countdown():
#     print(i)

# def num():
#     i = 10
#     while i > 0 and i < 25:
#         yield i
#         i += 1

# for i in num():
#     print(i) 
#================================================================================================

# def infinite_sevens():
#     while True:
#         yield 7

# for i in infinite_sevens():
#     print(i)
#================================================================================================

# Generator converted into list function.

# def numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i

# print(list(numbers(12)))
#================================================================================================

# def make_word():
#     word = ""
#     for ch in "spam":
#         word += ch
#         yield word

# print(list(make_word()))
#================================================================================================

# def abc(func):
#     def wrap():
#         print("========")
#         func()
#         print("==================")
#     return wrap

# def print_text():
#     print("Hello World!")

# decorated = abc(print_text)
# decorated()
#===============================================================================================

# def print_text(abc):
#     print("Hello World!")
#     abc()
#     return abc

# @print_text
# def print_text():
#     print("Go to Hell.")
#===============================================================================================

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x-1)
# print(factorial(5))
#===============================================================================================

def check_leap_year(year_):
    if year_%400==0 or (year_%100!=0 and year_%4==0):
          return 1
    else:
        return 0

def month_day(num):
    if (int(num)+1)<10:
        num=str(int(num)+1) 
        return '0'+num
    if (int(num)+1)>10:
        return str(int(num)+1)

def nxt_day(date_):
    try:
        d_list=date_.split('-')
        y,m,dt=d_list[0],d_list[1],d_list[2]
        day={1:31,2:[28,29],3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        year=check_leap_year(int(d_list[0]))
        month=int(m)
        if month!=2:
            if day[month]>int(dt):
                d=month_day(dt)
                print("Next Date : ",y+'-'+m+'-'+d)
            elif int(d_list[2])==day[month] and month!=12:
                mo=month_day(m)
                print("Next Date : ",y+'-'+mo+'-'+'01')
            elif int(dt)==day[month] and month==12:
                print("Next Date : ",str(int(y)+1)+'-'+'01'+'-'+'01')
                
        if (month==2 and year==0 and int(dt)<28) or (month==2 and year==1 and int(dt)<29):
            d=month_day(dt)
            print("Next Date : ",y+'-'+m+'-'+d)
        if (month==2 and year==0 and int(dt)==28) or (month==2 and year==1 and int(dt)==29):
            print("Next Date : ",y+'-'+'03'+'-'+'01')
    except:
        print('Invalid Input')
while True:
    n_d=input('Enter Date:  ')
    if n_d!='0':
        nxt_day(n_d)
    else:
        break