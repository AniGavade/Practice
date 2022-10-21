# Before performing any operation on the file like reading or writing, first, we have to open that file.
# f = open(filename, mode)     # Where the following mode is supported:

# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.

# ------------------------------------------------------------------------------------------------------------------------
# Creating a file using write() mode
# ------------------------------------------------------------------------------------------------------------------------

# file = open('file.txt', 'w')
# file.write('hello brain-works!\n')
# file.write('good morning')
# file.close()

# file = open('file.txt', 'w')
# file.write('this is line one\n')   # override all the existing data with new data.
# file.close()
# file = open('file.txt', 'r')
# print(file.read())

# open an existing file for a write operation. If the file already contains some data then it will be overridden.
# here, old data is overridden by new data.
# file = open('file.txt', 'w')
# file.write('this is line one\n')
# file.write('this is line two\n')
# file.write('this is line three\n')
# file.write('this is line four\n')
# file.write('this is line five\n')
# file.write('this is line six\n')
# file.write('this is line seven\n')
# file.write('this is line eight\n')
# file.write('this is line nine\n')
# file.write('this is line ten\n')
# file.close()

# file = open('file.txt', 'r')
# print(file.read())
# file.close()

# we can also open file using 'with' keyword. advantage we get using this method is we need not worry about closing the
# resources. file we get closed automatically

# with open('file.txt', 'w') as file:
#     file.write('this is line one\n')
#     file.write('this is line two\n')
#     file.write('this is line three\n')
#     file.write('this is line four\n')
#     file.write('this is line five\n')
#     file.write('this is line six\n')
#     file.write('this is line seven\n')
#     file.write('this is line eight\n')
#     file.write('this is line nine\n')
#     file.write('this is line ten\n')


# # in 'write' mode we cannot perform read operation. so, to perform read operation also, we use 'write and read' mode.
# file1 = open('file1.txt', 'w')
# file1.write('this is line one\n')
# line = file1.read()  # this will give us an error as write operation does not support read operation. so to overcome
# on it, we use read and write mode
# print(line)
# file1.close()

with open('file1.txt', 'w+') as file1:
    file1.write('this is line one\n')
    file1.write('this is line two\n')
    file1.write('this is line three\n')  # here file pointer is at the end
    file1.seek(0)                        # move the pointer at the beginning
    line = file1.read()                  # now we can read the file from the beginning
    print(line)


# ------------------------------------------------------------------------------------------------------------------------
# read operation :
# ------------------------------------------------------------------------------------------------------------------------

# with open('file.txt', 'r') as file:
# print('--- reading all lines inside txt file using for loop ---')
# for line in file:
#     print(line, end='')
# # The open command will open the file in the read mode and the for loop will print each line present in the file.
#
#
# file = open('file.txt', 'r')
# print('--- reading all lines inside txt file ---')
# print(file.read(), end="")
# file.close()
#
#
# with open('file.txt', 'r') as file:
#     print('--- reading specific numbers of characters from text file ---')
#     f = file.read(52)     # used to read specific numbers of characters.
#     print(f)
#     print()
#
#
# file = open('file.txt', 'r')
# print('--- reading text file using readline() and readlines() command ---')
# f = file.readline()  # it will read single line from the text file.
#
# f1 = file.readline()  # it will read next single line from the text file.
#
# f2 = file.readlines(30)  # The readlines() method returns a list containing each line in the file as a list item.
# # Use the hint parameter to limit the number of lines returned. If the total number of bytes returned exceeds the
# # specified number, no more lines are returned.
#
# f3 = file.readlines()  # if we have already used multiple readline() commands before using readlines() command then,
# # it will read remaining lines from text file.
#
# f4 = file.readlines()  # it will print empty string. because all lines present inside text file are read by above
# # readlines command so there is nothing left to read for this readlines command.
# # IT WORKS SIMILAR TO YIELD KEYWORD.
#
# print(f, end="")
# print(f1, end="")
# print(f2)
# print(f2)
# print(f3)
# print(f4)
# print()
# file.close()

# we cannot perform write operation in 'r' mode. to perform write as well as read operation we need to use 'r+'
# with open('file.txt', 'r+') as file:
#     print('--- performing write() operation using \'r+\' mode ---')
#     file.write('good ')
#     # In r+ mode, we can read and write the file, but the file pointer position is at the beginning of the file;
#     # if we write the file directly, it will overwrite the beginning content.
#     file.seek(0)   # we are taking pointer to beginning to read whole text file
#     print(file.read())

# to overcome this problem we use f.read() to move the file pointer to the end of the file, and append a new line.
# with open('file.txt', 'r+') as file:
#     print('--- use read() method to move pointer at the end position and then append new data ---')
#     file.read()
#     file.write('good ')
#     # In r+ mode, we can read and write the file, but initially file pointer position is at the beginning of the file;
#     # if we write the file directly, it will overwrite the beginning content.
#     file.seek(0)   # we are taking pointer to beginning to read whole text file
#     print(file.read())

# ------------------------------------------------------------------------------------------------------------------------
# append operation :
# ------------------------------------------------------------------------------------------------------------------------

# In order to append a new line to the existing file, open the file in append mode, by using either 'a' or 'a+' as
# the access mode.

# Append Only (‘a’): Open the file for writing. The file is created if it does not exist. The handle is positioned at
# the end of the file. The data being written will be inserted at the end, after the existing data.
# Append and Read (‘a+’): Open the file for reading and writing. The file is created if it does not exist. The handle
# is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

