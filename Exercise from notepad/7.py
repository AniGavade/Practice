#  Write a program to find the lowest number out of two numbers excepted from user.

# By using List method, sort method.

# l = [10, 20, 4, 45, 99]
# l.sort()
# print("Smallest number is: ", *l[:1])

# ///////////////////////////////////////////////////////////////////////

#  min list element on inputs provided by user. 
#  Using methods of range, append, and min

# l = []

# n = 2
# for i in range(1, n + 1):
#     ele = int(input("Enter Elements: "))
#     l.append(ele)

# print("Smallest element is:", min(l))

# ///////////////////////////////////////////////////////////////////////////////

# By using for loop.

# l = [ int(1) for l in input("list: ").split(",")]
# print("The list is ", l)

# min1 = l[0]

# for i in range(len(l)):

#     if l[i] < min1:
#         min1 = l[i]

# print("The Smallest element in the list is ", min1)

# ________________________________________________________________________________________________________________________

# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))

# d = min(a, b)
# while a % d != 0 or b % d != 0:
#     d -= 1
# print(d)

