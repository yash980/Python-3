import random

sides = ("Head", "Tail") # Tuple containing string.
print("Your luck says, It's a", sides[random.randint(0,1)], "!") # Print either Head or Tail!

# Used random integers in the range of 0 to 1.
# Furthermore, used this random integer as index of Tuple.
# Print the string stored in the Tuple using random integer (Index).
