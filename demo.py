# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/hoangks5/da76a870c766304de6778a793d4284ce/untitled21.ipynb
"""

pip install python-docx

pip install tflearn

import docx
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import json
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from tensorflow.python.framework import ops
import numpy as np
import tflearn
import tensorflow
import random
import pickle

# Up load các file luận văn khác nhau
# Tạo 1 file tên "main.json" và upload lên
def upfile():
  from google.colab import files
  upload = files.upload()

def __dell__(sentence):
  sentence = sentence.lower()
  sentence = re.sub(r'[~!@#$%\^&*\(\)\[\]\\|:;\'"]+', ' ', sentence)
  sentence = re.sub(r'\s+', ' ', sentence).strip()
  sentence = sent_tokenize(sentence)
  return sentence

def __read__file__(name):
        doc = docx.Document(name)  # Creating word reader object.
        data = ""
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            data = '\n'.join(fullText)
        print(data)
        return(data)

def __upload__(s):  
  information = __dell__(s)
  __add__ = {
      "intents": [
          
          {   
                             
          }
      ]
  }
  with open('main.json','w',encoding='utf-8') as fp: # Thêm dữ liệu vào tệp JSON
      json.dump(__add__, fp, indent=2,)

def update_json(s):
    with open("main.json",'r', encoding='utf-8') as fp:
        information1 = json.load(fp)
    information1["intents"].append({
        "title": s,
        "text": __dell__(__read__file__(s))
    })
    with open("main.json",'w',encoding='utf-8') as fp: # Thêm dữ liệu vào tệp JSON
        json.dump(information1, fp, indent=2,)

def __inp__name__():
  __nb__ = int(input("Số bài tiểu luận bạn cần train: "))
  __lib_dict__ = []
  for i in range(__nb__):
    __name__ = str(input("Tên file tiểu luận "+str(i+1)+" (vd: file.docx):"))
    __lib_dict__.append(__name__)
  return __lib_dict__

b = __inp__name__()

def main():
  b = __inp__name__()
  __upload__(__read__file__(b[0]))
  for i in range(len(b)-1):
    update_json(b[i+1])

main()

upfile()

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

ops.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training
#model.fit(train_x, train_y, n_epoch=300, batch_size=8, show_metric=True)
#model.save('model.tflearn')

pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" ) )

# restore our data structures
import pickle
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

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# bag of words
def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

# data structure to hold user context
context = {}

ERROR_THRESHOLD = 0.25
def test(sentence):
    results = model.predict([bow(sentence, words)])[0]
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    return print("Câu này khả năng nằm trong văn bản "+classes[r[0]]+" với độ chính xác "+str(r[1]*100)+" %")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

test('however, when a component needs to use another component in order to function, it adopts a used interface that specifies the services that it needs.')
test('in any case, when a part needs to utilize one more part to work, it takes on a pre-owned interface that determines the administrations that it needs.')

