# Anonymous function are the function without function defination.
# We use lambda keyword in anonymous function.
# Syntax ==> lambda (arguments) : expression
# A lambda funtion can take any number of arguments, but can only have one expression


# # make sure of argument a, and return the result
# square_ = lambda a: a ** 2
# print(square_(7))

# # Function to double the arguments value and return the result.
# double_ = lambda a: a * 2
# print(double_(20))

# # multiply arguments a with argument b and return the result.
# mul_ = lambda a, b: a * b
# print(mul_(11, 22))
# ______________________________________________________________________________________________________________________

# # A lambda can take any number of arguments.
# res = lambda a, b, c: a * b / c
# print(res(12, 6, 8))
# ______________________________________________________________________________________________________________________

# # Lambda Function returning multiple values.
# func = lambda a, b: (a + b, a - b)
# ans1, ans2 = func(4, 8)
# print(ans1)
# print(ans2)
# ______________________________________________________________________________________________________________________

# # It is better to use lambda function as anonymous function inside another function.
# # Make a function that always doubles the number you send in

# def myfunc(n):
#     return lambda a: a * n

# double_ = myfunc(2)         # RESULT = lambda a: a * 2
# print(double_(12))          # result = lambda 12: 12 * 2

# # make a same function that always triples the numnber you send in
# def myfunc(n):
#     return lambda a: a * n

# triple_ = myfunc(3)         # RESULT = lambda a: a * 3
# print(triple_(12))          # result = lmabda 12: 12 * 3

# # or use the same function definition to make both functions, in the same program
# def myfunc(n):
#     return lambda a: a * n

# double_ = myfunc(2)
# triple_ = myfunc(3)
# print(double_(12))
# print(triple_(12))
# ______________________________________________________________________________________________________________________

# # passing lambda function to another function
# def show(var):
#     print(var(5))

# show(lambda x: x * x / x)
# ______________________________________________________________________________________________________________________

# def show1(var):
#     return var(5, 8)

# ans = show1(lambda x, y: x * y)
# print(ans)
# ______________________________________________________________________________________________________________________

# map() ==> The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# We can use many number of iterables in map.

# # perform addition by sending teo iterable objects into function
# l1 = [71, 27, 83, 59, 15, 85]
# l2 = [28, 54, 72, 89, 53, 12]
# l3 = [453, 788, 99, 36, 23, 344]
# def addition(a, b, c):
#     return a + b + c

# res = map(addition, l1, l2, l3)
# print(res)

# # map() with lambda function
# ans2 = list(map(lambda a, b, c: a + b + c, l1, l2, l3))
# print(ans2)

# ans3 = list(map(lambda a: a**2 if  a > 50 else 0, l2))
# print(ans3)
# ______________________________________________________________________________________________________________________

# # filter() ==> filters the items in iterable based on given condition and returns True values.
# # We can give only one iterable to filter.

# # filter out even numbers from given list.
# l = [71, 27, 83, 56, 76, 43, 88, 345, 2, 52, 11, 534]
# def evenNumber(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False

# res = filter(evenNumber, l)     #this will rerturn a filter object
# print(res)                      # eg. <filter object at 0x000001EBBE90BF10>

# res1 = list(filter(evenNumber, l))      # convert it into list to print elements in it
# print(res1)

# res2 = list(filter(lambda a: True if a % 2 != 0 else False, l))
# print(res2)
# ______________________________________________________________________________________________________________________

# # reduce() ==> the reduce() function accepts a function and a sequence returns a single value.
# # Initially, the function is called with the first two items from the sequence and the result is returned.
# # The result is compared with next item in the sequence and so on.

# # Add all element in list and return final result.

# from functools import reduce            # reduce() function is used for

# l1 = [81, 52, 35, 62, 21, 68, 23]
# l2 = [28, 91, 54, 24, 36, 41, 66]
# x = reduce(lambda a, b: a if a > b else b, l1)
# y = reduce(lambda a, b: a if a > b and a < reduce(lambda a, b: a if a > b else b, l1) else b, l1)
# print(y)
# print(x)

