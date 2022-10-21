# a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

# Create Generators in Python

# It is as easy as defining a normal function, but with a yield statement instead of a return statement. If a
# function contains at least one yield statement (it may contain other yield or return statements), it becomes a
# generator function. Both yield and return will return some value from a function.
# The difference is that while a return statement terminates a function entirely, yield statement pauses the function
# saving all its states and later continues from there on successive calls.

# Differences between Generator function and Normal function

# Generator function contains one or more yield statements.
# When called, it returns an object (iterator) but does not start execution immediately.
# Methods like __iter__() and __next__() are implemented automatically.So we can iterate through the items using next().
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and their states are remembered between two successive calls.
# Finally, when the function terminates, StopIteration is raised automatically on further calls.

# interesting thing to note in generator is that the value of local variable is remembered between each call.
# Unlike normal functions, the local variables are not destroyed when the function yields.
# Furthermore, the generator object can be iterated only once.
# To restart the process we need to create another generator object
#
#
# list1 = [1, 2, 3, 4, 5, 6, 7]
#
#
# def sno(var):
#     for i in var:
#         yield i * i
#
#
# ans = sno(list1)
#
# print(next(ans))      # returns only one result and pause the function
# print(next(ans))      # returns next result, started from where it left in previous operation.
# print("-------------------------------")
# for i in ans:           # iterate over the generator object
#     print(i)
#
# print(list(ans))
#
# sq = (i*i for i in list1)     # we can also create generator object using tuple comprehension.
#
# for i in sq:
#     print(i)
# print("-------------------------------")

# fibonacci series using generator
# def fibo():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b
#
#
# for i in fibo():
#     if i >= 100:
#         break
#     print(i)

# ______________________________________________________________________________________________________________________

# def fibo():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b
#
#
# count = 0
# num = int(input('enter the number of values you want:\n'))
# for i in fibo():
#     print(i)
#     count += 1
#     if count >= num:
#         break
# ______________________________________________________________________________________________________________________

def nym_generator():
    for i in range(1, 11):
        yield i


gen = nym_generator()
print("values obtained from generator function are: ")
for j in gen:
    print(j)


def display(**kwargs):

    print(kwargs)
    print(type(kwargs))


display(a="Kelly", b=9000, c=3000, d="Mohan")
