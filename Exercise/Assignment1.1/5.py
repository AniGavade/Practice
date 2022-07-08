# Python Program to find sum of array (using multiple approach)

arr = [92, 38, 24, 15]
ans = sum(arr)
print('Sum of the array is ', ans)

# ______________________________________________________________________________________________________________________


def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return (sum)


arr = [12, 3, 4, 15]

n = len(arr)

ans = _sum(arr)
print('Sum of the array is ', ans)
