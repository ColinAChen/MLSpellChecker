import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
from keras.models import load_model

from skimage import exposure
from tensorflow.contrib.layers import flatten
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import numpy as np

import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import random
def parseData (inputFile, classLabel):
	x = []
	y = []


	fileToParse = open(inputFile, 'r')
	words = fileToParse.readlines()#list of words

	for word in words:
		wordCorrected = []#list to hold each value of character ascii
		char = 0
		#rebuild each string, remove new line characters and add null terminating character if the word is less than 7 letters
		while(char < 7):
			try:
				if (word[char:char+1] != '\n'):
					#wordCorrected += word[char:char+1]
					wordCorrected.append(ord(word[char:char+1]))
				else:
					wordCorrected.append(0)
					#wordCorrected += '\0'
				char += 1
			except:
				wordCorrected.append(0)
				#wordCorrected += '\0'
				char += 1
		#if (random.randint(0,420) == 69):
			#print (wordCorrected, classLabel)
		x.append(wordCorrected)
		y.append(classLabel)
	return x, y
def loadData():
	xWords, yWords = parseData('scrambledParsed.txt', 1)
	xNotWords, yNotWords = parseData('notWords.txt', 0)

	x = np.array(xWords + xNotWords)
	y = np.array(yWords + yNotWords)
	return x, y
def kerasModel(maxWordLength):

	model = Sequential()
	'''
	model.add(Dense(units = 64), activation = 'relu', input_dim = maxWordLength)
	model.add(Dense(units = 10), activation = 'softmax')
	# For a binary classification problem
	model.compile(optimizer='adam',
					loss='binary_crossentropy',
					metrics=['accuracy'])
	'''
	model.add(Dense(maxWordLength, input_dim=maxWordLength, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
	# Compile model
	
	model.save('spellCheckerModel3.h5')
	return model

#parseData('parsedWords', 'real')

def create_baseline():
	# create model
	model = Sequential()
	model.add(Dense(60, input_dim=60, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
	# Compile model
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model





scaled_X,y = loadData()
#parseData('notWords.txt', 0)

#from kmather73 github hot dog not hot dog binary classifier
rand_state = np.random.randint(0, 100)
X_train, X_test, y_train, y_test = train_test_split(scaled_X, y, test_size=0.2, random_state=rand_state)
model = kerasModel(7)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(X_train, y_train, nb_epoch=10, validation_split=0.1)
metrics = model.evaluate(X_test, y_test)
for metric_i in range(len(model.metrics_names)):
    metric_name = model.metrics_names[metric_i]
    metric_value = metrics[metric_i]
    print('{}: {}'.format(metric_name, metric_value))


'''
#from machinelearningmastery
seed = 7
# evaluate model with standardized dataset
estimator = KerasClassifier(build_fn=kerasModel(7), epochs=100, batch_size=5, verbose=0)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, encoded_Y, cv=kfold)
print("Results: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
'''