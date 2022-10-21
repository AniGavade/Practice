# create decorator for function which prints its arguments. decorator should check if
# argument divided by 2. if it is then only run the function.

def decor(func_):
    def inner(num):
        b = func_(num)
        if b % 2 == 0:
            print(func_(num))
        else:
            pass
    return inner


@decor
def func(num):
    return num


func(3)
func(5)
func(2)
func(10)
