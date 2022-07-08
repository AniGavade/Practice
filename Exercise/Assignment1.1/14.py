# Ways to find length of list

# Using len() method

# l = ["Ani", "Pankaj", "Ravi", "Shankar", "Mahesh", "Ravi", "Mahesh", "Ani", "Ravi"]
# print(len(l))
# ______________________________________________________________________________________________________________________

# By using the Naive method

# l = [1, 2, 3, 4, 5, 6, 7]
# count = 0
# for i in l:
#     count += 1
# print(count)

# ______________________________________________________________________________________________________________________

# By using the length_hint() method

# from operator import length_hint
#
# l = ["Teambrainworks", "Training", 1, 4, "Java", "Python"]
# length_l = length_hint(l)
# print(length_l)