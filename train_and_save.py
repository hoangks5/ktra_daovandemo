import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.util import pr
stemmer = LancasterStemmer()
import pickle
import numpy
import tflearn
import tensorflow
import random
import json
import os
import itertools
from math import log
import re
from tensorflow.python.framework import ops
import re
import json
import itertools
from math import log
import datetime
import webbrowser as wb


        


with open("training.json",encoding="utf8") as file:
    data = json.load(file)
try:
    with open("data.pickle", "ab") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
    
    for intent in data["intents"]:
        for pattern in intent["text"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["title"])
            
            if intent["title"] not in labels:
                labels.append(intent["title"])
                
    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))
    
    labels = sorted(labels)
    
    training = []
    output = []
    
    out_empty = [0 for _ in range(len(labels))]
    
    for x, doc in enumerate(docs_x):
        bag = []
        
        wrds = [stemmer.stem(w) for w in doc]
        
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
                
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1
        
        training.append(bag)
        output.append(output_row)
        
        
    training = numpy.array(training)
    output = numpy.array(output)
    
    with open("data.pickle", "ab") as f:
        pickle.dump((words, labels, training, output), f)
ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)


try:
    model.load(model.tflearn)
except:
    pass
    model.fit(training, output, n_epoch=100, batch_size=8, show_metric=True)
    model.save("model.tflearn")
    
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    
    for se in s_words:
        for i,w in enumerate(words):
            if w == se:
                bag[i] = 1
    return numpy.array(bag)


 
    
    
def chat():
    f = open('ss.txt','r',encoding='utf-8')
    f = f.read()
    f = f.split('.')
    N = []
    M = []
    Q = []
    for inp in f:
        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        if results[results_index] > 0.5:
            for tg in data["intents"]:
                if tg['title'] == tag:
                    responses = tg['title']
                    M.append(responses)
    for iss in M:
        kq = iss+' : '+str(M.count(iss)/len(M)*100)+' %'
        N.append(kq)
        for kq in N:
            if kq not in Q:
                Q.append(kq)
    print(Q)
chat()
