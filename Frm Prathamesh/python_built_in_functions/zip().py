# The zip() : zip() function returns a zip object, which is an iterator of tuples where the first item in each passed
# iterator is paired together, and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new
# iterator.

# l1 = ['a', 'c', 'e', 'e', 'm', 'q', 'y']
# m1 = [1, 8, 6, 2, 9, 2, 6]
# n1 = ['A', 'C', 'E', 'E', 'M']
#
# lst = zip(l1, m1)
# out = list(lst)
# print(out)
#
# sorted_list = sorted(out, key=lambda a: (a[0], a[1]))
# print(sorted_list)
#
# lst2 = zip(l1, n1)  # l1 and n1 has different length, so length of iterator equal to length of list which has fewer
# # elements
# out2 = list(lst2)
# print(out2)




