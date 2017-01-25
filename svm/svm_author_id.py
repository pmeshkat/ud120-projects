#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 
from sklearn.svm import SVC
# clf = SVC(kernel="linear")
for C_val in [10,100,1000,10000]:
	clf = SVC(kernel="rbf", C=C_val)

	clf.fit(features_train,labels_train)
	labels_predict=clf.predict(features_test)

	from sklearn.metrics import accuracy_score
	print  'C is:', C_val, 'Accuracy is: ', accuracy_score(labels_predict,labels_test)

# clf = SVC(kernel="rbf",C=10000)


#########################################################
### your code goes here ###

#########################################################


