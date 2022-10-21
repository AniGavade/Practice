# Write a python program for string that will print out char with char count.
# E.g. words = 'aaaabahhhhhaaa' Output should be a4b1a1h5

str_ = 'aaaabahhhhhaaa'                   # str_
char = str_[0]                            # chr_
cnt = 0                                   # count_
op = ""                                   # op
for ch in str_:                           # i
    if ch == char:
        cnt += 1
    else:
        op += (char+str(cnt))
        cnt = 1
        char = ch
op += (char+str(cnt))
print(op)


