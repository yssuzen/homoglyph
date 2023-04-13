#Creating a function which makes uppercase all letters.
def uppercase(new_sentence1):
	#Letters will be added into new_sentence_2 variable
	new_sentence_2 = ""
	
	#Making letters uppercase with ASCII characters
	for letter in range(len(new_sentence1)):
		
		if new_sentence1[letter] == " ":
			new_sentence_2 += " "	
		#If user enters an uppercase letter, this letter will add the variable without any changing		
		elif ord(new_sentence1[letter]) >= 65 and ord(new_sentence1[letter]) <=90: 
			new_sentence_2 += new_sentence1[letter]									
		else:		
			new_sentence_2 += chr(ord(new_sentence1[letter]) - 32)
	#returning new_sentence_2 variable	
	return new_sentence_2	
		
#Creating a function that combines the first letter of each word.
def acronym(new_sentence2):

	#Adding first letter of the sentence to new_acronym variable
	new_acronym = new_sentence2[0]

	for letter in range(len(new_sentence2)):
		#if there is a space before a letter, that letter will be added into new_acronym variable
		if new_sentence2[letter-1]== " ":
			new_acronym += new_sentence2[letter]		
	#returning new_acronym variable	
	return new_acronym

	
#Creating a function that converts 7 letters to homoglyphs 	
def homoglyph(new_sentence3):

	#It is for adding each letter and converted letters.
	new_homoglyph = ""	
	
	for letter in range(len(new_sentence3)):
		#if the letter is 'B', it wil be shown '8'.
		if new_sentence3[letter] == "B":
			new_homoglyph += "8"
		#if the letter is 'C', it wil be shown '['.	
		elif new_sentence3[letter] == "C":
			new_homoglyph += "["
		#if the letter is 'I', it wil be shown '|'.	
		elif new_sentence3[letter] == "I":
			new_homoglyph += "|"
		#if the letter is 'J', it wil be shown ']'.	
		elif new_sentence3[letter] == "J":
			new_homoglyph += "]"	
		#if the letter is 'O', it wil be shown '0'.	
		elif new_sentence3[letter] == "O":
			new_homoglyph += "0"	
		#if the letter is 'S', it wil be shown '$'.	
		elif new_sentence3[letter] == "S":
			new_homoglyph += "$"
		#Otherwise, letters will be added into new_homoglyph variable.	
		else:
			new_homoglyph += new_sentence3[letter]	
	#returning new_homoglyph variable		
	return new_homoglyph			
				

	
	

#Creating main function		
def main():
	
	#Getting a string from user via input function
	string = input("Please write your sentence or sentences: ")	
	
	#This will be used for determining whether sentence has punctuations
	punc = ",./?:;'{}[]\|!*()`~@#$%^&-_"
	
	#After removing all punctuations, the new sentence will be added into new_sentence variable.
	new_sentence = ""
	
	for letter in string:
		#If any punctuations are available in the sentence/sentences, they will not be added into the new_sentence
		if letter not in punc:
			new_sentence += letter
	
	#Calling previous functions
	result = homoglyph(acronym(uppercase(string)))
	
	#Printing the result
	print(result)
#Calling the main function
main()	
