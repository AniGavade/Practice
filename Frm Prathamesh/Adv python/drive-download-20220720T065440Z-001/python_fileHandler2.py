import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

file_handler = logging.FileHandler('Employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logging.basicConfig(filename='Employee.log',
#                     level=logging.INFO,
#                     format='%(name)s : %(levelname)s : %(message)s')


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info(f'Employee created : {self.first}.{self.last}{len(self.first)}@gmail.com')


emp1 = Employee('Prathamesh', 'Sawant')
emp2 = Employee('Rohit', 'Patil')
emp3 = Employee('Aniruddha', 'Gavade')
