# Find number of times every day occurs in a Year

def num_of_occurrence(n, first_day):
    my_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    my_count = [4 for i in range(0, 7)]
    my_position = -1
    for i in range(0, 7):
        if first_day == my_days[i]:
            my_position = i
            break
    inc = n - 28
    for i in range(my_position, my_position + inc):
        if i > 6:
            my_count[i % 7] = 5
        else:
            my_count[i] = 5
    for i in range(0, 7):
        print(my_days[i], " ", my_count[i])


num = 31
first_day = "Thursday"
num_of_occurrence(num, first_day)
