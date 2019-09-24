# MLSpellChecker
Neural network to perform rudimentary spell checking

## Motivation
Spell checking in WordMochaSolver is done with a deprecated external library. The existing library's predictions are inaccurate. I want to see if I can do better without performing an expensive lookup after generating all possible words. 

## Methods

#### Obtaining real words
English words were extracted from this [repo](https://github.com/dwyl/english-words).
I removed numbers, words shorter than three letters, and words longer than seven letters. I did this to match the words you expect to find in the game Word Mocha. 

#### Creating fake words
I created fake words by choosing a random word length between four and seven, then choosing random letters, then finally checking the list to ensure I didn't accidently create a real word.

#### Training
Each word is represented as an input vector of length seven. Words with less than seven letters are padded with zeroes. I tried an individual network for different lengths but found the highest accuracy with all word lengths combined.

I modified a [binary classifier](https://machinelearningmastery.com/binary-classification-tutorial-with-the-keras-deep-learning-library/). 

## Results
My current highest accuracy is 71 percent. This model misidentified words such as "hello" making it useless for this application.

## Future work
There are ways I would like to improve this model. 
#### Fake word creation
I would like to experiment with the distribution of word lengths in the fake words. The word lengths are currently chosen randomly and there is expected to be an equal distribution of four to seven letter words. I would like to experiment with creating a fake word list than closely matches the distribution of word lengths found in the real word list.
#### Training
I would like to experiment with using a larger network to achieve higher accuracy. I would like to explore how large a network I can create before it is no longer useful for fast spellchecking.
