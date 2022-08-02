# count positive and negative numbers in a list

# l = [-65, -87, 46, -9, 98, 78, 65, 345, -88]
# neg = list(filter(lambda x: x <= 0, l))
# pos = list(filter(lambda x: x >= 0, l))
# print(f"{len(neg)} is the count of negative number and {len(pos)} is the count of positive number")
# ___________________________________________________________________________________________________________________________________________________________________

# l = [-65, -87, 46, -9, 98, 78, 65, 345, -88]
# neg = [x for x in l if x <= 0]
# pos = [y for y in l if y >= 0]
# print("{0} is the count of negative number, {1} is the count of positive number.".format(len(neg), len(pos)))
# ___________________________________________________________________________________________________________________________________________________________________

# l = [-65, -87, 46, -9, 98, 78, 65, 345, -88]

# neg = 0
# pos = 0
# for i in l:
#     if i <= 0:
#         neg += 1
#     else:
#         pos += 1
# print("{0} nrgative numbers and {1} positive.".format(neg, pos))
# ____________________________________________________________________________________________________________________________________________________________________

# l = [-65, -87, 46, -9, 98, 78, 65, 345, -88]
# a = []
# for i in l:
#     if i <= 0:
#         a.append(i)
# print("{} is negative count {} is positive count".format(len(a), len(l)-len(a)))