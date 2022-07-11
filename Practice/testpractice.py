# lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# x=int(input("enter the number which you want to serach:"))

# count=0
# for i in lst:
#     if (i==x):
#         count=count+1
#         print("number of occurences of x is ",count)
#     # if (i not in lst): 
#     else:
#         print("type num which is in list")

# # _______________________________________________________________________________
# # Sort the values of first list using second list. 

# l = ["f", "l", "y", "r", "s", "j", "b", "c", "a"]
# m = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
# # def sort_list(l1, l2):
#     list_zip = zip(l2, l1)
#     output1 = [x for _, x in sorted(list_zip)]
#     return output1

# print("The values of first list using second list")
# print(sort_list(l1, l2))


# l = ['a', 'c', 'e', 'e', 'm', 'q', 'y']
# m = [1, 8, 6, 2, 9, 2, 6]

# lst = zip(l, m)
# final = list(lst)
# print(final)

# sorted_list = sorted(final, key=lambda x: (x[0], x[1]))
# print(sorted_list)
# # # _____________________________________________________________________________

# # a = "'Python' is programming language for Normal peoples, and 'Pyhon' is a language for Legends."
# # print(a)
# # _____________________________________________________________________________________________________________

# l1 = ["f", "l", "y", "r", "s", "j", "b", "c", "a"]
# l2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
# key1=dict(zip(l1,l2))
# print(key1)
# l1.sort(key=key1.get)
# print(l1)
# ______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# # We are creating our own social network application and need to have a hashtag generator program.
# Complete the program to output the input text starting with the hashtag (#).
# Also, if the user entered several words, the program should delete the spaces between them.

# s = input("Enter the name for hashtag: ")

# def hash(text):
# 	s1 = s.replace(" ", "")
# 	return "#" + s1

# print(hash(s))
# ______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# You are given a program with two inputs: one as password and the second one as password repeat. Complete and call the given function to output "Correct" if password and repeat are equal, and output "Wrong", if they are not.

# password = input("Enter the password: ")
# repeat = input("repeat the password: ")

# def validate(text1, text2):
# 	if text1 == text2:
# 		print("Correct")
# 	else:
# 		print("Wrong")

# validate(password, repeat)
# ________________________________________________________________________________________________________________________________________________

# num = int(input("enter the number:"))

# factorial = 1

# for i in range (1,(num+1)):
#     factorial = factorial * i
    
# print(f"Factorial of {num} = {factorial}")

# _________________________________________________________________________________________________________________________________

#
# s = "aniruddha"
# x = "-".join(s)
# print(x)

# s = "ankur"
# if i in s:
#     print(i, end="-")

# a = "nitin"
# b = ''
# # op > n-i-t-i-n
# for i in a:
#     b = b + i + "-"
# print(b.strip("-"))

# 9822503261

# # find the length of string
# str_="vijaynagar"
# z="ab"
# x=z.join(str_) # here x print vabiabjabaaby
# x1=x.count(z)+1
# #count function return how many time z occured in str. 4 time occured then add 1 i.e 4+1=5
# print(x)
# print(x1)


#
# s = "Djka1sjsjs2anns4ksmsm3"
# a = ""
# for i in s:
#     if i.isnumeric() + i.isalpha():
#         a += i
#         b = list(a)
#         b.sort()
# print(b)



# list1 = [11, 22, 33, 44]
# enumerate_list = enumerate (list1)
# print ("Enumerated list now looks like:", list (enumerate_list)) #print the index and corresponding value for enumerated list1 for i, item in enumerate (list1): print ("Index = ", i,": "," value = ", item)

#
# d = {}
# num_students = int(input("enter the no of student: "))
# for i in range(num_students):
#     name = input("Enter the name of student: ")
#     y = eval(input("enter the list of marks of student: "))
#     marks = sum(list(y))/len(y)
#     d[name] = marks
# print(d)
# # while True:
#     name = input("enter the name of student: ")
#     marks = d.get(name,-1)
#     if marks >= 80:
#         print(name,"has A Grade")
#     elif marks >= 60:
#         print(name,"has B Grade")
#     elif marks >= 40:
#         print(name,"has C Grade")
#     elif marks == -1:
#         print("student not found")
#     option = input("do u want to check another student marks:[yes/no] ")
#     if option == "no":
#         break
# print("thank u")

# for i in range(23, 24):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")
# a = 25
# l = [x*a for x in range(1, 11)]
# print(l)

# a = [f"{x} is even" if x%2 == 0 else f"{x} is odd" for x in range(10)]
# print(a)

# s = {7, 3, 9, 4, 8, 2}
# s.add(5)
# print(s)

# 1st method - Using list
# d = {"A": 1, "B": 2, "C": 3}
# k = list(d.keys())
# print(k)

# d = {"A": 1, "B": 2, "C": 3}
# k = list(d)
# print(k)

# 2nd method- Using iterable unpacking operator.
# d = {"A": 1, "B": 2, "C": 3}
# x = [*d.keys()]
# print(x)

# d = {"A": 1, "B": 2, "C": 3}
# x = [*d]
# print(x)

# 3rd method- Using keys() Function.
# d = {"A": 1, "B": 2, "C": 3}
# x = d.keys()
# print([k for k in x])

# 4th method
# d = {"A": 1, "B": 2, "C": 3}
# *x, = d
# print(x)