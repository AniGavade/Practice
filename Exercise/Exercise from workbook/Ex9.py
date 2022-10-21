interest = 0.04

deposit_amount = int(input("Enter the deposite amount: "))

first_year_savings = (deposit_amount* interest)+deposit_amount
second_year_savings = (first_year_savings* interest)+ first_year_savings
third_year_savings = (second_year_savings* interest)+second_year_savings
print("1st year savings: ", first_year_savings)
print("2nd year savings: ", second_year_savings)
print("3rd year savings: ", third_year_savings)
