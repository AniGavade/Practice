# Assignment 1.1

# 1. Write a program to check whether a person is eligible for voting or not. (Accept age from user)

# age = int(input("Enter the age of person: "))
# if age >= 18:
#     print("the person is eligible for voting")
# else:
#     print("Not eligible for voting")
# ______________________________________________________________________________________________________________________

# 2. Write a program to check whether a number entered by user is even or odd
# n = int(input("enter the number: "))
# if n % 2 == 0:
#     print("The number {} is Even".format(n))
# else:
#     print("The number {} is Odd".format(n))
# ______________________________________________________________________________________________________________________

# 3. Write a program to check whether a number is divisible by 7 or not
# n = int(input("Enter the number: "))
# if n % 7 == 0:
#     print("The number {} is divisible by 7".format(n))
# else:
#     print("The number {} is not divisible by 7".format(n))
# ______________________________________________________________________________________________________________________

# 4. Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
# n = int(input("Enter the number: "))
# if n % 5 == 0:
#     print("Hello")
# else:
#     print("Bye")
# ______________________________________________________________________________________________________________________

# 5. Write a program to accept percentage from the user and display the grade according to the following criteria:
# marks             Grade
# > 90                A
# > 80 and <=90       B
# > 60 and <=80       C
# Below 60            D

# percentage = int(input("Enter percentage: "))
# if percentage > 90:
#     print("The grade is 'A'")
# elif percentage > 80 and percentage <= 90:
#     print("The grade is 'B'")
# elif percentage > 60 and percentage <= 80:
#     print("The grade is 'C'")
# elif percentage < 60:
#     print("The grade is 'D'")
# ______________________________________________________________________________________________________________________

# 6. write a program to accept a number from 1 to 7 and
# display the name of the day like 1 for Sunday, 2 for monday and so on.

# n = int(input("Enter the any number:"))
# if n >= 1 and n <= 7:
#     if n == 7:
#         print("Sunday")
#     elif n == 6:
#         print("Monday")
#     elif n == 5:
#         print("Tuesday")
#     elif n == 4:
#         print("Wednesday")
#     elif n == 3:
#         print("Thursday")
#     elif n == 2:
#         print("Friday")
#     elif n == 1:
#         print("Saturday")
# else:
#     print("Enter the number in the rage of 1 to 7")
# ______________________________________________________________________________________________________________________

# 7. Write a program to find the lowest number out of two numbers excepted from user.
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the secind number: "))
# if n1 < n2:
#     print(n1)
# else:
#     print(n2)
# ______________________________________________________________________________________________________________________

# 8. Write a program to check whether a number (accepted from user) is positive or negative
# n = int(input("Enter the number: "))
# if n >= 0:
#     print("{} is a Positive Number".format(n))
# else:
#     print(f"{n} is negative number")
# ______________________________________________________________________________________________________________________

# 9. Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
# n = int(input("Enter the number: "))
# if n % 2 == 0 and n % 3 == 0:
#     print(f"This number {n} is divisible by 2 and 3")
# else:
#     print(f"This number {n} is not divisible by 2 and 3")
# ______________________________________________________________________________________________________________________

# 10.Write a program to find the largest number out of three number excepted from user.
# a, b, c = input("Enter the values: ").split()
# if a > b:
#     if a > c:
#         print(f"Largest Value is {a}")
#     else:
#         print(f"Largest value is {c}")
# elif b > c:
#     print(f"Largest Numberis {b}")
# else:
#     print(f"Largest Value is {c}")
# ______________________________________________________________________________________________________________________

# 11. Accept the age of 4 people and display the oldest one.
# a, b, c, d = input("Enter the age of 4 peoples: ").split()
# age = int(a)
# if int(b) > age:
#     age = int(b)
# elif int(c) > age:
#     age = int(c)
# elif int(d) > age:
#     age = int(d)
# print(f"Oldest age is {age}")
# ______________________________________________________________________________________________________________________

