import random
import re

symbols = ['!','@','#','$','%','&']
password = []
final_password = []

file1 = open("clues.txt", 'r')

rules = re.compile("\w+")
a = file1.readlines()

file1.close()

b = a[random.randint(0,4)]

c = b.strip("\n")

d = rules.findall(c)

for word in d:
    if len(word) >= 5 and word.isalpha:
        password.append(word)
    else:
        pass

final_password.append(str(random.randint(0, 99)))
final_password.append(symbols[random.randint(0, 5)])
final_password.append(password[random.randint(0, len(password) - 1)])
final_password.append(str(random.randint(0, 999)))

print("\n\n\nYour Password is: ", "".join(final_password), "\n\n\n")
