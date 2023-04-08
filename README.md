Homoglyph Generator

This code is written in Python and consists of three functions to transform a user-entered sentence into a string of homoglyphs.

How to use this code:
Open the Python interpreter on your computer.
Copy and paste the code into the interpreter.
Run the main() function by typing main() in the interpreter and pressing Enter.
Enter your sentence when prompted and press Enter.
The resulting string of homoglyphs will be displayed.
Functions in this code:
uppercase(new_sentence1): This function takes a string as input and returns the same string with all lowercase letters converted to uppercase. ASCII characters are used for this conversion.

acronym(new_sentence2): This function takes a string as input and returns the first letter of each word in the string concatenated together. The first letter of the whole sentence is also included.

homoglyph(new_sentence3): This function takes a string as input and returns a new string where certain letters are replaced with homoglyphs. The letters "B" are replaced with "8", "C" with "[", "I" with "|", "J" with "]", "O" with "0", and "S" with "$". All other letters are left unchanged.

Example:
Input: "Hello, World!"

Output: "H3LL0[,]W0R][)!"
