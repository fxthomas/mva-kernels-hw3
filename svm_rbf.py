#!/usr/bin/python
# coding=utf-8

# Base Python File (svm_rbf.py)
# Created: Sun Feb 12 17:06:31 2012
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
# 
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>

import libras_loader
import numpy as np
from numpy import *
from scipy import *
from pylab import *
from sklearn import svm

data, classes = libras_loader.load ("data/movement_libras.data")
error_train = 0.
error_test = 0.
nb_tests = 20
train_ratio = 0.8
train_count = int(train_ratio * len (data))

for i in range(nb_tests):
  # Randomly sample data vectors
  _per = np.random.permutation(len(data))
  _ds = data[_per, :]
  _cs = classes[_per]
  data_train    = _ds[:train_count,:]
  data_test     = _ds[train_count:,:]
  classes_train = _cs[:train_count]
  classes_test  = _cs[train_count:]

  # Train SVM
  model = svm.SVC (C=14., gamma=.8, kernel='rbf')
  model.fit (data_train, classes_train)

  # Test model
  predictions_train = model.predict (data_train)
  predictions_test = model.predict (data_test)

  # Print errors
  error_train = error_train + float(len(find(predictions_train != classes_train)))/float(len(classes_train))
  error_test = error_test + float(len(find(predictions_test != classes_test)))/float(len(classes_test))

print "Average Error (Train): {0}%".format (error_train*100./nb_tests)
print "Average Error (Test): {0}%".format (error_test*100./nb_tests)
