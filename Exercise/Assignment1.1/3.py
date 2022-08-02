# Python program to print all Prime numbers in an Interval

# l = int(input("Enter the lowest range number"))
# u = int(input("Enter the upper range number"))
# for i in range(l, u+1):
#     if i > 1:
#         for j in range(2, (i//2)+1):
#             if (i % j) == 0:
#                 break
#         else:
#             print(i, end=" ")

# for i in range(1, 25):
#     if i > 1:
#         for j in range(2, (i//2)+1):
#             if (i % j) == 0:
#                 break
#         else:
#             print(i, end=" ")
# ______________________________________________________________________________________________________________________

# s1 = {3, 4, 5, 6, 0}
# s2 = {9, 5, 6, 1, 8}
# for i in s1:
#     for j in s2:
#         if i + j == 9:
#             print(i, ",", j)
# ______________________________________________________________________________________________________________________

s1 = {3, 4, 5, 6, 0}
s2 = {9, 5, 6, 1, 8}


def func(a, b):
    for i in b:
        if i+a == 9:
            return [a, i]


f_res = []

for i in s1:
    res = func(i, s2)
    if res:
        f_res.append(res)


print(f_res)
