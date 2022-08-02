# Ways to check if element exists in list

# 1. Using "in" method.
# l = [1, 3, 6, 7, 8, 2, 9, 4]
# for i in l:
#     if i == 4:
#         print("Element exist")
#
# print("Checking if 4 existing in list (using in): ")
#
# if 4 in l:
#     print("Element exists.")

# __________________________________________________________________________________________________________________
# By using sort() + bisect_left() method

from bisect import bisect_left

ts = [1, 3, 6, 7, 8, 2, 9, 4]
tb = [1, 3, 6, 7, 8, 2, 9, 4]
ts = set(ts)
if 4 in ts:
    print("Element exist")
print("Checking if 4 existing in list: ")
tb.sort()
if bisect_left(tb, 4):
    print("Element Exist")