# file = open('file.txt', 'a')  # here we are appending new data at the end of the file.
# file.write("This is team-brainworks institute\n")
# # file.readlines()  # we cannot use readlines() method here. since we open file in append mode only. If we want to read
# # file as well, then we need to open the file in 'append and read' mode.
# file.close()
#
# file = open('file.txt', 'a+')  # here we opened the existing file in 'append and read' mode. so that we can perform read
# # as well as write operation on the existing file.
# file.write('Good morning team-brainworks\n')
# file.seek(0)  # here we take cursor to beginning of the file and then start to read data.
# line = file.read()
# print(line)
# file.close()

# ------------------------------------------------------------------------------------------------------------------------

# with open('file.txt', 'r') as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print(word)
#     print()

# ------------------------------------------------------------------------------------------------------------------------
# seek() and tell() methods :
# ------------------------------------------------------------------------------------------------------------------------
# seek() method
# seek() function is used to change the position of the File Handle to a given specific position. File handle is like
# a cursor, which defines from where the data has to be read or written in the file.

# with open('file.txt','w+') as file1:
#     file1.write('code is like humor. when you have to explain it, it\'s bad.')
#     file1.seek(20)   # moving file handle to 20th position
#     file1.tell()     # tell() method used to print current position of the file handle.
#     result = file1.read()
#     print(result)

# ------------------------------------------------------------------------------------------------------------------------

# read and write file using absolute path

# with open(r'C:\Users\91940\Desktop\lectures\interview questions.txt', 'a+') as file:
#     file.seek(0)
#     data = file.read()
#     print(data)
#
#     file.write('done with walrus operator')
#     file.seek(0)
#     data = file.read()
#     print(data)

# ------------------------------------------------------------------------------------------------------------------------

# person_data = ['Name: Emma', '\nAddress: 221 Baker Street', '\nCity: London']
# # writing string and list of lines to a file
# with open("write_demo.txt", "w+") as fp:
#     fp.writelines(person_data)
#     fp.seek(0)
#     data = fp.read()
#     print(data)

# ------------------------------------------------------------------------------------------------------------------------
# renaming the file
# ------------------------------------------------------------------------------------------------------------------------

# import os
#
# if os.path.isfile(r'C:\Users\91940\Desktop\lectures\interview questions.txt'):
#     os.rename(r'C:\Users\91940\Desktop\lectures\interview questions.txt', r'C:\Users\91940\Desktop\lectures\questions.txt')
#     print('file name changed successfully')
# else:
#     print('file is not present in your local system')
#     print()
#
#
# # with open(r'C:\Users\91940\Desktop\lectures\interview questions.txt', 'r') as file:
# #     # this will raise FileNotFoundError
# #     print(file.read())
#
# with open(r'C:\Users\91940\Desktop\lectures\questions.txt', 'r') as file:
#     print(file.read())

# ------------------------------------------------------------------------------------------------------------------------

# renaming the extension of the files

# import os
# folder = r'C:\Users\91940\Desktop\lectures\New folder\\'
# files = os.listdir(folder)
# print(files)
#
# for file in files:
#     old_name = os.path.join(folder, file)
#     new_name = old_name.replace('.txt', '.pdf')
#     os.rename(old_name, new_name)
#
# files = os.listdir(folder)
# print(files)

# ------------------------------------------------------------------------------------------------------------------------
# removing the file
# ------------------------------------------------------------------------------------------------------------------------

# import os
#
# print(os.listdir(r'C:\Users\91940\Desktop\lectures\New folder\\'))
# file_path = r'C:\Users\91940\Desktop\lectures\New folder\New Text Document (4).pdf'
# if os.path.exists(file_path):
#     os.remove(file_path)
# else:
#     print("The system cannot find the file specified")

# ------------------------------------------------------------------------------------------------------------------------
# copy the file
# ------------------------------------------------------------------------------------------------------------------------

# import shutil
# import os
#
# source_path = r'C:\Users\91940\Desktop\lectures\New folder\New Text Document.pdf'
# destination_path = r'C:\Users\91940\Desktop\lectures\New folder 2\New Text Document.pdf'
#
# shutil.copy(source_path, destination_path)
# copied_file = os.listdir(r'C:\Users\91940\Desktop\lectures\New folder 2')
# print(copied_file)
# ------------------------------------------------------------------------------------------------------------------------

# copy multiple files from folders
# source = r'C:\Users\91940\Desktop\lectures\New folder'
# destination = r'C:\Users\91940\Desktop\lectures\New folder 2'
#
# folder = os.listdir(source)
# print('files present in source folder\n', folder)
#
# for file in folder:
#     source_folder = os.path.join(source, file)
#     destination_folder = os.path.join(destination, file)
#
#     if os.path.isfile(source_folder):
#         shutil.copy(source_folder, destination_folder)
#     else:
#         print('No such file or directory')
#
# copied_files = os.listdir(destination)
# print('files in destination folder after copying it\n', copied_files)
# ------------------------------------------------------------------------------------------------------------------------

# copy entire directory

# source = r'C:\Users\91940\Desktop\lectures\New folder'
# destination = r'C:\Users\91940\Desktop\lectures\New folder (2)'
#
# shutil.copytree(source, destination)
# folder = os.listdir(destination)
# print(folder)

