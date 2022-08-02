l1= [1,2,3,4,5,7,10]
l2= [6,7,8,9,2,5,3,10]
l1.extend(l2)
print(l1)

newlist =[]
for item in l1:
    if item not in newlist:
        newlist.append(item)
print(newlist)