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

def decor1(func1):
    def check():
        print("Lets check")
        func1()
        print("Here")
    return check

@decor1
def data():
    print("It exist")

data()