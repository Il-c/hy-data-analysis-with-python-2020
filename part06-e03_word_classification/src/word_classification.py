#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree
import re
import numpy as np

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn import model_selection
from sklearn import linear_model
from sklearn.neural_network import MLPClassifier
import pickle

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('//kotus-sanalista/st/s')
   
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return list(lines)

def get_features(a):
    features=np.array([[]])
    b=np.array([])
    features=[counter(row) for row in a]
    return np.array(features)

def counter(sana):
  #  features=np.array([[]])
    features=np.zeros((len(alphabet),1))
    for char in sana:
        if char in alphabet:
            features[alphabet.find(char)]+=1
    features=np.ravel(features)

  #  for char in alphabet:
   #         features=np.append(features,sana.count(char))
    return features

def contains_valid_chars(s):
    set(s)<=alphabet_set
    return set(s)<=alphabet_set
def startswithcap(s):
    if s[0].isupper():
        return False
    return True
def get_features_and_labels():
    finnish=load_finnish()
    english=load_english()

    finnish=[word.lower() for word in finnish]
    finnish=list(filter(contains_valid_chars,finnish))

#    pref_list=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','V','X','Y','Z')
   
    english = list(filter(startswithcap,english))
    english=[word.lower() for word in english]
    english=list(filter(contains_valid_chars,english))
    
    

    X = np.concatenate((get_features(finnish),get_features(english)),axis=0)
    y_fin = np.zeros((len(finnish),1))
    y_eng = np.ones((len(english),1))
    y=np.concatenate((y_fin,y_eng),axis=0)

    return X, y


def word_classification():
    X,y=get_features_and_labels()
    y=np.ravel(y)
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,random_state=1,test_size=0.4)
    pkl_filename='pickle_model.pkl'
    with open(pkl_filename, 'rb') as file:
        pickle_model=pickle.load(file)
    
 
## NEURAL NETWORK--------------------------------- 
  #  clf=MLPClassifier(hidden_layer_sizes=(20,), random_state=1,max_iter=50)
  #  clf.fit(Xtrain,ytrain)
   # ypredict=clf.predict(Xtest)
  #  score=clf.score(Xtest,ytest)
# MultinomialNB with cross validation------------------------------------------------------
  #  model=MultinomialNB()
   # param=model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
  #  score = cross_val_score(model,X,y,cv=param)
  #  y_pred = cross_val_predict(model,X,y,cv=param)
  #  final_model=model.fit(X,y)
# Gaussian Naive Bayes---------------------------------------------------------------
 #   gnb=GaussianNB()
 #   gnb.fit(Xtrain,ytrain)
 #   ypred=gnb.predict(Xtest)
 #   score=metrics.accuracy_score(ytest,ypred)
# Plain MultinomialNB
#    mnb=MultinomialNB()
#    mnb.fit(Xtrain,ytrain)
#    ypred=mnb.predict(Xtest)
#    score=metrics.accuracy_score(ytest,ypred)

    
 #   with open(pkl_filename, 'wb') as file:
 #       pickle.dump(clf, file)

 #   Xtesti=['soft','keinu','try','kiipeli','katto','gun']
    while True:
        sana=input('Kirjoita sana: ')
        if sana=='':
            break
        Xtesti=[sana]
        featuresoma=get_features(Xtesti)
        featuresoma=np.vstack(featuresoma)
        result=pickle_model.predict(featuresoma)
        if result[0]==0:
            print('Sana on suomea!')
        else:
            print('You wrote in english!')

        
    ypred=pickle_model.predict(Xtest)
    score=metrics.accuracy_score(ytest,ypred)

    return score


def main():
   
 #   print(contains_valid_chars('Agdfgh'))
    get_features_and_labels()
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
