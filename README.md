# Python-3

### Synopsis: 
Inputs a phrase and prints all of the words that start with h-z.

### Sample input: 
Enter a 1 sentence quote, non-alpha separate words: `Time and Tide waits for none.`

### Sample output: 
```
TIME
TIDE
WAITS
NONE
```
            
### Algorithm:

1.  Split the words by building a placeholder variable: word
*  Loop each character in the input string
*  Check if character is a letter
*  Add a letter to word each loop until a non-alpha char is encountered
	
2.  If character is alpha
*  Add character to word
*  Non-alpha detected (space, punctuation, digit,...) defines the end of a word and goes to else
	
3.  Else
*  Check if word is greater than "g" alphabetically 
*  Print word
*  Set word = empty string
	
4.  Or else 
*  Set word = empty string and build the next word


**NOTE:** *How you will print the last word if it doesn't end with a non-alpha character like a space or punctuation?*
