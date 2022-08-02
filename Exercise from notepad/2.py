# Write a program to check whether a number entered by user is even or odd

a = int(input("Enter the number: "))
if a % 2 == 0:
    print("even")
elif a % 2 == 1:
    print("Odd")
else:
    print("Wrong input")