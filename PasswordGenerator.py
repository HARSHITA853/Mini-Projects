import random
import string
letters=string.ascii_letters
digits=string.digits
characters=string.punctuation
char=letters + digits + characters
length=int(input("enter the length of the password "))
password=""
for i in range(0,length):
    password+=random.choice(char)
print("Your Password is: ",password)