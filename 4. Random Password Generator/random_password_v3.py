import random
import re

symbols = ['!','@','#','$','%','&','_']
password = []


file1 = open("raw_text.txt", 'r')

a = file1.readlines()
file1.close()

b = a[random.randint(0,466543)]

c = b.strip("\n")

rules = re.compile("\w+")
d = rules.findall(c.title())

password.append(str(random.randint(0,99)))
password.append(symbols[random.randint(0,6)])
password.append("".join(d))
password.append(str(random.randint(0,999)))



print("\n\n\nYour Password is: ", "".join(password))
print("\r")
print("If you didn't like the Password, Please Generate it again! ;-)\n\n\n")

