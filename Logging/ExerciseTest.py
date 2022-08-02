# Q. take a list which having the number 1 to 5, & append 100 in the given list.

# lst = [1, 2, 3, 4, 5]
# print(lst)
# lst.append(100)
# ______________________________________________________________________________________________________________________

# Q. Use list comprehension to create another list to give square the number from 1-10.

# s = [x*x for x in range(10)]
# print(s)
# ______________________________________________________________________________________________________________________

# Q. Take int list return second-largest number.
# l = [1, 2, 3, 4, 5, 6]
# print(l[-2])
# ______________________________________________________________________________________________________________________

# Q. Take a string & every word to be element of a list.
# a = "Welcome to the tommorowland Belgium"
# b = a.split(" ")
# print(b)
# ______________________________________________________________________________________________________________________

# Q.  Can we Pass the list as key into the dictionary?
# A. cannot use a list as a key because lists are mutable.

# Q.  Can we Pass the tuple as key into the dictionary?
# A. A tuple is indeed a hashable object however it contains a list and therefore you can't use it as a dictionary key.
# for eg.
# D = { (1,2,3): "Uday"} this is allowed but D = { (1,[2,3] ): "Uday"}  not allowed
# ______________________________________________________________________________________________________________________

# Q. Fibonacci series.
#  Next term generated is the sum of preceding two terms.
#  0 1 1 2 3 5 . . . .
# 0+1=1, 1+1=2, 1+2=3, 2+3=5.

# n = 5    # int(input("Enter the numbers of element : "))
# a = 1    # int(input("Enter the first number: "))
# b = 2    # int(input("Enter the Second number: "))
# print(a, b, end=" ")
# while n-2:    # already we have take two number so we eleminates from given numbers of elements.
#     c = a + b
#     a = b
#     b = c
#     print(c, end=" ")
#     n = n-1
# ______________________________________________________________________________________________________________________

# Q. Take the string and reverse it without using inbuilt function.
# a = "Aniruddha Sanjay Gavade"
# b = ""
# # print(len(a))
# for i in range(1, len(a)+1):
#     b += a[-i]
# print(b)
# ______________________________________________________________________________________________________________________

# Q. Take a list and square the numbers by using map function.
# l = [2, 5, 3, 4, 8]
# b = map(lambda x: x*x, l)
# print(list(b))
# ______________________________________________________________________________________________________________________

# # Q.
# a = [3, 4, 5, 6, 7, 8, 9, 1]
# st = a[0]
# l = len(a)
# for i in range(l):
#     if a[i] < st:
#         st = a[i]
#     else:
#         print("Ankur loves butterfly.")
# print("Small: {} ".format(st))
# ______________________________________________________________________________________________________________________

# Q. Recursive Python function to solve tower of hanoi

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods

l = [2, 34,54 ,7 ,8,9]
l.sort()
for i in l:
    print(i)
    break
