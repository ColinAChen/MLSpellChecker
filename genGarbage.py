import math
import random
import time

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
wordLength = [7,7]
nonChars = ['0','1','2','3','4','5','6','7','8','9','.',',','-','&','/','\'']
def randChar(lettersList):
	return lettersList[random.randint(0,len(letters) - 1)]	

def randWord(letterList,wordLengths):
	word = ''
	for letter in range(0,random.randint(wordLengths[0],wordLengths[1])):
		word += randChar(letterList)
	return word

def genGarbage():

	realWordFile = open("sevenLetterWords.txt", "r")
	realWords = realWordFile.readlines()
	numWords = len(realWords)
	realWordFile.close()
	print ("Generating", numWords)
	outputFile = open("notSevenWords.txt","w+")
	for word in range(0,numWords):
		#write a word to the file
		wordToAdd = randWord(letters, wordLength) + "\n"
		while (wordToAdd in realWords):
			#print ('created a real word!', wordToAdd)
			wordToAdd = randWord(letters, wordLength) + "\n"

		outputFile.write(randWord(letters, wordLength) + "\n")

	outputFile.close()
def genExclusiveRand():
	word=''
	if (random.randint(0,len(letters)) > len(vowels)):
		#make a vowel only word
		for letter in range(0,random.randint(wordLengths[0],wordLengths[1])):
			word += randChar(vowels)
	else:
		for letter in range(0,random.randint(wordLengths[0],wordLengths[1])):
			word += randChar(consonants)

def genExclusiveGarbage():
	'''
	Generates fake words with only vowels or only consonants
	'''
	with open('exclusiveNotWords.txt') as file:
		file.write(randWord)

def removePunct(inputFile, outputFile, badChars):
	wordFile = open(inputFile, 'r')
	outFile = open(outputFile, 'w+')
	words = wordFile.readlines(0)
	print ('PREPROCESSED', len(words))
	time.sleep(2)
	word = 0
	while (word < len(words)):
		if (len(words[word]) > 8 or len(words[word] < 3)):
			print('removing', words[word])
			words.remove(words[word])
			word -= 1
		word += 1
	print ('AFTER length',len(words))
	time.sleep(2)
	word = 0
	while (word < len(words)):
		for char in badChars:
			if (char in words[word]):
				print('removing', words[word])
				words.remove(words[word])
				word -= 1
				break
		word += 1
	wordFile.close()
	print (len(words))
	for word in words:
		outFile.write(word)
	outFile.close()


def fileToLower(lowerFile):
	wordFile = open(lowerFile, 'r')
	wordsInFile = wordFile.readlines()
	wordFile.close()
	writeFile = open(lowerFile, 'w')

	for word in wordsInFile:
		#print (word.lower())
		writeFile.write(word.lower())
	writeFile.close()


'''
def cleanGarbage(inputFile, comparisonFile):
	actualWords = open(comaprisonFile, 'r')
	possibleNotWords = open((inputFile), 'rw')
	actualWordsList = actualWords.readlines()
	possibleNotWordsList = possibleNotWords.readlines()

	#####Binary Search Tree to remove real words from the fake words
	for possibleNotWord in possibleNotWordsList:	
		start = actualWords[int(len(actualWords)/2)]#will round down so can be missing one if odd number
		if (possibleNotWord[0:1] == start[0:1]):	#first letter equal

		if (possibleNotWord[0:1] > start[0:1]):		#



	possibleNotWords.close()
	actualWords.close()
	return 0

'''
'''
test = ['hello', 'HELLO']
for testWord in range(0,len(test)):
	test[testWord] = test[testWord].lower()
print (test)
'''
#fileToLower('parsedWords.txt')
#removePunct()
if __name__ == '__main__':
	genGarbage()

#removePunct('allWords.txt', 'parsedWords.txt', nonChars)