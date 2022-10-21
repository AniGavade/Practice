# # Python Program for Reversal algorithm for array rotation
# arr = [10, 25, 36, 43, 52, 60]
# print("The original list is: ", arr)
# arr = arr[::-1]
# print(arr)
# ____________________________________________________________________________________________________
#  By using generator.
# def reverse_list(n):
#     # Traverse [n-1, -1) , in the opposite direction.
#     for i in range(len(n)-1, -1, -1):
#         yield n[i]
#
#
# print(list(reverse_list([1, 2, 3, 4, 5, 6, 7])))
# ____________________________________________________________________________________________________

arr = [10, 25, 36, 43, 52, 60]
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=", ")
# ____________________________________________________________________________________________________

# arr = [10, 20, 30, 40, 50, 60]
# l = []
# for i in arr:
#     l.insert(-i, i)
# print(l)

