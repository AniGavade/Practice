for i in range(7):
    print("My name is Jocker", i)

    for j in range(5):
        if j == 3:
            print("I am variable with value 3")
            break
        print("j=", j)
        for x in range(2):
            print("x=", x)
