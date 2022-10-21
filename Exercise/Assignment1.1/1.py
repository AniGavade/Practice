# Python Program for factorial of a number with and without recursion
# : It is a function which calls itself.

# With recursion.

# def fact(n1):
#     if n1 == 1:
#         return n1
#
#     return n1 * fact(n1-1)
#
#
# num = int(input("User input: "))
# print("The factorial", num, "is", fact(num))

# ______________________________________________________________________________________________________________________

# Without recursion.

# n = int(input("Enter the number: "))
# fact = 1
# while n > 0:
#     fact = fact*n
#     n = n-1
#
#
# print("The factorial is", fact)

# ______________________________________________________________________________________________________________________

# f = int(input("enter the number to see factorial:"))
# fact = 1
# for i in range(1, (f+1)):
#     fact = fact * i
#
#
# print(f"Factorial of {f} = {fact}")
# ______________________________________________________________________________________________________________________

# # Factorial using lambda function
# fact_ = lambda n: 1 if n == 0 else n * fact_(n - 1)
# print(fact_(5))
# ______________________________________________________________________________________________________________________

# # factorial by using recursion method (lambda)
# recursive_lambda = (lambda func: lambda *args: func(func, *args))
# print(recursive_lambda(lambda self, x: x * self(self, x - 1) if x > 0 else 1)(5))
"""the name self is not a reserved keyword, it is merely a convention above pythonistas
to name the instance of the object on which the function applies.
here, the author uses the name self as the first argument to the lambda,
because this argument will receive an instance of an object on which the lambda will
apply the method specified in the argument named method"""
# ______________________________________________________________________________________________________________________
