# Find the unique element(s) from a given list that only occurs once by using list comprehension.

# a = [2, 4, 4, 3, 5, 2, 3, 9, 8, 7, 6]
# print(type(*[x for x in a if a.count(x) == 1]))
# print([x for x in a if a.count(x) == 1])

# print(", ".join(str(x) for x in a if a.count(x) == 1))

# for i in a:
#     if a.count(i) == 1:
#         print(i)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# By using function with for loop

# def lonely_int(a):
#     for i in a:
#         if a.count(i) == 1:
#             result = i
#             return result
#
#
# v = [2, 4, 4, 3, 5, 2, 3]
# print(lonely_int(v))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# By using list comprehension in function

# def lonely_int(a):
#     result = [x for x in a if a.count(x) == 1]
#     for i in result:
#         return i
#
#
# v = [2, 4, 4, 3, 5, 3, 2]
# print(lonely_int(v))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# By using list comprehension and join in function.

# def lonely_int(a):
#     result = [str(x) for x in a if a.count(x) == 1]
#     return "\n".join(result)
#
#
# v = [2, 3, 4, 4, 5, 2, 3, 9]
# print(lonely_int(v))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# By using join and list comprehension in one line. # MASTER SOLUTION.

# def lonely_int(a):
#     return ", ".join(str(x) for x in a if a.count(x) == 1)
#
#
# v = [2, 4, 4, 3, 5, 3, 2, 9]
# print(lonely_int(v))
# ______________________________________________________________________________________________________________________

