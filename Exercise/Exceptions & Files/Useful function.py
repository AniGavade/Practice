# print(", ".join(["spam", "eggs", "ham"]))

# print("Hello Me".replace("me", "World"))

# print("This is a sentence.".startswith("This"))

# print("This is a sentence.".endswith("sentence"))

# print("This is a sentence.".upper())

# print("AN ALL CAPS SENTENCE".lower())

# print("spam, eggs, ham".split(", "))
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# print(min(1, 2, 3, 4, 0, 2, 1))
# print(max([1, 4, 9, 2, 5, 6, 8]))
# print(abs(-99))
# print(abs(42))
# print(sum([1, 2, 3, 4, 5]))
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# n = [55, 44, 33, 22, 11]
# if all([i > 5 for i in n]):
#     print("All larger than 5")

# if any([i % 2 == 0 for i in n]):
#     print("At least one is even")

# for v in enumerate(n):
#     print(v)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# filename = input("enter a filename: ")

# with open(filename)as f:
#     text = f.read()

# print(text)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def count_char(text, char):
#     count = 0
#     for c in text:
#         if c == char:
#             count += 1
#     return count

# filename = input("Enter a filename: ")
# with open(filename) as f:
#     text = f.read()

# print(count_char(text, "i"))
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# #  To find out largest word from input.

# def largestWord(s):
  
#     s = sorted(s, key = len)
  
#     print(s[-1])
  

# s = input("The function enumerate can be used to iterate through the values and indices of a list simultaneously")

# l = list(s.split(" "))
  
# largestWord(l)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# #  Function  programming

# def apply_twice(func, arg):
#     return func(func(arg))

# def add_five(x):
#     return x + 5

# print(apply_twice(add_five, 10))

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def polynomial(x):
#     return x**2 + 5*x + 4
# print(polynomial(-4))
# print((lambda x: x**2 + 5*x +4)(-4))
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def add_five(x):
#     return x + 5

# n = [11, 22, 33, 44, 55]
# result = list(map(add_five, n))
# print(result)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# n = [11, 22, 33, 44, 55]

# result = list(map(lambda x: x+5, n))
# print(result)\
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def countdown():
#     i=5
#     while i>0:
#         yield i
#         i -= 1

# for i in countdown():
#     print(i)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def n(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i

# print(list(n(11)))
# ////////////////////////////////////////////////////////////////////////////////////////////////

def make_word():
    word = ""
    for i in "spam":
        word += i
        yield word
print(list(make_word()))