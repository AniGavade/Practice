def print_text():
    print("Everything is fair in love and war")

print_text = decor(print_text)

@decor
def print_text():
    print("Ok, then what i do?")