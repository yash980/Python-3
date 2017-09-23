input_quote = input("Enter a 1 sentence quote, non - alpha seperate words: ")
word = ""

for character in input_quote:
    if character.isalpha():
        word += character

    else:
        if word and word[0].lower() >= "h":
            print("\n", word.upper())
            word = ""

        else:
            word = ""

if word.lower() >= "h":
    print("\n", word.upper())
