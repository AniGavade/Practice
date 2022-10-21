# Name that Shape.

numSides = int(input("How many sides in the shape: "))
geometry = {
    3: "The shape is a triangle.",
    4: "The shape is a quadrilateral",
    5: "The shape is a pentagon",
    6: "The shape is a hexagon",
    7: "The shape is a heptagon",
    8: "The shape is a octagon",
    9: "The shape is a nonagon",
    10: "The shape is a decagon",
    11: "The shape is a hendecagon",
    12: "The shape is a dodecagon",
    13: "The shape is a tridecagon",
    14: "The shape is a tetradecagon",
}
if numSides == 3:
    print(geometry [3])
elif numSides == 4:
    print(geometry [4])
elif numSides == 5:
    print(geometry [5])
elif numSides == 6:
    print(geometry [6])
elif numSides == 7:
    print(geometry [7])
elif numSides == 8:
    print(geometry [8])
elif numSides == 9:
    print(geometry [9])
elif numSides == 10:
    print(geometry [10])
elif numSides == 11:
    print(geometry [11])
elif numSides == 12:
    print(geometry [12])
elif numSides == 13:
    print(geometry [13])
elif numSides == 14:
    print(geometry [14])
else:
    print("Error, sides must be in between 3 and 15. Please try again.")
