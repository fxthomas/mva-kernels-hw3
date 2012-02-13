#!/usr/bin/python
# coding=utf-8

# Base Python File (svm_linear.py)
# Created: Sun Feb 12 17:06:31 2012
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
# 
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>

import xml_loader
import libras_loader
import numpy as np
from numpy import *
from scipy import *
from pylab import *
from sklearn import svm
from matplotlib.colors import rgb2hex

#data, classes = libras_loader.load ("data/movement_libras.data")
data, classes = xml_loader.load ("data/HandWritingModels.xml")
error_train = 0.
error_test = 0.
nb_tests = 20
train_ratio = 0.8
train_count = int(train_ratio * len (data))

# Randomly sample data vectors
_per = np.random.permutation(len(data))
_ds = data[_per, :]
_cs = classes[_per]
data_train    = _ds[:train_count,:]
data_test     = _ds[train_count:,:]
classes_train = _cs[:train_count]
classes_test  = _cs[train_count:]

C_values = exp (arange(-5, 10, 0.1))
gamma_values = exp (arange (-2, 5, 1))
degree_values = arange (1, 5, 1)
error_train_values = zeros (C_values.shape)
error_test_values = zeros (C_values.shape)

phi = get_cmap('jet')
colors = [phi(float(i)/float(len(gamma_values)+len(degree_values)+2)) for i in range(len(gamma_values)+len(degree_values)+2)]

for j in range(len(gamma_values)):
  for i in range(len(C_values)):
    gamma = gamma_values[j]
    C = C_values[i]
    print "  --> Gamma = {0} ; C = {1}".format (gamma, C)

    # Train SVM
    model = svm.SVC (C=C, gamma=gamma, kernel='rbf')
    model.fit (data_train, classes_train)

    # Test model
    predictions_train = model.predict (data_train)
    predictions_test = model.predict (data_test)

    # Print errors
    error_train_values[i] = float(len(find(predictions_train != classes_train)))/float(len(classes_train))
    error_test_values[i]  = float(len(find(predictions_test != classes_test)))/float(len(classes_test))

  semilogx (C_values, error_test_values, color=colors[j], label="RBF Kernel, g={0:.1f}".format(gamma), linewidth=3.0)

for j in range(len(degree_values)):
  for i in range(len(C_values)):
    degree = degree_values[j]
    C = C_values[i]
    print "  --> Degree = {0} ; C = {1}".format (gamma, C)

    # Train SVM
    model = svm.SVC (C=C, degree=degree, kernel='poly', gamma=1.0)
    model.fit (data_train, classes_train)

    # Test model
    predictions_train = model.predict (data_train)
    predictions_test = model.predict (data_test)

    # Print errors
    error_train_values[i] = float(len(find(predictions_train != classes_train)))/float(len(classes_train))
    error_test_values[i]  = float(len(find(predictions_test != classes_test)))/float(len(classes_test))

  semilogx (C_values, error_test_values, color=colors[j+len(gamma_values)], label="Polynomial Kernel, d={0:.0f}".format(degree), linewidth=3.0)

for i in range(len(C_values)):
  C = C_values[i]
  print "  --> Sigmoid, C = {0}".format (C)

  # Train SVM
  model = svm.SVC (C=C, kernel='sigmoid')
  model.fit (data_train, classes_train)

  # Test model
  predictions_train = model.predict (data_train)
  predictions_test = model.predict (data_test)

  # Print errors
  error_train_values[i] = float(len(find(predictions_train != classes_train)))/float(len(classes_train))
  error_test_values[i]  = float(len(find(predictions_test != classes_test)))/float(len(classes_test))

semilogx (C_values, error_test_values, color=colors[-2], linewidth=3.0, label="Sigmoid Kernel")

for i in range(len(C_values)):
  C = C_values[i]
  print "  --> Linear, C = {0}".format (C)

  # Train SVM
  model = svm.SVC (C=C, kernel='linear')
  model.fit (data_train, classes_train)

  # Test model
  predictions_train = model.predict (data_train)
  predictions_test = model.predict (data_test)

  # Print errors
  error_train_values[i] = float(len(find(predictions_train != classes_train)))/float(len(classes_train))
  error_test_values[i]  = float(len(find(predictions_test != classes_test)))/float(len(classes_test))

semilogx (C_values, error_test_values, color=colors[-1], linewidth=3.0, label="Linear Kernel")

legend()
title ("Classification Error for all kernels")
ylabel ("Classification Error (%)")
xlabel ("C")
show()
