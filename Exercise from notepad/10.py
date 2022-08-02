# Write a program to find the largest number out of three numbers excepted from user.

l = []

n = 3
for i in range(1, n + 1):
    ele = int(input("Enter Elements: "))
    l.append(ele)

print("Maximum element is:", max(l))