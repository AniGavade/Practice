# Count occurrences of an element in a list

# By using counter.
# from collections import Counter
# names = ["break", "the", "rules", "do", "not", "break", "the", "heart"]
# ele = "break"
# cnt = Counter(names)
# print("Given element: ", ele)
# print("Count of element: ", cnt[ele])
# ____________________________________________________________________________________________________________________________________________________________________

# By using count
# names = ["break", "the", "rules", "do", "not", "break", "the", "heart"]
# cnt = names.count("break")
# print(cnt)
# _____________________________________________________________________________________________________________________________________________________

# l = [1, 2, 3, 4, 5, 6, 21, 8, 3, 5, 9, 667, 2, 3, 5]
# l1 = l.count(21)
# print(l1)
# _____________________________________________________________________________________________________________________________________________________

# def cntEle(l, x):
#     count = 0
#     for i in l:
#         if i == x:
#             count += 1
#     return count

# l = [1, 2, 3, 4, 5, 6, 5, 8, 3, 5, 9, 667, 2, 3, 5]
# x = 5
# print(f"{x} has occured {cntEle(l, x)} times")
# _________________________________________________________________________________________________________________________________________________

# def word(l, x):
#     count = 0
#     for i in l:
#         if i == x:
#             count +=1
#     return count

# l = ["Prashant", "Yogesh", "Mohan", "Rohit", "Sameer", "Prashant", "Mohan", "Prashant"]
# x = "Prashant"
# print("{} has occured {} times in list".format(x, word(l, x)))
# __________________________________________________________________________________________________________________________________________________

