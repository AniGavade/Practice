# Python | Finding ‘n’ Character Words in a Text File

count = 1
chrw = ""

file = open('exercise.txt', 'r')
while 1:
    sp = file.read(1)
    if count <= 2:
        chrw = chrw + sp
    if count > 2:
        if sp == " ":
            count = 0
            if len(chrw) > 0:
                print(chrw)
                chrw = ""
        elif sp != " ":
            chrw = ""
    count = count + 1
    if not sp:
        break
file.close()
