# Python Program to obtain the line number in which given word is present

with open('exercise.txt', 'r') as f:
    lines = f.read().split("\n")


print("Number of lines is {}".format(len(lines)))

word = 'been'
for i, line in enumerate(lines):
    if word in line:
        print("Word \"{}\" found in line {}".format(word, i+1))
