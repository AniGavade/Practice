import sys
# global keyword -
# Global keyword is a keyword that allows a user to modify a variable outside the current scope.
# It is used to create global variables from a non-global scope i.e. inside a function.
# Global keyword is used inside a function only when we want to do assignments or when we want to change a variable.
# Global is not needed for printing and accessing.

# If we need to assign a new value to a global variable then we can do it by declaring the variable as global.

# x = 15
# print("Value of x before changing :", x)
#
#
# def change():
#     x = 100
#     x = x + 5
#     print("Value of x inside a function :", x)
#
#     def change2():
#         global x
#         x = x + 10
#         print("value of x inside change 2 :", x)
#
#     change2()
#     print("value of x after changing it inside change2: ", x)
#
#
# change()
#
# print("Value of x outside a function :", x)

# ==============================================================================================================
# Nonlocal Variables
# Nonlocal variables are used in nested functions whose local scope is not defined.
# This means that the variable can be neither in the local nor the global scope.
# nonlocal keyword won't affect global keyword.
# it also won't affect to local variable which are present nested function to that function.
# If we change the value of a nonlocal variable, the changes appear in the local variable which are above to that
# nonlocal variable.

x = 25


def outer():
    x = 10
    print("outer x before changing:", x)

    def inner():
        nonlocal x
        x = 20
        print("inner x after making it nonlocal:", x)

        def innerInner():
            x = 30
            print("innerInner x after making value of x nonlocal in above scope:", x)
        innerInner()

    inner()
    print("outer x after changing:", x)


outer()
print("global x after changing :", x)

# ==============================================================================================================
