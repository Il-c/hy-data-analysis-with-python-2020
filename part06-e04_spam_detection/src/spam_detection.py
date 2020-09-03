#!/usr/bin/env python3
import gzip
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn import model_selection
from sklearn.model_selection import LeaveOneOut

def spam_detection(random_state=0, fraction=0.5):
    valid_mails=[]
    spams=[]
    with gzip.open('src/ham.txt.gz','rb') as f:
        valid_mails=f.readlines()
    with gzip.open('src/spam.txt.gz','rb') as f:
        spams = f.readlines()
    
    end_valid = fraction*len(valid_mails)
    end_spam = fraction*len(spams)
    ham=valid_mails[0:int(end_valid)]
    spam=spams[0:int(end_spam)]
    ham.extend(spam)
#kommentti
    vec = CountVectorizer()
    X=vec.fit_transform(ham)
    yham=np.zeros((int(end_valid),1))
    yspam=np.ones((int(end_spam),1))
    y=np.concatenate((yham,yspam))
    y=np.ravel(y)
    koe = pd.DataFrame(X.toarray(), columns = vec.get_feature_names())
  
    Xtrain, Xtest, ytrain, ytest = train_test_split(koe,y,random_state=random_state,test_size=0.25)
    model = MultinomialNB()
    model.fit(Xtrain, ytrain)
    ypred=model.predict(Xtest)
    score=metrics.accuracy_score(ytest,ypred)
    missed=np.sum(ytest!=ypred)
 
    return score, Xtest.shape[0] , missed

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
