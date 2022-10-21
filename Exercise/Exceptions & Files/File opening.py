# # writing file.

f = open("abcd.txt", "w")
f.write("Ani\n")
f.write("Ankush\n")
f.write("pankaj\n")
f.write("vinay\n")
f.close()
# =================================================================

#  Reading character data from the files:

# f = open("abcd.txt", "r")
# data = f.read()
# print(type(data))
# f.close()
# ///////////////////////////////////////////////////////////////////////////////

# f = open("abcd.txt", "r")
# data = f.read(10)
# print(data)
# f.close()
# //////////////////////////////////////////////////////////////////////////////////

# f = open("abcd.txt", "r")
# print(f.readline(),end = "")
# print(f.readline(),end = "")
# print(f.readline(),end = "")
# print(f.readline(),end = "")
# f.close()
# //////////////////////////////////////////////////////////////////////////////////////////////

# f = open("abcd.txt", "r")
# list = f.readlines()
# for line in list:
#     print(line, end = "")
# f.close()
# //////////////////////////////////////////////////////////////////////////////////////////////////////

# f = open("junk.txt", "w")
# f.write("some\n")
# f.write("thing\n")
# f.write("happens\n")
# f.write("to\n")
# f.write("you\n")
# f.close()
# ///////////////////////////////////////////////////////////////////////////////////////////

# f = open("junk.txt", "r")
# data = f.read()
# print(data)
# f.close()
# ///////////////////////////////////////////////////////////////////////////////////////////////

# f = open("junk.txt", "r")
# data = f.read(13)
# print(data)
# f.close()
# ///////////////////////////////////////////////////////////////////////////////////////

# file = open("junk.txt", "r")
# print(file.read(16))
# print(file.read(4))
# print(file.read(6))
# print(file.read())
# file.close()
# ///////////////////////////////////////////////////////////////////////////////////////////

# f = open("junk.txt", "r")
# print(f.readline(), end = "")
# print(f.readline(), end = "")
# print(f.readline(), end = "")
# print(f.readline(), end = "")
# print(f.readline(), end = "")
# f.close()
# /////////////////////////////////////////////////////////////////////////////////////////////

# f = open("blank.txt", "w")
# f.write("all ")
# f.write("going ")
# f.write("to ")
# f.write("be ")
# f.write("nice ")
# f.write("in ")
# f.write("coming ")
# f.write("days.")
# f.close()
# ////////////////////////////////////////////////////////////////////////////////////

# f = open("blank.txt", "r")
# data = f.read()
# print(data)
# f.close
# ///////////////////////////////////////////////////////////////////////////////////////////////

# f = open("blank.txt", "r")
# print(f.read(6))
# f.seek(0)
# print(f.read(17))
# f.close()
# /////////////////////////////////////////////////////////////////////////////////////////////////

# file = open("junk.txt", "r")
# file.read()
# print("Re-reading")
# print(file.read())
# print("Finished")
# file.close()
# //////////////////////////////////////////////////////////////////////////////////////////////////

# f = open("welcome.txt", 'w')
# f.write("The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, then it'll return the first value of the loop. Then, each subsequent call will run another iteration of the loop you have written in the function and return the next value. This will continue until the generator is considered empty, which happens when the function runs without hitting yield. That can be because the loop has come to an end, or because you no longer satisfy an if/else")
# f.close()

# f = open("welcome.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# ///////////////////////////////////////////////////////////////////
# msg = "Hello, World!"
# f = open("welcome.txt", "w")
# amount_written = f.write(msg)
# print(amount_written)
# f.close()
#//////////////////////////////////////////////////////////////////////////////////

# #  character occurs in a string of txt file.

# def count_char(text, char):
#     count = 0
#     for c in text:
#         if c == char:
#             count += 1
#     return count

# filename = input("Enter a filename: ")
# with open(filename) as f:
#     text = f.read()

# print(count_char(text, "i"))

# /////////////////////////////////////////////////////////////////////////////////////////////////

# percentage of the text each character of the alphabet occupies.

# def count_char(text, char):
#     count = 0
#     for c in text:
#         if c == char:
#             count += 1
#         return count

# filename = input("Enter a filename: ")
# with open(filename) as f:
#     text = f.read()
#     print(text)
#     ln = len(text)
#     print(ln)

# st = "abcdefghijklmnopqrstuvwxyz"

# for char in st:
#     char_count = text.count(char)
    

#     perc = 100 * char_count / ln
#     print(f"percent of char {char} is {perc}%.")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# f = open("Tuples.py", "w")
# f.write("tuples are immutable. recognise by parenthesis")
# f.close()

# f = open("Tuples.py", "r")
# data = f.read()
# print(data)
# f.close()
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

#  r+

# f = open("welcome.txt", "r+")
# print(f.tell())
# data = f.read()
# print(f.tell())
# f.write("' Python'")
# print(f.tell())
# print(data)
# print(f.tell())
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# a = open("oo.txt", "w")
# a.write("Something is missing in program")
# a.close()

# a = open("oo.txt", "r")
# b = a.read()
# print(b)
# a.close()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

