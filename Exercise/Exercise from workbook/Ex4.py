# Area of field in Acre.
"""Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres."""
# 43560 square feet = 1 acre

sqr_ft_per_acres = 43560

a = int(input("Enter the Length of the field in feet: "))
b = int(input("Enter the Width of the field in feet: "))
c = a*b / sqr_ft_per_acres

print("The area of field is %.3f" % c, "Acre")
