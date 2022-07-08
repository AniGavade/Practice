# # count Even and Odd numbers in a List
# l = [23, 43, 46, 21, 34, 36, 78, 15, 72, 47, 67]
# b = []
# for i in l:
#     if i % 2 == 0:
#         b.append(i)
# print("{0} even numbers and {1} odd numbers in list: ".format(len(b), len(l)-len(b)))

# _______________________________________________________________________________________________________________________________

# By using for loop.
# l = [23, 43, 46, 21, 34, 36, 78, 15, 72, 47, 67]

# even = 0
# odd = 0
# for i in l:
#     if i%2==0:
#         even += 1
#     else:
#         odd += 1
# print("{0} even numbers and {1} odds.".format(even, odd))
# _______________________________________________________________________________________________________________

# # By using lambda.
# l = [23, 43, 46, 21, 34, 36, 78, 15, 72, 47, 67]
# evenlst = list(filter(lambda x: x % 2 == 0, l))
# oddlst = list(filter(lambda x: x % 2 == 1, l))
# print("{1} even numbers and {0} odd numbers.".format(len(oddlst), len(evenlst)))
# _______________________________________________________________________________________________________________

# By using list comprehension.
# l = [23, 43, 46, 21, 34, 36, 78, 15, 72, 47, 67]
# evenlst = [x for x in l if x % 2 == 0]
# print("{} even numbers and {} odd numbers".format(len(evenlst), len(l)-len(evenlst)))
# ____________________________________________________________________________________________________________
