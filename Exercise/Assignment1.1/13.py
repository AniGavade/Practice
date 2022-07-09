# remove Nth occurrence of the given word

l = ["Ani", "Pankaj", "Ravi", "Shankar", "Mahesh", "Ravi", "Mahesh", "Ani", "Ravi"]
word = "Ravi"
n = 2
count = 0
for i in range(len(l)):
    # print(i)
    if l[i] == word:
        count += 1
    if count == n:
        # print(i)
        l.pop(i)
        break

print("New List: ", l)

# ______________________________________________________________________________________________________________________

# def remove_wrd(lst, wrd, n):
#     count = 0
#
#     for i in range(0, len(lst)):
#         if lst[i] == wrd:
#             count = count + 1
#
#             if count == n:
#                 del(lst[i])
#                 return True
#
#     return False
#
#
# lst = ["Ani", "Pankaj", "Ravi", "Shankar", "Mahesh", "Ravi", "Mahesh", "Ani", "Ravi"]
# print("The list is: ")
# print(lst)
# wrd = "Ravi"
# n = 2
# ele = remove_wrd(lst, wrd, n)
#
# if ele == True:
#     print("The updated list: ", lst)
# else:
#     print("New list: ")
