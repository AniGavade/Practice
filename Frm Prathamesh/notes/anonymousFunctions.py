# anonymous functions are the function without function definition.
# we use lambda keyword in anonymous function.
# syntax ==> lambda (arguments) : expression
# A lambda function can take any number of arguments, but can only have one expression.
#
# # make square of argument a, and return the result.
# sqr = lambda a: a ** 2
# print(sqr(5))
#
# # function to double the argument value and return the result.
# double = lambda a: a * 2
# print(double(10))
#
# # multiply argument a with argument b and return the result:
# mul = lambda a, b: a * b
# print(mul(10, 20))
# ==============================================================================
#
# # A lambda function can take any number of arguments
# result = lambda a, b, c: a * b / c
# print(result(10, 9, 2))
# ==============================================================================
#
# lambda function returning multiple values
# func = lambda a, b: (a + b, a - b)
# ans1, ans2 = func(5, 10)
# print(ans1)
# print(ans2)
# ==============================================================================
#
# # it is better to use lambda function as anonymous function inside another function.
# # make a function that always doubles the number you send in
# def myFunc(n):
#     return lambda a: a * n
#
#
# double = myFunc(2)  # result = lambda a: a * 2
# print(double(10))  # result = lambda 10: 10 * 2
#
#
# # make a same function that always triples the number you send in
# def myFunc(n):
#     return lambda a: a * n
#
#
# triple = myFunc(3)
# print(triple(10))
#
#
# # Or, use the same function definition to make both functions, in the same program
# def myFunc(n):
#     return lambda a: a * n
#
#
# double = myFunc(2)
# triple = myFunc(3)
# print(double(10))
# print(triple(10))

# =================================================================================
# passing lambda function to another function.
# def show(var):
#     print(var(5))
#
#
# show(lambda x: x * x)
#
# ----------------------------------------------------------------------------------
# def show1(var):
#     return var(5, 8)
#
#
# ans = show1(lambda x, y: x * y)
# print(ans)
#
# =================================================================================
#
# # map() ==> The map() function executes a specified function for each item in an iterable.
# # The item is sent to the function as a parameter.
# # We can use many number of iterables in map.
#
# # perform addition by sending two iterable objects into function.
# l1 = [71, 27, 83, 59, 15, 86]
# l2 = [28, 91, 54, 24, 36, 41]
# l3 = [28, 91, 54, 24, 36, 41]
#
# def addition(a, b, c):
#     return a + b + c
#
#
# ans = map(addition, l1, l2, l3)  # this will return a map object
# print(ans)                   # eg. <map object at 0x0000024710317EE0>
# #
# ans1 = list(map(addition, l1, l2, l3))  # convert it into list to print elements in it.
# print(*ans1)
# #
# # map() with lambda function
# ans2 = list(map(lambda a, b, c: a + b + c, l1, l2, l3))
# print(ans2)
#
# ans3 = list(map(lambda a: a**2 if a > 50 else 0, l1))
# print(ans3)
#
# =================================================================================
#
# # filter() ==> filters the items in iterable based on given condition and returns true values.
# # we can give only one iterable to filter.
#
# # filter out even numbers from given list.
# l = [71, 27, 83, 59, 15, 86, 28, 91, 54, 24, 36, 41]
#
#
# def evenNumber(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
#
#
# ans = filter(evenNumber, l)  # this will return a filter object
# print(ans)  # eg. <filter object at 0x0000027EAE6B7F40>
#
# ans1 = list(filter(evenNumber, l))  # convert it into list to print elements in it
# print(ans1)
# #
# # # filter() with lambda function
# ans2 = list(filter(lambda a: True if a % 2 == 0 else False, l))
# print(ans2)
#
# # filter out odd numbers from given list
# ans3 = list(filter(lambda a: True if a % 2 != 0 else False, l))
# print(ans3)
#
# =================================================================================
#
# reduce() ==> The reduce() function accepts a function and a sequence and returns a single value
# Initially, the function is called with the first two items from the sequence and the result is returned.
# Then result is compared with next item in the sequence. And so on.
#
# # Add all elements in list and return final result.
    # from functools import reduce
#
# l = [71, 27, 83, 59, 15, 86, 28, 91, 54, 24, 36, 41]
#
#
# def addList(a, b):
#     return a + b
#
#
# ans = reduce(addList, l)
# print(ans)
#
# reduce() with lambda function
# ans1 = reduce(lambda a, b: a + b, l)
# print(ans1)
#
# # find maximum number in given list
# ans2 = reduce(lambda a, b: a if a > b else b, l)
# print(ans2)
# #
# =================================================================================
# from functools import reduce
# l1 = [71, 27, 83, 59, 15, 86]
# l2 = [28, 91, 54, 24, 36, 41]
# print(l1)
# print(l2)
#
# # iterate two list simultaneously and give the largest element after each iteration.
# # form new list of the largest elements we get after each iteration.
# # from new list formed filter out those elements which are greater than 40 and smaller than 70.
# # finally give the largest element from filtered elements.
#
# ans = reduce(lambda a, b: a if a > b else b, filter(lambda x: 40 <= x <= 70, map(lambda y, z: y if y > z else z,
# l1, l2))) print(ans)

# # iterate two list simultaneously and give the largest element after each iteration.
# # form new list of the largest elements we get after each iteration.
# # from new list formed filter out even numbers.
# # finally give the largest element from filtered elements.
#
# ans1 = reduce(lambda a, b: a if a > b else b, filter(lambda x: x % 2 == 0, map(lambda y, z: y if y > z else z, l1,
# l2))) print(ans1)
#
# =================================================================================
#
# factorial using lambda function
# func = lambda a: 1 if a == 0 else a * func(a - 1)
# print(func(5))

# ======================================================================================================================

# help("functools")
# print(help())