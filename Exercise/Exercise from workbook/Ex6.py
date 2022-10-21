tax_rate = 0.075
tip_rate = 0.18

menu_rate = float(input("Enter the rate of selected menu $"))

tax = menu_rate * tax_rate
tip = menu_rate * tip_rate

final_bill = menu_rate + tip + tax

print("The tax is %.2f and the tip is %.2f, Your final_bill %.2f", (tax, tip, final_bill))
