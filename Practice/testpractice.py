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
# x="-".join(s)
# print(x)

# s = "ankur"
# if i in s:
#     print(i, end="-")

a = "nitin"
b = ''
# op > n-i-t-i-n
for i in a:
    b = b + i + "-"
print(b.strip("-"))

# 9822503261

# # find the length of string
# str_="vijaynagar"
# z="ab"
# x=z.join(str_) # here x print vabiabjabaaby
# x1=x.count(z)+1
# #count function return how many time z occured in str. 4 time occured then add 1 i.e 4+1=5
# print(x)
# print(x1)