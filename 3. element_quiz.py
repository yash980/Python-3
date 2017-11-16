# !curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt

def get_names():
    elements_list = []

    while len(elements_list) != 5:
        user_input = input("Enter the name of an element: ")

        if user_input in elements_list:
            print(user_input, "was already entered     <--no duplicates allowed")
        elif user_input == "":
            pass
        else:
            elements_list.append(user_input.lower())
    return elements_list


elements_file = open('elements1_20.txt', 'r')
main_list = []

while len(main_list) != 20:
    elements_text = elements_file.readline().strip()
    main_list.append(elements_text.lower())

elements_list = get_names()

correct_response = []
incorrect_response = []

for elem1 in elements_list:
    if elem1 in main_list:
        correct_response.append(elem1)
    else:
        incorrect_response.append(elem1)

result = int(len(correct_response) * 20)
print()
print(result, "% correct")
print("Found: ", " ".join(correct_response).title())
print("Not Found: ", " ".join(incorrect_response).title())
