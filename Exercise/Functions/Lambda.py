from functools import reduce            # reduce() function is used for

# l = [81, 52, 35, 62, 21, 68, 23]
#
# x = reduce(lambda a, b: a if a > b else b, l)
# y = reduce(lambda a, b: a if a > b and a < reduce(lambda a, b: a if a > b else b, l) else b, l)
# print(y)
# print(x)

# abc=[10,20,30,[40,50]]
# n=len(abc)
# for i in range(abc):
#     if type(list[i]) is list:
#         if len(abc[i])>1:
#             m=len(abc[i])
#             for j in range(m):
#                 print(i,"=",j,"=",abc[i][j])
#     else:
#         print(i,"=",list[i])

# def sc(tt):
#     return[j for i in reversed(tt)]
    

# tt=[5,6,7,8,9]

# print(sc(tt))

# l1=[1,2,3,4]
# l2=[2,3,4,5]
# x=list(map(lambda x,y:x+y,l1,l2))
# print(x)

# l1=[1,2,3,4]
# l2=[2,3,4,5]
# l3=[]
# for i in zip(l1,l2):
#     l3.append(sum(list(i)))
# print(l3)


# s = '+919561489883 9422819890 +918605031487 8474525885'

# s1 = s.split(' ')
# l1 = [ ]
# for i in s1:
#     if '+91' in i:
#         l1.append(i)
# print(l1)

# s2 = s.split(" ")
# l2 = []
# for j in s2:
#     if "+91" not in j:
#         l2.append(j)
# print(l2)
# _____________________________________________________________________________________________________________________________________________________________

# # Given a list of names, output a list that contains only the names that consist of more than 5 characters.

# names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]
# result = list(map(lambda x: len(x) > 5, names))
# print(result)

# fruits = ["apples", "oranges", "bananas", "melons"]
# prices = [20, 30, 40, 35]
# quantities = [5, 6, 8, 4]

# for fruit, price, quantity in zip(fruits, prices, quantities):
#     print(f"You bought {quantity} {fruit} for ${price*quantity}")

# l = [10, 20, 30, [40, 50]]

# for i, j in zip(range(len(l)), l):
#     if type(j) == int:
#         print(i, " ", j)
#     if type(j) == list:
#         for k in range(len(j)):
#             print(i, k, j[k])

# alien = {"color" : "red", "bird" : "parrot"}
# print(alien["color"])
# print(alien["bird"])

# _______________________________________________________________________________________________
# Lambda (anonymous function.)
# def square(a):
#     return a*a

# l = lambda a, b: a*b
# result = l(3, 4)
# print(result)
# ______________________________________________________________________________________________________________________

# from functools import reduce
# lst = [1, 2, 3, 45]
# result = reduce((lambda x, y: x + y), lst)
# print(result)
# ______________________________________________________________________________________________________________________

# f = lambda x: bool(x % 2)
# print(f(20), f(21))
 