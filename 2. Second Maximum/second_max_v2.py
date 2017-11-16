#Write a method to find 2nd maximum number in a single traversal.
numbers = []                            # Declare an empty list
maximum, second_max, a, b = 0, 0, 0, 0  # Initialisation of variables

print("Enter 10 numbers: ")

for number in range(10):                 # Define range 10 to accept 10 values
    numbers.append(int(input()))         # Accepting values and appending it to list
    if maximum < numbers[number]:        # Comparing maximum with each number from list
        a = maximum                      # Storing previous maximum number
        maximum = numbers[number]        # Storing maximum number
    elif numbers[number] > b and numbers[number] < maximum: # Checking for redundant number in list
        b = numbers[number]              # Storing previous maximum number
    else:
        pass

if a > b:                                # Comparison between previous maximum if list is in ascending order. 
    second_max = a
else:
    second_max = b

print("The maximum number is: ", maximum)
print("The second maximum number is: ", second_max)
