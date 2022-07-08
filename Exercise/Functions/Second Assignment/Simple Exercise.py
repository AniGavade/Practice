# 1. Python program to add two numbers.

# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# print(a+b)
# _________________________________________________________________________________________________________________________

# 2. Maximum of two numbers in Python

# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))

# if a > b:
#     print(a)
# else:
#     print(b)
# _________________________________________________________________________________________________________________________

# 3. Python Program for factorial of a number

## in Simple form
# n = int(input("enter a number: "))
# fac = 1
# for i in range(1, n + 1):
#     fac = fac * i
 
# print("factorial of ", n, " is ", fac)

## By using function form.

# n = int(input('Enter the number: '))
# def fac(n):
#     if n == 0:
#         result = 1
#     else:
#         result = n*fac(n-1)
#     return result
# print("the Factorial of given number is: ", fac(n))
# ______________________________________________________________________________________________________________

# 4. Python Program for simple interest

# p = int(input("Enter the principle Amount: "))
# t = int(input("Enter the tim,e period in years: "))
# r = int(input("Enter the rate on interest: "))
# Simple_Interest = (p * t * r) / 100
# print("The Simple interest on your amount is ", Simple_Interest)

# ______________________________________________________________________________________________________________

# 5. Python Program for compound interest
# The formula for compound interest is A = P(1 + r/n)^nt, where P is the principal balance,
# r is the interest rate, n is the number of times interest is compounded per time period and
# t is the number of time periods

# p = int(input("Enter the principle of balance: "))
# r = int(input("Enter the interest rate: "))
# n = int(input("Enter the number of times interest: "))
# t = int(input("Enter the time period: "))

# a = p * (1 + r / n) ** (n * t)
# fo_a = "{:.2f}".format(a)
# print(fo_a)
# ____________________________________________________________________________________________________________________________

# l = [["a",["b",["c","x"]]],42]
# print(l[0][1][1][0])
# _______________________________________________________________________________________________________________________________________

# names = ["Ankur", "Shri", "Prathamesh", "Pushpraj", "SaurabhVaidya", "Rohit", "Item"]
# result = list(filter(lambda x: len(x)>5, names))
# print(result)
# _______________________________________________________________________________________________________________________________________

# # String Function.

# # 1.Capitalize()
# s = "hello team brainworks"
# s = s.capitalize()
# print(s)

# # # 2. Title()
# s = "hello team brainworks"
# s = s.title()
# print(s)

# # 3. Upper case()
# s = "hello team brainworks"
# s = s.upper()
# print(s)

# # 4. Lower case()
# s = "HELLO TEAM BRAINWORKS"
# s = s.lower()
# print(s)

# # 5. Casefold()
# s = "English is $ Funny language"
# s = s.casefold()
# print(s)

# # 6. swapcase()
# s = "Python is programming language, Python is used for Machine learning"
# s = s.swapcase()
# print(s)

# 7. strip()
# s = "098Team 098Brainworks12"
# s = s.strip("01892")
# print(s)

# # 8. rstrip()
# s = "898989Team 89898Brainworks89898"
# s = s.rstrip("89")
# print(s)

# # 9. lstrip()
# s = "123Team 123Brainworks123"
# s = s.lstrip("123")
# print(s)

# # 10. replace()
# s = "Hello Python and 12 data science Python"
# s = s.replace("Python", "Java").replace("Hello", "Welcome to")
# print(s)

# 11. count()
# s = "hellopythondeveloper"
# for i in s:
#     r = s.count(i)
#     # print(f"the count {i} = {r}")
#     print("the count of {} is {}".format(i, r))

# s = "Thisisalengthyprocess"
# s = s.count("i")
# print(s)

# 12. index()
# s = "welcome to goa singham goa hi"
# s = s.index("goa", 1, -1)
# print(s)

# # 13. split()
# # To calculate total words in string.
# s = input("Enter the sentence from user: ")
# r = len(s.split())
# print("There are " + str(r) + " words.")

# s = "We are happy with our performance from last month"
# s = s.split()[-1]
# print(s)

# # 14. endswith()
# s = "Shakalaka boom boom."
# e = s.endswith("m")
# r = s.endswith(".")
# print(e)
# print(r)

# # 15. startswith
# s = "Everything is object in Python"
# a = s.startswith("Everything")
# b = s.startswith("everything")
# print(a)
# print(b)

# # 16. find()
# s = "Hello martian, today is great day."
# a = s.find("s")
# b = s.find("q")
# c = s.rfind("today")
# print(a)
# print(b)
# print(c)

# 17. center()
# s = "Fast and furius"
# s = s.center(22, "@")
# print(s)

# 18. join()
# s = ("Mogli", "Taarzan", "Ankur", "Raju")
# b = " is ".join(s)
# print(b)

# s = "PushprajPatil"
# b = " ".join(s)
# print(b)

# my_dict = {"name": "Aniruddha", "country":"India"}
# separator_1 = "TEST"
# x = separator_1.join(my_dict)
# print(x)

# 19. zfill
# s = "`Amar"
# a = s.zfill(5)
# print(a)

# a = input("Enter the string: ")
# b = ""
# for i in a:
#     if i.istitle():
#         b = b + " " + i
#     else:
#         b = b + i
# print(b)

# a = "here is advise for those who are not able to make program keep practicing and be a patient about your goals. be greatfull what you have. its always been nice to worry abou future."
# x = a.rpartition("program")
# print(x)

