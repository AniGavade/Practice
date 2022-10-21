# Python Program to Eliminate repeated lines from a file

outputFile = open('welcome.txt', "w")
inputFile = open('exercise.txt', "r")
lines_seen_so_far = set()
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)
print(lines_seen_so_far)

inputFile.close()
outputFile.close()
