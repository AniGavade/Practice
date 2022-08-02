#  Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

a = int(input("Enter the number: "))

if a % 2 == 0 and a % 3 == 0:
    print("The number is divisible by both 2 & 3.")
else:
    print("Enter another number")