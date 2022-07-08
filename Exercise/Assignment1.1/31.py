# print Negative numbers in a list

# By using for loop
# l = [-65, -87, 46, -9, 98, 78, 345, -88]
# for i in l:
#     if i <= 0:
#         print(i, end = " ")
# _______________________________________________________________________________________________________________________________________________

# By using for loop with user input.
# l = []
# n = int(input("enter the number of elements: "))
# for i in range(0, n):
#     ele = int(input("Enter the number: "))
#     l.append(ele)

# print(l)
# for i in l:
#     if i <= 0:
#         print(i, end= " ")
# _______________________________________________________________________________________________________________________________________________

# Using list comprehension.
# l = [-65, -87, 46, -9, 98, 78, 345, -88]
# ele = [x for x in l if x <= 0]
# print("The positive elements are: ", ele)
# _________________________________________________________________________________________________________________________________

# List comrehention by user input.
# l = []
# n = int(input("enter the number of elements: "))
# for i in range(n):
#     ele = int(input("Enter the element number: "))
#     l.append(ele)

# print("original list: ", l)
# pos = [x for x  in l if x <= 0]
# print(pos)
# _____________________________________________________________________________________________________________________________________________________

# by using lambda function.
# l = [-65, -87, 46, -9, 98, 78, 345, -88]
# pos = list(filter(lambda x: x <= 0, l))
# print(pos)
# _____________________________________________________________________________________________________________________________________________________

# by using lambda function with user input.
# l = []
# n = int(input("Enter the number of element: "))
# for i in range(n):
#     ele = int(input("Enter the element number: "))
#     l.append(ele)

# print("Original list: ", l)
# pos = list(filter(lambda x: x <= 0, l))
# print("The positive numbers from list: ", pos)