# Remove empty tuples from a list.
l = [34, (), 12, 87, (), 65, (), ()]
empty_tuple = list(filter(lambda x: x != (), l))
print(empty_tuple)