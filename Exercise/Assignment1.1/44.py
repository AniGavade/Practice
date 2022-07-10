# Program to accept the strings which contains all vowels

vowels = {"a", "e", "i", "o", "u"}
str = input("Enter a string: ")
s = set()
for i in str:
    if i in vowels:
        s.update(i)
if vowels == s:
    print("Yes")
else:
    print("No")
