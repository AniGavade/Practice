# print all even numbers in a range
# for i in range(512):
#     if i % 2 == 0:
#         print(i, end=" ")
# _______________________________________________________________________________________________________________________________________________________

# by using list comprehension.
# l = [x for x in range(50) if x%2==0]
# print(l)
# _______________________________________________________________________________________________________________________________________________________

# By taking user input.
# start = int(input("Enter the starting number of range: "))
# end = int(input("Enter the ending number of range: "))
# for i in range(start, end):
#     if i % 2 == 0:
#         print(i, end=" ")
# _______________________________________________________________________________________________________________________________________________________

l = [23, 43, 46, 21, 34, 36, 78, 15, 72, 47, 67]
evenlst = list(filter(lambda x: (x % 2 == 0), l))
print(evenlst)