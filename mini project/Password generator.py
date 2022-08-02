import random

l = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = "0123456789"
symbols_ = "!@#$%^&*()."

str_ = l + u + n + symbols_
length_ = 8
password_ = "".join(random.sample(str_, length_))

print("Your new password is: ", password_)