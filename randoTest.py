from keras.models import load_model
import numpy as np
spellCheckModel = load_model('layerTest.h5')
def spellCheck (possibleWord):
	print ('Checking',possibleWord)
	processWord = []
	temp = []
	#print(len(processWord))
	for letter in range(7):
		#print(letter)
		if (letter < len(possibleWord)):
			#print (possibleWord[letter:letter+1], ord(possibleWord[letter:letter+1]))
			processWord.append(ord(possibleWord[letter:letter+1]))
		else:
			processWord.append(0)
	temp.append(processWord)
	#print (temp)
	processWord = np.array(temp)
	return spellCheckModel.predict(processWord)
print(spellCheck('hello'))
print(spellCheck('wow'))
print(spellCheck('tree'))
print(spellCheck('seven'))
print(spellCheck('asdfjk'))
print(spellCheck('iowahn'))

testWord = input('word to test\n')
while(testWord != '~'):
	print(spellCheck(testWord))
	testWord = input('word to test')