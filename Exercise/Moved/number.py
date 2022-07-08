l1 = (1, 2, 3, [], 4, [])
l2 = []

if i in l1:
	if i != []:
		l2.append(i)
		l1, l2 = l2, l1
print(l1)