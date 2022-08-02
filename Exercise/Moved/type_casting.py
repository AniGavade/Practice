list1 = [1, 2, 3, [], 4, [], 5]
list2 = []

for i in list1:
    if i != []:
        list2.append(i)

list1 ,list2 = list2,list1
del list2
print(list1)