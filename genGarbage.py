import math
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
wordLength = [2,8]
nonChars = ['0','1','2','3','4','5','6','7','8','9','.',',','-','&','/','\'']
def randChar(lettersList):
	return lettersList[random.randint(0,len(letters) - 1)]	

def randWord(letterList,wordLengths):
	word = ''
	for letter in range(0,random.randint(wordLengths[0],wordLengths[1])):
		word += randChar(letterList)
	return word

def genGarbage(numGarbage):
	outputFile = open("notWords.txt","w+")
	for word in range(0,numGarbage):
		#write a word to the file
		outputFile.write(randWord(letters, wordLength) + "\n")
	outputFile.close()

def removePunct(inputFile,outputFile, badChars):
	wordFile = open(inputFile, 'r')
	outFile = open(outputFile, 'w+')
	words = wordFile.readlines(0)
	print (len(words))
	for word in words:
		if (len(word) > 8):
			print('removing', word)
			words.remove(word)
			
	for word in words:
		for char in badChars:
			if (char in word):
				print('removing', word)
				words.remove(word)
				break
		else:
			continue
		break
	
	wordFile.close()
	print (len(words))
	for word in words:
		outFile.write(word)
	outFile.close()


def cleanGarbage(inputFile, comparisonFile):
	possibleNotWords = open((inputFile), 'w')
	englishWords = open
	possibleNotWords.close()
	return 0

genGarbage(50)
removePunct('allWords.txt', 'parsedWords.txt', nonChars)