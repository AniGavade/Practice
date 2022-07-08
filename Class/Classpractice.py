# class Student:
#     """This is the student class dveloped by me"""

# # print(Student.__doc__)
# help(Student)
# ______________________________________________________________________________________________

# class Student(object):
#     """Developed by Me."""
#     def __init__(self):
#         self.name = "Aniruddha"
#         self.marks = 86
#         self.age = 27
    

#     def talk(self):
#         print("My name is: ", self.name)
#         print("My age is: ", self.age)
#         print("My marks: ", self.marks)


#     # def seek(self):
#         # self.marks = 99
    

# s1 = Student()
# s1.marks = 99
# # s2 = Student()
# s1.talk()

# # print(type(s1))
# ________________________________________________________________________________________________________________

# class Student:

#     def __init__(self, name, rollno, marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks

#     def talk(self):
#         print("Hey my name is: ",self.name)
#         print("My rollno is: ",self.rollno)
#         print("My marks are: ",self.marks)

# s2 = Student("Aniruddha", 67, 93)
# s2.talk()
# _______________________________________________________________________________________________________________

# class Ceremony:

#     def __init__(self):
#         self.Venue = ("Marriage")
#         self.date = "28-05-2022"
#         self.Location = "Hayat Hotel"

#     def asset(self):
#         print("The occasion is: ", self.Venue)
#         print("On the date: ", self.date)
#         print("location of: ", self.Location)

# c1 = Ceremony()
# c1.asset()
# __________________________________________________________________________________________________________________

# class College:

#     def __init__(self, Principle, Classrooms, Playground):
#         self.Principle = Principle
#         self.Classrooms = Classrooms
#         self.Playground = Playground

#     def teacher(self):
#         print("College's main authorised persons is ",self.Principle)
#         print("total Classrooms are: ",self.Classrooms)
#         print("Tournament orgnise on Playground of ",self.Playground)

# p1 = College("Principle", 69, "Cricket")
# p1.teacher()
# _____________________________________________________________________________________________________________________________________________________________________

# # Self variable:
#  self is the default variable which is pointing to current object)like this keyword in java.
# By using self we can access instance variables and instance method of object.
# ___________________________________________________________________________________________________________________________________________________

class Dog:

    attr1 = "mammal"

    def __init__(self, name):
        self.name = name
        print('brainworks')
    print('python')

    def method1(self):
        print('pyhon')


Moti = Dog("Moti")
Tommy = Dog("Tommy")


print("Moti is a {}".format(Moti.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# # print("My dog name is {}".format(Moti.name))
# # print("My dog name is {}".format(Tommy.name))
# class g_s(Dog):
#     def __init__(self):
#         super().method1()
#         print('Husky')
    
        
# inst=g_s()
# # ________________________________________________________________________________________________________________________________________________________________

# # Inheritance in python.

# for i in range(100,1000):
#     if str(i)==(str(i))[::-1]:
#         print(i)
# 
# a = "yaranachalega"
# l = len(a)
# b = a[:l-1]
# print(b)

# str = "yaranachalega"
# str = ((str[::-1]).replace("a", "", 1))[::-1]
# print(str)
# _________________________________________________________________________________________________________________

# for i in range(100, 1000):
#     if str(i) == (str(i))[::-1]:
#         print(i)
# ___________________________________________________________________________________

# a = []
# for i in range(10):
#     a.append(i*++i)
# for a[i] in a:
#     print(a[i])
# _________________________________________

# a = 50
 
# def show():
#    x=10

# show()
# print(x)
# print(a)

# a = [1,2,3,4,5,6]
# for i in a:
#     print(i)

# ____________________________________________________________________________________________________________

