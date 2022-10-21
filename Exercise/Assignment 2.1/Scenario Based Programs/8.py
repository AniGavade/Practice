# Write a decorator for calculating execution time of any python function.

import time
start = time.time()


def decor(fact_):
    def inner(num):
        b = fact_(num)
        print("the execution time is: ", time.time()-start)
        return
    return inner


@decor
def fact(num):
    k = 1
    for i in range(num):
        k += (k*i)
    return k


fact(50000)