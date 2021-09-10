import pickle
import json
import nltk
import random
import numpy as np
import tensorflow

from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
###################################################################

with open('main.json') as json_data:
    intents = json.load(json_data)

words = []
classes = []
documents = []
stop_words = ['?', 'a', 'an', 'the']

for intent in intents['intents']:
    for pattern in intent['text']:

        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['title']))
        if intent['title'] not in classes:
            classes.append(intent['title'])

words = [stemmer.stem(w.lower()) for w in words if w not in stop_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

training = []
output = []
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
random.shuffle(training)
training = np.array(training)

# create train and test lists
train_x = list(training[:,0])
train_y = list(training[:,1])

pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" ) )

# restore our data structures

data = pickle.load( open( "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

# import intents file
import json
with open('main.json') as json_data:
    intents = json.load(json_data)


model.load('./model.tflearn')