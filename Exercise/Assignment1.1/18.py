# Cloning or Copying a list Python

# Using the slicing technique.
# l = [12, 45, 436, 76, 98, 34]
# print("Original list: ", l)
# l1_clone = l[:]
# print("After cloning: ", l1_clone)
# ____________________________________________________________________________________________________________________

# Using the extend() method.
# l = [12, 45, 436, 76, 98, 34]
# print("Original list: ", l)
# l1_clone = []
# l1_clone.extend(l)
# print("After coning: ", l1_clone)
# ____________________________________________________________________________________________________________________

#  By using =(assignment operator)
# l = [12, 45, 436, 76, 98, 34]
# print("Original list: ", l)
# l1_clone = l
# print("After Cloning: ", l1_clone)
# ____________________________________________________________________________________________________________________

# By using Shallow copy
# import copy
# l = [12, 45, 436, 76, 98, 34]
# print("Original list: ", l)
# l1 = copy.copy(l)
# print("After Copying: ",l1)
# ____________________________________________________________________________________________________________________

# By using list comprehension.
# l = [12, 45, 436, 76, 98, 34]
# print("original list: ", l)
# l1 = [x for x in l]
# print("After opying the list: ", l1)
# ____________________________________________________________________________________________________________________

# Using append() method.
# l = [12, 45, 436, 76, 98, 34]
# print("original list: ", l)
# l1 = []
# for i in l:
#     l1.append(i)
# print("After copying: ", l1)
# ____________________________________________________________________________________________________________________

# By using copy() method
# l = [12, 45, 436, 76, 98, 34]
# print("original list: ", l)
# l1 = []
# l1 = l.copy()
# print("New list after copying: ", l1)
# ___________________________________________________________________________________________________________________

