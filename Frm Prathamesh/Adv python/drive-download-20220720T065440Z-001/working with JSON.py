# converting JSON string into python dictionary

import json

# developerJsonString = """{
#     "people" : [
#         {"name": "jane doe",
#         "salary": 9000,
#         "skills": [
#             "Raspberry pi",
#             "Machine Learning",
#             "Web Development"
#         ],
#         "email": "JaneDoe@pynative.com"
#     },
#     {
#         "name": "john mathew",
#         "salary": 8000,
#         "skills": [
#             "Machine Learning",
#             "Web Development"
#         ],
#         "email": "JohnMathew@pynative.com"
#         }
#     ]
# }
# """
#
# print('JSON string :\n', developerJsonString)
# print('converting JSON string to the python dictionary')
#
# pythonDict = json.loads(developerJsonString)
# # print('Python dictionary :\n', pythonDict)
# print(type(pythonDict))
#
# for person in pythonDict['people']:
#     # print(person)
#     # print(person['name'])
#     del person['salary']
#
# # converting python dictionary back to JSON string
#
# new_string = json.dumps(pythonDict, indent=2)
# print(new_string)

# ----------------------------------------------------------------------------------------------------------------------

# converting JSON file into python object (dictionary)

# with open('file.json') as f:
#     data = json.load(f)
#
# for people in data['people']:
#     # print(people['firstName'], people['number'])
#     del people['gender']
#
# # converting python object (dictionary) to JSON file
#
# with open('new_file.json', 'w') as f:
#     json.dump(data, f, indent=2)

# ----------------------------------------------------------------------------------------------------------------------

