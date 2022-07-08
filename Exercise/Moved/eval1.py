n = int(input("Enter the number of rows: "))
k = n
l = n-1
for i in range(n):
	for j in range(k):
		print(end= " ")
	for j in range (i + 1):
		print("*",end= " ")
	k = k-1
	print()
for i in range(n-1):
	for j in range(i+1):
		print(end=" ")
	for j in range(l):
		print(" *",end = "")
	l = l-1
	print()