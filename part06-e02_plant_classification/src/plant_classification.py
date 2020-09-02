#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    iris=load_iris()
    X= iris.data
    y= iris.target
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,random_state=0,test_size=0.2)
    model=naive_bayes.GaussianNB()
    model.fit(Xtrain,ytrain)
    ytest_fitted=model.predict(Xtest)
    acc=metrics.accuracy_score(ytest,ytest_fitted)
    return acc

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
