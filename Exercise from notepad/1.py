# Write a program to check whether a person is eligible for
# voting or not. (Accept age from user)

age = int(input("Enter the age: "))
if age >= 18:
    print("A person is eligible for voting")
elif age < 18:
    print("A person is under age for voting.")
else:
    print("Enter a number")