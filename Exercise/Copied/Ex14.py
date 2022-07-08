#Convert a height in feet and inches to centimeter.

in_per_feet = 12
cm_per_in = 2.54

#read input from the user
print("Enter your height")
feet = int(input(" Number of Feet:" ))
inches = int(input(" Number of inches:" ))

#Compute the equivalent value of Centimeters.
cm = (feet * in_per_feet + inches) * cm_per_in
print("Your height in centimeters is: ", cm)