alphabets = "abcdefgh"
block = input("Enter the position of block: ")
column = int(alphabets.index(block[0]))+1
row = int(block[1:])
if row < 9:
    position = column + row
    if position % 2 == 0:
        print("The block is \"black\"")
    else:
        print("The block is \"white\"")
else:
    print("invalid input")
