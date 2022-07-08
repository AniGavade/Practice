# Write a program to display "Hello" if a number entered by user is a
# multiple of five, otherwise print "Bye".

a = int(input("Enter the number: "))
if a % 5 == 0:
    print("Hello")
else:
    print("Bye")