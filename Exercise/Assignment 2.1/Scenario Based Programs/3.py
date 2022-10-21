# Python Program for Bubble Sort

lst = [34, 81, 7, 4, 13, 51, 93, 9, 81]
for i in range(len(lst)-1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            x = lst[j+1]
            lst[j+1] = lst[j]
            lst[j] = x
print(lst)

