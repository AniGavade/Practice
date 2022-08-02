# class year_graduated:
#     def __int__(self, year=0):
#         self.year = year
#
# # Instantiating the class
#
#
# grade_obj = year_graduated()
# # printing the object
# print(grade_obj)
# # printing the object attribute
# print(grade_obj.year)

class year_graduated:
    def __init__(self, year=0):
        self._year =year

    def get_year(self):
        return self._year

def set_year(self, a):
    self._year = a

