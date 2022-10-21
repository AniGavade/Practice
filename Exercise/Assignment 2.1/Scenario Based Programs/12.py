# Write a program to convert json file to csv file.

import json
import csv

f = open('data.json')
data = json.load(f)
f.close()

f = open('data.csv')
csv_file = csv.writer(f)
for item in data:
    csv_file.writerow(item)

f.close()

# ______________________________________________________________________________________________________________________

# import json
# print("Program to demonstrate JSON parsing using Python")
# print("\n")
# course ='{"c_name":"Android", "fees": "25000", "c_place":"Chennai"}'
# course_dict = json.loads(course)
# print("JSON data is as follows:")
# print(course_dict)
# print("\n")
# print("Printing particular field in JSON data using data as keys in course dictionary")
# print(course_dict['c_name'])