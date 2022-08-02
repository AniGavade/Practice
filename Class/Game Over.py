class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")


name = input("Enter the name of player: ")

level = input("Enter the level number: ")

p = Player(name, level)
p.intro()