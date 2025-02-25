#!/usr/bin/env python3

import scipy
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics
from sklearn.cluster import KMeans


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    iris=load_iris()
    X= iris.data
    y= iris.target
    model=KMeans(n_clusters=3,random_state=0)
    model.fit(X)
    permutation = find_permutation(3,y,model.labels_)
    score = metrics.accuracy_score(y,[permutation[label] for label in model.labels_])


    return score

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
