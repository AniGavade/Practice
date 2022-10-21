# Python program to read file word by word

with open("exercise.txt", "r") as f:
    # for i in f:
    #     for word in i.split():
    #         print(word)

    l1 = f.readline()
    f.seek(1, 0)
    l2 = f.readline()
    f.seek(-12, 1)
print(l1)
print(l2)