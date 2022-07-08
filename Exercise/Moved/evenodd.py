
# even numbers
list1 =[1,7,3,4,5,6,7,8,9]

for element in list1:
    if element %2 == 0:
        print(f"{element} is even")
        break
    else:
        print(f"{element} is odd")