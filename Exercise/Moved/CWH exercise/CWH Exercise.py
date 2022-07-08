# from playsound import playsound
# playsound("C:\\Users\\HP\\Music\\Pasori Coke Studio Song Download Season 14.mp3")
# ___________________________________________________________________________________________________________________________________________

def soted(l):
    return (sorted(l, key=lambda x: x[1]))


l = [("Pushp", 100), ("Ani", 50), ("Prath", 15), ("Uds", 20)]

print(soted(l))
# ___________________________________________________________________________________________________________________________________________

l = [("Pushp", 10), ("Ani", 5), ("Prath", 15), ("Uds", 20)]
s = [15, 10, 5, 20]
a = [i for j in s for i in filter(lambda x: x[1] == j, l)]
print("The sorted list is: ", a)
# __________________________________________________________________________________________________________________________________________

# test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
#
# # printing original list
# print("The original list is : ", test_list)
#
# # performing sort, lambda function provides logic
# res = sorted(test_list, key=lambda tup: sum([len(str(ele)) for ele in tup]))
# # sorted(t,key=lambda x: )
# # printing result
# print("Sorted tuples : ", res)
# ___________________________________________________________________________________________________________________________________________
# # code to demonstrate working of
# # Elements frequency in Tuple
# # Using Counter()
# ____________________________________________________________________________________________________________________________________________________

# from collections import Counter
#
# test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
#
# print("before",test_tup)
#
# sup=Counter(test_tup)
# print("after :",sup)
# ________________________________________________________________________________________________________________________________________________


import random


# Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose r
    elif comp == 'r':
        if you == 'p':
            return False
        elif you == 's':
            return True

    # Check for all possibilities when computer chose p
    elif comp == 'p':
        if you == 's':
            return False
        elif you == 'r':
            return True

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you == 'r':
            return False
        elif you == 'p':
            return True


print("Comp Turn: Rock(r) paper(p) or Scissors(s)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Rock(r) Paper(p) or Scissors(s)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
