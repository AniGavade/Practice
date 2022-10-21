# def decorator_func(func):
#     def wrapper_func():
#         print("wrapper_func Worked")
#         return func()
#
#     print("decorator_func worked")
#     return wrapper_func
#
#
# def show():
#     print("Show Worked")
#
#
# decorator_show = decorator_func(show)
# decorator_show()
#
#
# @decorator_func
# def display():
#     print("display worked")
# display()
#

# def dec1(func1):
#     def nowexec():
#         print("executing now")
#         func1()
#         print("Executed")
#     return nowexec
#
#
# @dec1
# def who_is_developer():
#     print("I am developer")
#
#
# who_is_developer()

# def decor1(func1):
#     def check():
#         print("Lets check")
#         func1()
#         print("Here")
#     return check
#
# @decor1
# def data():
#     print("It exist")
#
# data()
# ______________________________________________________________________________________________________________________

# code for testing decorator chaining

# def decor1(func):
#     def inner2():
#         print("inner2")
#         func()
#         print("inner2***")
#
#     return inner2
#
#
# def decor(func):
#     def inner1():
#         print("inner1")
#         func()
#         print("inner1***")
#
#     return inner1
#
#
# @decor
# @decor1
# def num():
#     print("hello")
#
#
# num()
# ______________________________________________________________________________________________________________________

# def decor_(func):
#     print("here executes the function ")
#     return func
#
#
# @decor_
# def normal_func(a, b):
#     print(f"the value of a = {a}, and value of b = {b}")
#
#
# normal_func(2, 4)
# ______________________________________________________________________________________________________________________

def outer(exp):
    def upper(fun):
        def inner():
            str1 = fun()
            a = str1.upper()
            return a + exp

        return inner

    return upper


@outer(" SWASTIK")
def str_fun():
    return "good morning"


print(str_fun())
