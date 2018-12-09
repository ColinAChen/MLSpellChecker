import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Dropout
from tensorflow.python.keras.layers import Flatten
from tensorflow.python.keras.layers.convolutional import Conv2D
from tensorflow.python.keras.layers.convolutional import MaxPooling2D
from tensorflow.python.keras.utils import np_utils
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import load_model

import numpy


def parseData (inputFile, classLabel):
	x = []
	y = []


	fileToParse = open(inputFile, 'r')
	words = fileToParse.readlines()

	for word in words:
		wordCorrected = ''
		char = 0
		#rebuild each string, remove new line characters and add null terminating character if the word is less than 7 letters
		while(char < 7):
			try:
				if (word[char:char+1] != '\n'):
					wordCorrected += word[char:char+1]
				else:
					wordCorrected += '\0'
				char += 1
			except:
				wordCorrected += '\0'
				char += 1
		print (wordCorrected)
		x.append(wordCorrected)
		y.append(classLabel)

	return x, y

def kerasModel(maxWordLength):

	model = Sequential()

	model.add(Dense(units = 64), activation = 'relu', input_dim = maxWordLength)
	model.add(Dense(units = 10), activation = 'softmax')
	# For a binary classification problem
	model.compile(optimizer='rmsprop',
					loss='binary_crossentropy',
					metrics=['accuracy'])


parseData('parsedWords', 'real')