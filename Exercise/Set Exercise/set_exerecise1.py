# # a = {"apple", "banana", "strawberry"}

# # for x in a:
# #     print(x)

# a = {"apple", "banana", "strawberry"}
# a.discard("banana")

set1 = {"a", "b" , "a" , "c"}
set2 = {1, 2, 3, 2, 2, 3}

set1.update(set2)   #it excluded any duplicate values/items
print(set1)
