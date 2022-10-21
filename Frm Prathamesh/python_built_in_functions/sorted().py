# sorted() : Sorted() sorts any sequence (list, tuple) and always returns a list with the elements in a sorted manner,
# without modifying the original sequence.
# It takes three argument, iterable, key(optional), reverse(optional)
# Reverse in sorted:
# If set true, then the iterable would be sorted in reverse (descending) order, by default it is set as false.
# key in sorted():
# This argument expects a function to be passed to it, and that function will be used on each value in the list being
# sorted to determine the resulting order.
#
# Difference between .sort() and sorted() :
# sorted() won't change original iterable but .sort() changes the original iterable.


m1 = [1, 8, 6, 2, 9, 2, 6]
print(f'original list before sorting : {m1}')

m2 = sorted(m1)
print(f'original list after sorting : {m1}')  # original list won't change even after using sorted()
print(f'new list after sorting : {m2}')


# reverse in sorted
m3 = sorted(m1, reverse=True)
print(f'new list after sorting and reversing : {m3}')


# if we want to sort list based on length of the elements of a list
m4 = ['333', '55555', '1', '333', '666666', '22']
print(f'original list before sorting : {m4}')

m5 = sorted(m4, key=len)
print(f'new list after sorting : {m5}')


# if we want to sort list of tuples based on 2nd element of tuple
m6 = [('a', 7), ('j', 9), ('m', 3), ('d', 5), ('q', 2)]
print(f'original list before sorting : {m6}')

m7 = sorted(m6, key=lambda a: a[1])
print(f'new list after sorting based on 2nd element of tuple : {m7}')


# if we want to sort list of tuple based on length of 2nd element of tuple
m8 = [('a', '22'), ('j', '55555'), ('m', '333'), ('d', '1'), ('q', '4444')]
print(f'original list before sorting : {m8}')

m9 = sorted(m8, key=lambda a: len(a[1]))
print(f'new list after sorting based on 2nd element of tuple : {m9}')