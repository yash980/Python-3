import random

print("\n\nWelcome to BOLLYWOOD Game!\n\n")

bollywood = ['B','O','L','L','Y','W','O','O','D']

everything = []
clue = []
wood = []
guess = []
answer = []


file1 = open("bollywood.txt", 'r')

a = file1.readlines()

file1.close()

b = a[random.randint(0,5)]


c = b.split(":")


everything.append(c[0])
print("".join(everything))

clue.append(c[1])
print("".join(clue))

for i in c[2]:
    wood.append(i)


for j in c[3]:
    guess.append(j)

answer.append(c[4].strip("\n"))
final = "".join(answer)

count = 0
word = ""

while bollywood != []:
    
    user_input = input("\nGuess the Character: ").upper()
  
    if user_input in wood:
        count = wood.index(user_input)
        
        guess.pop(count)
        guess.insert(count, user_input)
        
        
        wood.pop(count)
        wood.insert(count,'0')
       
        xyz = "".join(guess)
        print(xyz, "\n")     
   
        if xyz == final:
            print("\nYou Win!\n")
            quit()
        else:
            pass

    elif user_input == final:
        print("\nYou Win!\n")
        quit()

    else:
        bollywood.pop(0)
        print(word.upper())
        print("\nYour Chances: ", "".join(bollywood))


print("\nYou Lost!\n")
