# print all odd numbers in a range

# by using for loop
# for i in range(23, 69):
#     if i % 2 == 1:
#         print(i, end=" ")
# ____________________________________________________________________________________________________

# By using list comprehension
# l = [x for x in range(45, 90) if x% 2 != 0]
# print(l)
# ____________________________________________________________________________________________________

# By taking user input.
# start = int(input("Enter the starting number of range: "))
# end = int(input("Enter the ending number of range: "))
# for i in range(start, end):
#     if i % 2 != 0:
#         print(i, end=" ")
# _____________________________________________________________________________________________________

# # By using filter lambda
# l = [23, 43, 46, 21, 34, 36, 78, 15, 72, 47, 67]
# oddlst = list(filter(lambda x: x % 2 != 0, l))
# print(oddlst)