# Accessing private variable using public method

class Employee:
    def __init__(self, name, salary):
        self.name = name         # public variable
        self.__salary = salary   # protected variable

    def showDetails(self):
        return {f'Name : {self.name}, Salary : {self.__salary}'}


emp = Employee("Ross", 50000)
details = emp.showDetails()
print(details)

# Accessing private variable using name mangling


class Employee1:
    def __init__(self, name, salary):
        self.name = name         # public variable
        self.__salary = salary   # protected variable


emp = Employee1("Ross", 50000)
print(f'Name : {emp.name}')
# direct access to private variable using name mangling
print(f'Salary : {emp._Employee1__salary}')   # classInstance._classname__datamember


# Accessing protected variable using public method
# class Company:
#     def __init__(self):
#         self._c_name = "ABC"
#
#
# class Emp(Company):
#     def __init__(self, e_name):
#         self.e_name = e_name
#         Company.__init__(self)
#
#     def showDetails(self):
#         return f'Employee {self.e_name} working in {self._c_name} company'
#
#
# emp = Emp("John")
# details = emp.showDetails()
# print(details)

# ----------------------------------------------------------------------------------------------------------------------

# modifying data members using getter and setter

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         # private variable
#         self.__marks = marks
#
#     # public instance method
#     def showDetails(self):
#         return f'Name : {self.name}, Marks : {self.__marks}'
#
#     # getter method
#     def getMarks(self):
#         return self.__marks
#
#     # setter method
#     def setMarks(self, marks):
#         if marks < 0 or marks > 100:
#             print('Invalid input. Please set correct marks..')
#         else:
#             self.__marks = marks
#
#
# stud = Student("John", 70)
# details = stud.showDetails()
# print(details)
# stud.setMarks(120)
# print(f'marks = {stud.getMarks()}')
# stud.setMarks(80)
# details = stud.showDetails()
# print(details)

