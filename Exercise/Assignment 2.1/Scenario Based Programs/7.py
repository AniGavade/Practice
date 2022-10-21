# write a program for character count string "aaabbbccaa" for output:a5b3c2

str_ = "aaabbbccaa"
d = {i: str_.count(i) for i in str_}
lst = [k+str(v) for k, v in d.items()]
print("".join(lst))
# ______________________________________________________________________________________________________________________

# op = {i + str(str_.count(i)) for i in str_}
# print("".join(op))
