# Area of field in Acre.
# 43560 square feet = 1 acre

sqr_ft_per_acres = 43560

a= int(input("Enter the Lenght of the field in feet: "))
b= int(input("Enter the Width of the field in feet: "))
c = a*b / sqr_ft_per_acres

print("The area of field is ", c, "Acre")