# 12. Create Simple calculator Add, Sub, Mul, Dev takes two numbers from user.
# x = int(input("Enter first value: "))
# y = int(input("Enter second value: "))
# add = x + y
# sub = x - y
# mul = x * y
# div = x / y
# print(f"{x}+{y}={add}")
# print(f"{x}-{y}={sub}")
# print(f"{x}*{y}={mul}")
# print(f"{x}/{y}={div}")
# ______________________________________________________________________________________________________________________

# 13. Write a python program to count the number of even and odd numbers from a series of numbers.
# series1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# odd_count = 0
# even_count = 0
# for i in series1:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"The count of even numbers is {even_count}\nThe count of odd number is {odd_count}")
# ______________________________________________________________________________________________________________________

# 14. Write the program that prints all the numbers from 0 to 6 except 3 and 6.
# for i in range(0, 7):
#     if i == 3 or i == 6:
#         continue
#     else:
#         print(i)
# ______________________________________________________________________________________________________________________

# 15.Write the program to display the factorial of a number.
# n = int(input("Enter number for factorial: "))
# a = n
# fact = 1
# while n > 1:
#     fact *= n
#     n -= 1
# print(f"Factorial of {a} is {fact}")
# ______________________________________________________________________________________________________________________

# 16. Write the program to reverse the word.
# word = input("Enter the word: ")
# for i in range(len(word), 0, -1):
#     print(word[i-1], end="")
# ______________________________________________________________________________________________________________________

# 17.write program to reverse a number
# n = input("Enter the number: ")
# a = n[::-1]
# print(a)
# ______________________________________________________________________________________________________________________

# n = int(input("Enter the number: "))
# while n > 0:
#     rev = n % 10
#     n = n // 10
#     print(rev, end="")
# ______________________________________________________________________________________________________________________

# 18. write a program to print n natural number in descending order using a while loop.
# n = int(input("Enter the number for natural number collection: "))
# while n > 0:
#     print(n)
#     n -= 1
# ______________________________________________________________________________________________________________________

# 19. Print the square of all numbers from 0 to 100.
# l = [x*x for x in range(0, 100)]
# print(l)
# ______________________________________________________________________________________________________________________

# for i in range(0, 100):
#     sqr_rt = i*i
#     print(f"{i}^2 = {sqr_rt}")
# ______________________________________________________________________________________________________________________

# 20.Find the sum of all even numbers from 0 to 10.
# for i in range(11):
#     sum1 = 0
#     if i % 2 == 0:
#         sum += i
# print(f"Sum of all even numbers = {sum}")
# ______________________________________________________________________________________________________________________

# x = [10, 20, 30, [40, 50]]
# print("Index and Values: ")
# for i in range(3):
#     print(i, "   ", x[i])
# for j in range(3, 4):
#     print(j, " 0 ", x[3][0])
#     print(j, " 1 ", x[3][1])

# x = [10, 20, 30, [40, 50]]
# index = 0
# index1 = 0
# for i in x:
#     if i == x[3]:
#         for i in x[3]:
#             print(index, "", index1, " ", i)
#             index1 += 1
#     else:
#         print(index, "   ", i)
#         index += 1
# ______________________________________________________________________________________________________________________

# l = [10, 20, 30, [40, 50]]
#
# for i, j in zip(range(len(l)), l):
#     if type(j) == int:
#         print(i, ' ', j)
#     if type(j) == list:
#         for k in range(len(j)):
#             print(i, k, j[k])
# ______________________________________________________________________________________________________________________

# lst=[2,3,4,5,6,7,8,9,10]
# x=list(map(lambda x:x if x%2==0 else continue, lst))
# print(x)
# ______________________________________________________________________________________________________________________

from itertools import combinations

x = combinations(['a', "boss"], 1)
cnt = 0
for i in x:
    cnt += 1
    print(i)
    print(cnt)
# ______________________________________________________________________________________________________________________
