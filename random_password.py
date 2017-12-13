import random
symbols = ['!','@','#','$','%','&']
password = []

file1 = open("alphabets.txt", 'r')

a = file1.readlines()

file1.close()

b = a[random.randint(0,51)]
x = a[random.randint(0,51)]
y = a[random.randint(0,51)]
z = a[random.randint(0,51)]

c = b.strip("\n")

password.append(c)
password.append(str(random.randint(0,999)))
password.append(x.strip("\n"))
password.append(symbols[random.randint(0,5)])
password.append(y.strip("\n"))
password.append(str(random.randint(0,999)))
password.append(z.strip("\n"))

print("\n\n\nYour Password is: ", "".join(password), "\n\n\n")


