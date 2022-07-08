# Python Program for array rotation

arr = [10, 25, 36, 43, 52, 60]
# print("Original list : " + str(arr))
arr = arr[1:] + arr[:1]
print("List after rotate: " + str(arr))

