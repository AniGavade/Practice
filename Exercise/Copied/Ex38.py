# Month Name to number of days.

name = input("What month is it? ")
thirty_days = ["April", "June", "September", "November"]
thirty_one_days = ["January", "March", "May", "July", "August", "October", "December"]
feb = ["February"]
if name in thirty_days:
    print("number of days: 30")
elif name in thirty_one_days:
    print("number of days: 31")
elif name in feb:
    print("number of days: 28 or 29")