# l1 = [71, 27, 83, 59, 15, 86]
# l2 = [28, 91, 54, 24, 36, 41]

# # iterate two list simultaneously and give the largest element after each iteration.
# # form new list of the largest elements we get after each iteration.
# # from new list formed filter out those elements which are greater than 40 and smaller than 70.
# # finally give the largest element from filtered elements.

# ans = reduce(lambda a, b: a if a > b else b, filter(lambda x: 40 <= x <= 70, map(lambda y, z: y if y > z else z, l1, l2)))
# print(ans)

# # iterate two list simultaneously and give the largest element after each iteration.
# # form new list of the largest elements we get after each iteration.
# # from new list formed filter out even numbers.
# # finally give the largest element from filtered elements.

# ans1 = reduce(lambda a, b: a if a > b else b, filter(lambda x: x % 2 == 0, map(lambda y, z: y if y > z else z, l1, l2)))
# print(ans1)
# ______________________________________________________________________________________________________________________

# factorial using lambda function
# func = lambda a: 1 if a == 0 else a * func(a - 1)
# print(func(5))

# abc=[10,20,30,[40,50]]
# n=len(abc)
# for i in range(abc):
#     if type(list[i]) is list:
#         if len(abc[i])>1:
#             m=len(abc[i])
#             for j in range(m):
#                 print(i,"=",j,"=",abc[i][j])
#     else:
#         print(i,"=",list[i])

# def sc(tt):
#     return[j for i in reversed(tt)]


# tt=[5,6,7,8,9]

# print(sc(tt))

# l1=[1,2,3,4]
# l2=[2,3,4,5]
# x=list(map(lambda x,y:x+y,l1,l2))
# print(x)

# l1=[1,2,3,4]
# l2=[2,3,4,5]
# l3=[]
# for i in zip(l1,l2):
#     l3.append(sum(list(i)))
# print(l3)


# s = '+919561489883 9422819890 +918605031487 8474525885'

# s1 = s.split(' ')
# l1 = [ ]
# for i in s1:
#     if '+91' in i:
#         l1.append(i)
# print(l1)

# s2 = s.split(" ")
# l2 = []
# for j in s2:
#     if "+91" not in j:
#         l2.append(j)
# print(l2)
# ______________________________________________________________________________________________________________________

# # Given a list of names, output a list that contains only the names that consist of more than 5 characters.

# names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]
# result = list(map(lambda x: len(x) > 5, names))
# print(result)

# fruits = ["apples", "oranges", "bananas", "melons"]
# prices = [20, 30, 40, 35]
# quantities = [5, 6, 8, 4]

# for fruit, price, quantity in zip(fruits, prices, quantities):
#     print(f"You bought {quantity} {fruit} for ${price*quantity}")

# l = [10, 20, 30, [40, 50]]

# for i, j in zip(range(len(l)), l):
#     if type(j) == int:
#         print(i, " ", j)
#     if type(j) == list:
#         for k in range(len(j)):
#             print(i, k, j[k])

# alien = {"color" : "red", "bird" : "parrot"}
# print(alien["color"])
# print(alien["bird"])

# ______________________________________________________________________________________________________________________
# Lambda (anonymous function.)
# def square(a):
#     return a*a

# l = lambda a, b: a*b
# result = l(3, 4)
# print(result)
# ______________________________________________________________________________________________________________________

# from functools import reduce
# lst = [1, 2, 3, 45]
# result = reduce((lambda x, y: x + y), lst)
# print(result)
# ______________________________________________________________________________________________________________________

# f = lambda x: bool(x % 2)
# print(f(20), f(21))
#  _____________________________________________________________________________________________________________________


# fact_ = lambda n: 1 if n == 0 else n * fact_(n - 1)
# print(fact_(6))


# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# v = list(filter(lambda x: (x % 2 == 0), l1))
# print(v)

# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# v = list(map(lambda x: (x % 2 == 0), l1))
# print(v)

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# v = list(map(lambda x: (x**2), li))
# print(v)

// find Python Program for bubble sort?