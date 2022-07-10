# check if a string is palindrome or not Reverse words in a given String in Python.


str_ = input("Enter a string: ")
v = "aeiou"
t = set(str).intersection(v)
if t == set(v):
    print("yes")
else:
    print("no")