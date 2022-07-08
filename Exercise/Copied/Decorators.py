def decor(func):
    def wrap():
        print("abcdefghi")
        func()
        print("stuvwxyz")
    return wrap

def print_text():
    print("jklmnopqr")

decorated = decor(print_text)
decorated()