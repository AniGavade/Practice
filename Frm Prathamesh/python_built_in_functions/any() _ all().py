# any() : This function returns True if any element of an iterable is True. If not, it returns False.

# # True since 1,3 and 4 (at least one) is true
# l = [1, 3, 4, 0]
# print(any(l))
#
# # False since both are False
# l1 = [0, False]
# print(any(l1))
#
# # True since 5 is true
# l2 = [0, False, 5]
# print(any(l2))
#
# # False since iterable is empty
# l3 = []
# print(any(l3))

# # At east one (in fact all) elements are True
# s = "This is good"
# print(any(s))
#
# # 0 is False
# # '0' is True since it's a string character
# s1 = '000'
# print(any(s1))
#
# # False since empty iterable
# s2 = ''
# print(any(s2))

# In the case of dictionaries, if all keys (not values) are false or the dictionary is empty, any() returns False.
# If at least one key is true, any() returns True.

# # 0 is False
# d = {0: 'False'}
# print(any(d))
#
# # 1 is True
# d1 = {0: 'False', 1: 'True'}
# print(any(d1))
#
# # 0 and False are false
# d2 = {0: 'False', False: 0}
# print(any(d2))
#
# # iterable is empty
# d3 = {}
# print(any(d3))
#
# # 0 is False
# # '0' is True
# d4 = {'0': 'False'}
# print(any(d4))

# ----------------------------------------------------------------------------------------------------------------------

# all() : This function returns True if all elements in the given iterable are true. If not, it returns False.
# returns true for empty iterable

# # all values true
# l = [1, 3, 4, 5]
# print(all(l))
#
# # all values false
# l1 = [0, False]
# print(all(l1))
#
# # one false value
# l2 = [1, 3, 4, 0]
# print(all(l2))
#
# # one true value
# l3 = [0, False, 5]
# print(all(l3))
#
# # empty iterable
# l4 = []
# print(all(l4))

# s = "This is good"
# print(all(s))
#
# # 0 is False
# # '0' is True
# s = '000'
# print(all(s))
#
# s = ''
# print(all(s))

# s = {0: 'False', 1: 'False'}
# print(all(s))
#
# s = {1: 'True', 2: 'True'}
# print(all(s))
#
# s = {1: 'True', False: 0}
# print(all(s))
#
# s = {}
# print(all(s))
#
# # 0 is False
# # '0' is True
# s = {'0': 'True'}
# print(all(s))



