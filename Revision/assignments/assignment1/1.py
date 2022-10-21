# Python Program for factorial of a number with and without recursion

# with recursion
# def fact(n1):
#     if n1 == 0:
#         return 1
#
#     return n1 * fact(n1 - 1)
#
#
# num = int(input("enter the number for factorial: "))
# print("The factorial of {} is {}".format(num, fact(num)))
# ______________________________________________________________________________________________________________________

# without recursion.
# using while loop

# n = int(input("enter the number for factorial: "))
# fact = 1
# while n > 0:
#     fact *= n
#     n -= 1
# print("the factorial is: ", fact)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# using for loop

n = int(input("enter the number gor factorial: "))
fact = 1
for i in range(1, (n + 1)):
    fact *= i
print("the factorial is: ", fact)
