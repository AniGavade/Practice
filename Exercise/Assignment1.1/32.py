#  print all positive numbers in a range

# By using for loop.
# start,  end = -13, 8
# for i in range(start, end):
#     if i >= 0:
#         print(i, end =" ")
# ____________________________________________________________________________________________________________________________________________________________

# by using for loop with user input.
# l = []
# n = int(input("enter the number of elements: "))
# for i in range(0, n):
#     ele = int(input("Enter the number: "))
#     l.append(ele)

# print(l)
# for i in l:
#     if i >= 0:
#         print(i, end= " ")
# _______________________________________________________________________________________________________________________________________________________

# by using for loop with user input.
# start = int(input("Enter the number of element in negative: "))
# end = int(input("Enter the number of element in positive: "))
# for i in range(start, end):
#     if i >= 0:
#         print(i, end = " ")
# _______________________________________________________________________________________________________________________________________________________

# List comrehention by user input.
# l = []
# n = int(input("enter the number of elements: "))
# for i in range(n):
#     ele = int(input("Enter the element number: "))
#     l.append(ele)

# print("original list: ", l)
# pos = [x for x  in l if x >= 0]
# print(pos)
# _____________________________________________________________________________________________________________________________________________________

# by using lambda function with user input.
# l = []
# n = int(input("Enter the number of element: "))
# for i in range(n):
#     ele = int(input("Enter the element number: "))
#     l.append(ele)

# print("Original list: ", l)
# pos = list(filter(lambda x: x >= 0, l))
# print("The positive numbers from list: ", pos)