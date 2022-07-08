# find sum of elements in list

# By using for loop.
# l = [534, 76, 63, 82, 37, 111]
# sum = 0
# for i in range(0, len(l)):
#     sum += l[i]
# print("The sum of elements in list: ", sum)
# ______________________________________________________________________________________________________________________________________

# By using while loop.
# l = [534, 76, 63, 82, 37, 111]
# ele = 0
# sum = 0
# while ele < len(l):
#     sum += l[ele]
#     ele += 1
# print("Sum of elements is: ", sum)
# _______________________________________________________________________________________________________________________________________________

# By using recursive method.

# def sumOflist(l, size):
#     if size == 0:
#         return 0
#     else:
#         return l[size - 1] + sumOflist(l, size-1)

# l1 = [534, 76, 63, 82, 37, 111]
# total = sumOflist(l1, len(l1))
# print(total)
# _________________________________________________________________________________________________________________________________________
