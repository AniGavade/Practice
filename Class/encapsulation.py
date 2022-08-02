# To enclose something in or as if in a capsule.
#
# class Cat:
#     def __init__(self):
#         self.__sound = "Meow"
#
#     def speak(self):
#         print("Cat says: {}".format(self.__sound))
#
#
# c = Cat()
# c.speak()

# c.sound = "Bhow Bhow"
# c.speak()
# +_____________________________________________________________________________________________________________________

# class Dog:
#     def __init__(self):
#         self.sound = "Bhow"

#
#     def speak(self):
#         print("Dog says: {}".format(self.sound))
#
#
# c = Dog()
# c.speak()
#
# c.sound = "Jevla ka Bhow"
# c.speak()
# ______________________________________________________________________________________________________________________

class Cat:

    def __init__(self):
        self.__sound = "Meow"

    def speak(self):
        print("Cat says: {}".format(self.__sound))


c = Cat()
c.speak()

# change the price
c.sound = "bow-wow"
c.speak()

