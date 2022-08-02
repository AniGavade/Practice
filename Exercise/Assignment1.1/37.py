# Program to print duplicates from a list of integer

# l = [12, 23, 37, 4, 51, 23, 37, 42, 7, 9, 51]
# l1 = []
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#         print(i, end=' ')

# _____________________________________________________________________________________________________

# lst = [3, 6, 9, 12, 3, 30, 15, 9, 45, 36, 12, 12]
# dupEle = []
# uniqEle = {}
# for i in lst:
#     if i not in uniqEle:
#         uniqEle[i] = 1
#     else:
#         if uniqEle[i] == 1:
#             dupEle.append(i)
#         uniqEle[i] += 1
# print(dupEle)

# __________________________________________________________________________________________________________

# n = [3, 6, 9, 12, 3, 30, 15, 9, 45, 36, 12, 12]
#
# dupEle = [x for x in n if n.count(x) > 1]
# uniqEle = list(set(dupEle))
# print(uniqEle)

# ________________________________________________________________________________________________________________

# def uniqEle():
#     for i in l:
#         if i not in l1:
#             l1.append(i)
#         else:
#             print(i, end=" ")
#
#
# l = [3, 6, 9, 12, 3, 30, 15, 9, 45, 36, 12, 12, 12, 12]
# l1 = []
# uniqEle()

# _____________________________________________________________________________________________________________
# l = [3, 6, 9, 12, 3, 30, 15, 9, 45, 36, 12, 12, 12, 12]
# for i in range(len(l)-1, -1, -1):
#     if l.count(l[i]) == 1:
#         l.remove(l[i])
# for j in range(len(l)-1, -1, -1):
#     if l.count(l[j]) > 1:
#         l.remove(l[j])
# print(l)
