# Count number of lines in a text file in Python.

with open('exercise.txt', 'r') as f:
    lines = f.read().split("\n")


print("The number of lines is: ", len(lines))
