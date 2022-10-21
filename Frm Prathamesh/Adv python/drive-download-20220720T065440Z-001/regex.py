import re

# ----------------------------------------------------------------------------------------------------------------------
# re.compile() method and findall() method
# ----------------------------------------------------------------------------------------------------------------------

# find words with length 5
string = 'kelly and jolly are best friends'
# \b used to get string present at start or end according to its position
# \w{5} used for alphanumeric characters with length 5
pattern = re.compile(r'\b\w{5}\b')
res = pattern.findall(string)
print(res)


# find three digits numbers
# string1 = "Emma's lucky numbers are 251 76155 231 451 4512"
# pattern = re.compile(r'\b\d{3}\b')
# pattern2 = re.findall(r'\bluck', string1)
# pattern1 = re.compile(r'\B\d{3}\B')
# res = pattern.findall(string1)
# res1 = pattern1.findall(string1)
# print(res)
# print(res1)
# print(pattern2)


# ----------------------------------------------------------------------------------------------------------------------
# re.search() method
# ----------------------------------------------------------------------------------------------------------------------

# target_string = "Emma is a baseball player who was born on June 17"
# res = re.search(r'\w{8}', target_string)   # re.search gives first occurrence of specified string in form of object
# print(f'matched word = {res}')
# print(f'matched word = {res.group()}')   # print result using group method
# res1 = re.search(r'ball', target_string)  # fetch the string 'ball' from baseball
# print(f'matched word = {res1.group()}')
# res2 = re.search(r'\bball\b', target_string)
# if res2:
#     print(f'matched word = {res2.group()}')
# else:
#     print('none')
# res3 = re.search(r'\bplayer\b', target_string)
# if res3:
#     print(f'matched word = {res3.group()}')
# else:
#     print('none')


# target_string = "Emma is a basketball player who was born on 1998, June 17"
# target_string2 = "Emma is a basketball player who was born on 19 98, June 17 in New York. 15"
# res1 = re.search(r'\d{2}', target_string)
# res = re.search(r'(\w{10}).+(\d{2})', target_string)
# res2 = re.search(r'(\w{10}).+(\d{2})', target_string2)  # this d{2} represent last occurrence of two digits number
# print(res1.group())
# print(res2.group())
# print(res.group())
# print(res.group(1), "-----", res.group(2))
# print(res.groups())

# ----------------------------------------------------------------------------------------------------------------------
# re.match() method
# ----------------------------------------------------------------------------------------------------------------------

# target_string = "Emma is a baseball player who was born on June 17"
#
# res = re.match(r'\w{4}', target_string)
# if res:
#     print(res.group())
# else:
#     print('None')
#
# res1 = re.match(r'\w{6}', target_string)
# if res1:
#     print(res1.group())
# else:
#     print('None')
#
# res2 = re.match(r'\bEmma\b', target_string)
# if res2:
#     print(res2.group())
# else:
#     print('None')
#
# res3 = re.match(r'\bplayer\b', target_string)
# if res3:
#     print(res3.group())
# else:
#     print('None')

# ----------------------------------------------------------------------------------------------------------------------

# target_string = "Jessa loves Python and pandas"
# # Match six-letter word
# pattern = r"\w{6}"
#
# # match() method
# result = re.match(pattern, target_string)
# if result:
#     print(result.group())
# else:
#     print('None')
#
# # search() method
# result = re.search(pattern, target_string)
# print(result.group())
#
# # findall() method
# result = re.findall(pattern, target_string)
# print(result)

# ----------------------------------------------------------------------------------------------------------------------
# re.fullmatch() method
# ----------------------------------------------------------------------------------------------------------------------

# str1 = "My name is maximums and my salary is 1000$"
#
# pattern = r'[A-Za-z0-9 | \s | \W]{2,}'
#
# result = re.fullmatch(pattern, str1)  # . is special character matching any character, no matter if it’s a
# # letter, digit, whitespace, or a symbol except the newline character
#
# # print entire match object
# print(result)
#
# # print actual match value
# print("Match :", result.group())


# email validation
# email = 'no-reply@pythontutorial.net'

# pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
# match = re.fullmatch(pattern, email)
# print(match.group())

# ----------------------------------------------------------------------------------------------------------------------
# re.finditer() method
# ----------------------------------------------------------------------------------------------------------------------

# target_string = "Emma is a basketball player who was born on June 17, 1993. She played 112 matches with a scoring average of 26.12 points per game. Her weight is 51 kg."
#
# pattern = r'\d{2}'
# pattern1 = r'\b\w{6}\b'
# pattern2 = r'\Bket'
# result = re.finditer(pattern2, target_string)
#
# # print all match object
# for match_obj in result:
#     # print each re.Match object
#     print(match_obj)
#
#     # extract each matching number
#     print(match_obj.group())

# ----------------------------------------------------------------------------------------------------------------------
# re.split() method
# ----------------------------------------------------------------------------------------------------------------------

# target_string = "My name is maximums and my luck numbers are 12 45 78"
# # split on white-space
# pattern = r'\s+'
# word_list = re.split(pattern, target_string)
# print(word_list)
#
# target_string = "12-45-78"
# ----------------------------------------------------------------------------------------------------------------------

# # Split only on the first occurrence
# # max split is 1
# pattern = re.compile(r'\D')
# result = pattern.split(target_string, maxsplit=1)
# print(result)
# # Output ['12', '45-78']

# # Split on the three occurrence
# # max split is 3
# result = pattern.split(target_string, maxsplit=3)
# print(result)
# ----------------------------------------------------------------------------------------------------------------------

# split string by two delimiters
# target_str = '12,15,20-18,21,55-78-91'
# pattern = r'\D'
# pattern1 = r',|-'
# result = re.split(pattern, target_str)
# result1 = re.split(pattern1, target_str)
#
# print(result)
# print(result1)

# ----------------------------------------------------------------------------------------------------------------------
# re.sub() method
# ----------------------------------------------------------------------------------------------------------------------

# replace all the whitespace with an underscore.
# target_str = "Jessa knows testing and machine learning"
# target_str1 = "Jessa     knows     testing     and     machine     learning"
# target_str2 = "      Jessa     knows     testing     and     machine     learning      "
#
#
# # \s+ used to remove all spaces, including single or multiple spaces
# res = re.sub(r'\s+', '_', target_str)
# res1 = re.sub(r'\s+', '_', target_str1)
#
# # count parameter used to set how many replacement to be done
# res2 = re.sub(r'\s+', '_', target_str1, count=1)
# res3 = re.sub(r'\s+', '_', target_str1, count=3)
#
# res4 = re.sub(r'^\s+ | \s+$', '', target_str2)
# res5 = re.sub(r'\s+', ' ', res4)
#
# print(res)
# print(res1)
# print(res2)
# print(res3)
# print(res5)

# ----------------------------------------------------------------------------------------------------------------------

# target_str = "   Jessa Knows Testing And Machine Learning.     "
#
# # ^\s+ remove only leading spaces
# # caret (^) matches only at the start of the string
# res_str = re.sub(r"^\s+", "", target_str)        # Remove leading spaces
# res_str1 = re.sub(r'\s+$', '', target_str)       # Remove trailing spaces
# res_str2 = re.sub(r'^\s+ | \s+$', '', target_str)      # Remove leading as well as trailing spaces
#
# print(res_str)
# print(res_str1)
# print(res_str2)



