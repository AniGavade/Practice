# Python Counter to find the size of largest subset of anagram words
#
# from collections import Counter


# def largeSubset(word):
#
#     word = word.split(" ")
#
#     for i in range(0, len(word)):
#         word[i] = "".join(sorted(word[i]))
#
#     a = Counter(word)
#     print(max(a.values()))
#
#
# if __name__ == "__main__":
#     word = "rukna evol ylfrettub tub vole ylfrettub evol knura"
#     largeSubset(word)
