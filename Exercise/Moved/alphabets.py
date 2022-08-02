from functools import reduce

l = [81, 52, 35, 62, 21, 68, 23]

x = reduce(lambda a, b: a if a > b else b, l)
y = reduce(lambda a, b: a if a > b and a < reduce(lambda a, b: a if a > b else b, l) else b, l)
print(y)
print(x)