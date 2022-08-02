# Python Program to Split the array and add the first part to the end
# def splitArr(arr, n, k):
#     for i in range(0, k):
#         x = arr[0]
#         for j in range(0, n - 1):
#             arr[j] = arr[j + 1]
#
#         arr[n - 1] = x
#
#
# arr = [12, 10, 5, 6, 52, 36]
# n = len(arr)
# position = 1
#
# splitArr(arr, n, position)
#
# for i in range(0, n):
#     print(arr[i], end=", ")
# print()


arr = []
n = int(input("number of elements in array: "))
for i in range(n):
    ele = int(input("Enter the number: "))
    arr.append(ele)
print(arr)
m = int(input("element number from rotate the array: "))
for i in range(m):
    y = arr.pop(0)
    arr.append(y)
print(arr)
