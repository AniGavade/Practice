# Write a program to accept percentage from the user and
# display the grade according to the following criteria:
#               Marks                                    Grade
#                > 90                                       A
#                > 80 and <= 90                             B
#                >= 60 and <= 80                            C
#                below 60                                   D

marks = int(input("Enter the marks : "))
if marks > 90:
    print("Grade 'A'")
elif marks > 80 and marks<= 90:
    print("grade 'B'")
elif marks >=60 and marks <=80:
    print("Grade 'C'")
elif marks < 60:
    print("Grade 'D'")
