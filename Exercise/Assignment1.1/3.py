# Python program to print all Prime numbers in an Interval

# l = int(input("Enter the lowest range number"))
# u = int(input("Enter the upper range number"))
# for i in range(l, u+1):
#     if i > 1:
#         for j in range(2, (i//2)+1):
#             if (i % j) == 0:
#                 break
#         else:
#             print(i, end=" ")

for i in range(1, 121):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break 
        else:
            print(i, end=" ")
