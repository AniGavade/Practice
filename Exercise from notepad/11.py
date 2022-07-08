#  Accept the age of 4 people and display the oldest one.

l = []

n = 4
for n in range(1, n+1):
    age = int(input("Enter the age of person: "))
    l.append(age)

print("Oldest age is: ", max(l))