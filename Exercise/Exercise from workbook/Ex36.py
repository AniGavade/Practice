# Vowel or Consonant.

vowel = input("Enter the vowel: ")
if vowel in ("a", "e", "i", "o", "u"):
    print("%s is a vowel." % vowel)
elif vowel == "y":
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print("%s is consonant." % vowel)