# Global variables.
# Local variables.
#========================================================================


#Recursive Function.

#a function call itself is recursive function.
#1. reduce length of code and improves readability.
#2. Very complex problem we can solve very easily.
# towers of hanoi.
#3. 


#Recursion variation
# 1. Direct
# 2. Indirect.
# 3. Nested
# 4. Excessive
# 5. Tail.

# example of indirect recursion.
# def is_even(x):
#     if x==0:
#         return True
#     else:
#         return is_odd(x-1)

# def is_odd(x):
#     return not is_even(x)

# print(is_even(2))
# print(is_odd(3))
#============================================================================

# def fib(x):
#     if x==0 or x==1:
#         return 1
#     else:
#         return fib(x-1)+ fib(x-2)
# print(fib(4))
#============================================================================


# def reverse(str):
#     if len(str) == 0:
#         return str
#     else:
#         return reverse(str[1:]) + str[0]


# mystr = "BeginnersBook"

# print("The Given String  is: ", mystr)

# print("Reversed String is: ", reverse(mystr))