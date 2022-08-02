# Python Program for Fibonacci numbers.

# Q. Fibonacci series.
#  Next term generated is the sum of preceding two terms.
#  0 1 1 2 3 5 . . . .
# 0+1=1, 1+1=2, 1+2=3, 2+3=5..................

n = int(input("Enter the numbers of element : "))
a = int(input("Enter the first number: "))
b = int(input("Enter the Second number: "))
print(a, b, end=" ")
while n-2:    # already we have take two number, so we eliminate from given numbers of elements.
    c = a + b
    a = b
    b = c
    print(c, end=" ")
    n = n-1

