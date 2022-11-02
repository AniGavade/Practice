"""The zip() : zip() function returns a zip object, which is an iterator of tuples where the first item in each passed
Onterator is paired together, and then the second item in each passed iterator are paired together
if etc:
If the passed iterators have differnet lengths, the iteratr with the least items decides the length of the new iterator.
"""

l1 = ['a', 'c', 'e', 'e', 'm', 'q', 'y']
m1 = [1, 8, 6, 2, 9, 2, 6]
n1 = ['A', 'C', 'E', 'E', 'M']

lst_ = zip(l1, m1)
out_ = list(lst_)
print(out_)


sorted_list = sorted(out_, key=lambda a: (a[0], a[1]))
print(sorted_list)

lst2_ = zip(l1, n1)
out2_ = list(lst2_)
print(out2_)