#Bottle recycle deposit to encourage people.

LESS_DEPOSITE = 0.10
MORE_DEPOSITE = 0.25

less = int(input("how many containers 1 liter or less do you have? "))
more = int(input("how many containers more than 1 liter do you have? "))

refund = less * LESS_DEPOSITE + MORE_DEPOSITE * more

print("your total refund will be $%.2f."  % refund)