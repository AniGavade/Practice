#Bottle recycle deposit to encourage people.
"""In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places."""

less_than1_deposit = 0.10
max_than1_deposit = 0.25

less_ = int(input("Enter the number of bottles capacity of less than 1 ltr: "))
max_ = int(input("Enter the number of bottles capacity of more than 1 ltr: "))

total_cost = less_ * less_than1_deposit + max_than1_deposit * max_
print("Your total refundable amount is %.2f" % total_cost)

