# functions are subprogram used to compute value or perform particular task.
# function run only when we call it, function cannot run on its own.

# Advantages of functions
# 1. function provide us code re-usability ie write once and use many times.
# 2. function facilitate code of maintenance.
# 3. divide task into small task, so it helps you to debug the code.
# 4. you can remove or add new feature to function any time.

# =====================================================================================================================
# # function definition
# we can define a function using def keyword followed by function name with parenthesis.

# def add():
#     x = 10
#     y = 20
#     addition = x + y
#     print(addition)
#
#
# add()

# ======================================================================================================
# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.

# parameter vs arguments
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
#
# # function with no argument
# def subtract():
#     x = 10
#     y = 20
#     subtraction = y - x
#     print(subtraction)
#
#
# subtract()

# ----------------------------------------------------------------------------------------------------------
# # positional argument - Positional arguments are arguments that need to be included in the proper position or order.
# def info(name, age):
#     print(f"Hi, my name is {name}. I am  {age * 365.25} days old.")


# # This does what is expected
# info("Alice", 23.0)
# This doesn't
# info(23.0, "Alice")
#
# function with one parameter
# def disp(var):
#     var1 = 200
#     var2 = var + var1
#     print(var2)
#
#
# disp(101)


# # function with multiple parameter
# def disp1(var, var1):
#     var2 = var + var1
#     print(var2)
#
#
# disp1('Aniruddha ', 'Gavade')

# -------------------------------------------------------------------------------------------------------------------------
# # default argument - if we not pass any value to function then python will take default value.

# def mul(x, y=50):
#     multiplication = x * y
#     print(multiplication)
#
#
# mul(10)
# mul(10, 20)
#
# ----------------------------------------------------------------------------------------------------------------------
# keyword argument - These arguments are passed to the function with name-value pair
#                    so keyword arguments can identify the formal argument by their names.
# keyword argument's name and formal argument's name must match.
# no of arguments must be equal in formal and actual argument.
#
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
#   print("The youngest child is " + child1)
#   print("The youngest child is " + child2)
#
#
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# ==========================================================================================================================================
# # Dynamic Typing
# # parameter do not know which type of value they are about to receive until we pass it while function call.
# # So, type of value is determined only during runtime not compile time this is called dynamic typing.
#
# # Passing list as an argument
# # You can send any data types of argument to a function (string, number, list, dictionary etc.),
# # and it will be treated as the same data type inside the function.
#
# def my_func(food):
#     for i in food:
#         print(i)
#
#
# fruits = ['apple', 'banana', 'cherry']
# my_func(fruits)
#
# ====================================================================================================
# # return statement
# # return statement is used to return something from function.
#
#
# def func(var1, var2):
#     var3 = var1 + var2 + 50
#     return var3
#
#
# ans = func(100, 35)
# print(ans)
#
# ====================================================================================================
# # function returning multiple values
#
#
# def func1(var):
#     x = 10
#     y = var
#     addition = x + y
#     subtraction = x - y
#     return addition, subtraction
#
#
# add, sub = func1(20)
# print(add)
# print(sub)
#
# ===================================================================================================
# # Nested function - function inside another function
# def func2():
#     def show():
#         print("show function")
#
#     show()
#     print("outer function")
#
# ===================================================================================================
# # passing function as an argument
#
# def func3(var):
#     a = "func3 " + var()
#     print(a)
#     var()
#     print("func3")
#
#
# def disp1():
#     print("disp11")
#     return "disp1"
#
#
# func3(disp1)
#
# ==================================================================================================
# # function returning another function
#
# def func4():
#     def disp2():
#         return "disp2"
#     print("func4")
#     return disp2
#
#
# val = func4()
# print(val())

# -------------------



