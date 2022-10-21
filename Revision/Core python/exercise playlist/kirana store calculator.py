# write a python program which will keep adding a
# stream of numbers inputted by the user. The adding
# stops as soon as user presses q key on the keyboard.

sum_ = 0
while True:
    user_input = input("Enter the item price or press 'q' to quit: \n")
    if user_input != "q":
        sum_ = sum_ + int(user_input)
        # print(f"Order total so far: {sum_}")
    else:
        print(f"Your total bill is {sum_}. Thanks for shopping with us!")
        break
