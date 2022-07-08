# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = f'{self.first}.{self.last}@gmail.com'

#     def full_name(self):
#         return f'{self.first} {self.last}'


# emp_1 = Employee('John', 'Smith')
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.full_name())
# print('-------------------------------------')

# # but if we change first name then first name will change but email will take old first name
# emp_1.first = 'Tim'
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.full_name())
# print('-------------------------------------')


# t=[(1,2),(3,4),(2,3,4),(1)]

# print("before:"+str(t))
# k=1

# res=[ele for ele in t if len(ele)!=k]

# print("out:"+str(res))

dict = {
    1:"Rohit",
    2:"Prathamesh",
    3:"Uday"
}