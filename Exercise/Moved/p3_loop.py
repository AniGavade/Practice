text = input("Enter the text\n")
spam = False
if("make a lot of money"):
    spam = True
elif("buy now" in text):
    spam = True
elif("Subscribe this for rewards" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")
