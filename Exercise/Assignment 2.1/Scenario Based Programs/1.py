# Python Program for Linear Search

def search(lst_, n):
    i = 0

    while i < len(lst_):
        if lst_[i] == n:
            return True
        i += 1

    return False


lst_ = [2, 4, 6, 9, 4, 1]
n = 4

if search(lst_, n):
    print("Found the number {}".format(n))
else:
    print("NOt Found the number {}".format(n))

