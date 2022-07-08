# Write a program to check whether a number (accepted from user) is positive or negative

a = int(input("Enter a number: "))

if a < 0:
    print("Negative Number")
elif a > 0:
    print("Positive number")
elif a == 0:
    print("Zero")
else:
    print("Invalid input")