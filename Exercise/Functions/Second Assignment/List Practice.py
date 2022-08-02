# 1. Python program to interchange first and last elements in a list
# lst = []
# n = int(input("Enter the element list numbers: "))
# for i in range n):
#     num = int(input("Enter the number in the list: "))
#     lst.append(num)
# print(lst)
# # first = lst[-1]
# # lst[-1] = lst[0]
# # lst[0] = first()
# # print("the new list is: ", lst)
# # ______________________________________________________________________________________________________________________________________________________________

# # 2. Python program to swap two elements in a list

# # Python Program to Swap Two Elements in a List using Function.

list1 = []
 
#how many elements in list
Number = int(input("How many elements in list :- "))
     
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element :- " %i))
    list1.append(value)
 
#print list before swapping
print("\nList before swapping of elements :-\n",list1)
 
#take position to swap
position1 = int(input("Enter the position 1 of element, which you want to swap :- "))
position2 = int(input("Enter the position 1 of element, which you want to swap :- "))
 
# Swap function 
def swapPositions(list, pos1, pos2): 
       
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
   
print("List after swapping of elements :-\n",swapPositions(list1, position1-1, position2-1)) 


# Python Program to Swap the First and Last Value of a List.
# Python Program to Swap Two Elements in a List using Inbuilt POP() and Insert() Function


# _______________________________________________________________________________________________________________________________________________________________

# 3. Python | Ways to find length of list
# lst = [2, 3, 4, 5, 6, 7, 8]
# print(lst)

# count = 0
# for i in lst:
#     count += 1
# print("The length of list by using for loop method is: ", count)

# lst = [2, 3, 4, 5, 6, 7, 8]
# print(lst)
# print("The length of list by using len() method is: " len(lst))

# a  = "Yaha bhi hoga, vaha bhi hoga, ab toh saare jahaan me hoga. kya? Mera hi jalwa."
# print(a)

# count = 0
# for i in a:
#     count += 1
# print(count)
# ________________________________________________________________________________________________

# l = [2, 3, 4, 5, 6]
# b = (9, 8, 7, 6)

# l += b # l = l + b

# print(l)
# print(type(l))  

# ______________________________________________________________________________________________________________________
