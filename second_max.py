#Write a method to find 2nd maximum number in array in single traversal.
numbers = [] # Declared an empty list
print("Enter 10 numbers: ") # User input for numbers
for number in range(10): # Parsing through index 10 times to accept 10 numbers.
    numbers.append(int(input())) # Accepting user input and appending it to the list.
numbers.sort() # Using sort method to sort the number in list by traversing it.
print("\nThe maximum second number is: ", numbers[-2]) # Directly displaying the value present at second last index by index slicing.
