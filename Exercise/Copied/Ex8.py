#weights are in grms.
widget_weight = 75
gizmos_weight = 112
widget = int(input("Enter the numbers of weights: "))
gizmos = int(input("Enter the numbers of gizmos: "))

total_weight = widget*widget_weight + gizmos*gizmos_weight
print("The Total weight is: ", total_weight)