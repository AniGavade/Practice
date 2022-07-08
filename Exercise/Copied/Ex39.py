# Sound Level.

decibels = int(input("Describe the decibles: "))
if decibels <= 130 and decibels >= 106:
    print("Sonud level is Jackmer")
elif decibels <= 106 and decibels >= 70:
    print("Sonud level is Gas lawnmover")
elif decibels <= 70 and decibels >= 40:
    print("Sonud level is Alarm Clock")
elif decibels <= 40:
    print("Sonud level is Quite room")
else:
    print("Sound level is loudest in the table")