# Python Program for factorial of a number with and without recursion

# With recursion.

def fact(n):
    if n == 1:
        return n
    
    return n * fact(n-1)


num = int(input("User input: "))
print("The factorial", num, "is", fact(num))

# _____________________________________________________________________________________________________________________

# Without recursion.

n = int(input("Enter the number: "))
fact = 1
while n > 0:
    fact = fact*n
    n = n-1


print("The factorial is", fact)

# ____________________________________________________________________________________________________________________

f = int(input("enter the number to see factorial:"))
fact = 1
for i in range(1, (f+1)):
    fact = fact * i

    
print(f"Factorial of {f} = {fact}")