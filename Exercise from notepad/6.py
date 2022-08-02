# Write a program to accept a number from 1 to 7 and
# display the name of the day like 1 for Sunday, 2 for Monday and so on.

# weekday = int(input("Enter the number: "))
# if weekday == 1:
#     print("Sunday")
# elif weekday == 2:
#     print("Monday")
# elif weekday == 3:
#     print("Tuesday")
# elif weekday == 4:
#     print("wednesday")
# elif weekday == 5:
#     print("Thirsday")
# elif weekday == 6:
#     print("Friday")
# elif weekday == 7:
#     print("Saturelday")
# else:
#     print("Invalid Input  ")
#
# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = f'{self.first}.{self.last}@gmail.com'
#
#     def full_name(self):
#         return f'{self.first} {self.last}'
#
#
# emp_1 = Employee("Uday", "shetty")
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.full_name())
# print('-------------------------------------')
#
# # but if we change first name then first name will change but email will take old first name
# emp_1.first = 'Tim'
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.full_name())
# print('-------------------------------------')
#
# t = [(1, 2), (3, 4), (2, 3, 4), (1,)]
#
# print("before:", t)
# print(type(t))
# k = 1
#
# res = [ele for ele in t if len(ele) != k]
#
# print("out:", res)
#
# test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None,)]
#
# print("before", test_list)
# k = None
# res = [ele for ele in test_list if k not in ele]
#
# print("out", res)
#___________________________________________________________________________________________________________________________

a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
a += b
print(a)