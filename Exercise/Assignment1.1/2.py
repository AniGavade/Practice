# # Python Program to check Armstrong Number.
# # By using while loop
#
# n = int(input("Enter the number for Armstrong number: "))
# sum = 0
# order = len(str(n))
# copy_num = n
# while n > 0:
#     digit = n % 10
#     sum += digit ** order
#     n = n // 10
# if sum == copy_num:
#     print("This is the Armstrong number")
# else:
#     print("This number isn't armstrong number")
#
#
# # By using for loop in function.
n = int(input("Enter the number: "))
sum = str(n)
order = len(sum)
digit = 0
for i in sum:
    i = int(i)
    a = i ** order
    digit = digit + a

if digit == n:
    print("The number is Armstrong number")
else:
    print("The number isn't Armstrong number, try another number.")
# ________________________________________________________________________________________________________________
