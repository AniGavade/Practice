# from webbrowser import get
# 

# def get_formatted_name(first_name, last_name, middle_name=" "):
#     """Return a full name, neatly formatted"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name}{last_name}"
#     return full_name.title()

# musician = get_formatted_name("Aniket", "Kadam")
# print(musician)

# musician = get_formatted_name("Aniket", "Kadam", "Suresh")
# print(musician)
#  ______________________________________________________________________________________________________________________

# list=[4,9,16,49,64,48,78,26,58,100,121,284,361,1]
# list1 = []
# def myfun(n):
#     for i in n:
#         j=1
#         while j*j<=i:
#             if j*j == i:
#                 list1.append(i)
#                 break
#             j += 1

# myfun(list)

# print(list1)
# ___________________________________________________________________________________________________________________________________

# num = []
# # for i in range num(100, 1000)
# n = num
# l = 0
# while n != 0:
#     l = (l * 10) + (n)
#     n = n // 10

# if num == l:
#     print("The number is palindrom")
# else:
#     print("The number is not palindrom")
# ____________________________________________________________________________________________________________

# Reverse the Number.

# n = int(input("enter the number: "))
# l = 0
# while(n > 0):
#     a = n % 10
#     l = l *10 + a
#     n = n // 10
# print(l)

# n=int(input("enter the number:"))
# print(str(n)[: :-1])
# ___________________________________________________________________________________________________________________

# list=[]
# for i in range(100,1000):
#     if i%11==1:
#         list.append(i)
    
# print(list)

Str = "Latracal Solutionss"
l = len(Str)
 
Remove_last = Str[:l-1]
 
print("String : ",Remove_last)