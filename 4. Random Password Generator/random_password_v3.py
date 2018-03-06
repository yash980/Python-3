import random
import re

symbols = ['!','@','#','$','%','&','_']
password = []


my_file = open("raw_text.txt", 'r')

read_file = my_file.readlines()
my_file.close()

single_word = read_file[random.randint(0,466543)]

cleaned_word = single_word.strip("\n")

rules = re.compile("\w+")
final_word = rules.findall(cleaned_word.title())

password.append(str(random.randint(0,99)))
password.append(symbols[random.randint(0,6)])
password.append("".join(final_word))
password.append(str(random.randint(0,999)))



print("\n\n\nYour Password is: ", "".join(password))
print("\r")
print("If you didn't like the Password, Please Generate it again! ;-)\n\n\n")

