#!/usr/bin/python
# coding=utf-8

# Base Python File (svm_pca.py)
# Created: Mon Feb 13 13:48:14 2012
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
from sklearn.decomposition import pca
from matplotlib.colors import rgb2hex

print "Loading data..."
data, classes = libras_loader.load ("data/movement_libras.data")
error_train = 0.
error_test = 0.
nb_tests = 20
train_ratio = 0.8
train_count = int(train_ratio * len (data))
out_size = 1000

# Randomly sample data vectors
print "Randomizing samples..."
_per = np.random.permutation(len(data))
_ds = data[_per, :]
_cs = classes[_per]
data_train    = _ds[:train_count,:]
data_test     = _ds[train_count:,:]
classes_train = _cs[:train_count]
classes_test  = _cs[train_count:]

C = 5.
gamma = 0.7

# Train SVM
print "Training SVM..."
model = svm.SVC (C=C, gamma=gamma, kernel='rbf')
model.fit (data_train, classes_train)

# Compute the first 2 components of the PCA
print "Computing PCA..."
components = pca.PCA (n_components=2)
components.fit (data_train)

# Compute min/max over the 2 axes
print "Computing decision function..."
print " --> Transform data"
transformed_data = components.transform (data_train)
dmin = np.min(transformed_data, axis=0)
dmax = np.max(transformed_data, axis=0)

# Create mesh grid from min to max
print " --> Mesh grid ({0}x{0})".format (out_size)
x = arange (dmin[0], dmax[0], (dmax[0]-dmin[0])/float(out_size))
y = arange (dmin[1], dmax[1], (dmax[1]-dmin[1])/float(out_size))
xx,yy = meshgrid (x, y)

# Create a list of vectors from PCA components
print " --> Mesh vectors"
nda = np.rollaxis(array ([xx,yy]), 0, 3).reshape (out_size*out_size, 2)
pp = components.inverse_transform(nda)

# Compute predicted classes for each vector
print " --> Mesh prediction"
pr = model.predict (pp).reshape ((1000, 1000))

# Show the predicted classes
print "Displaying decision function..."
print " --> Classes"
imshow (pr, extent=[dmin[0],dmax[0], dmin[1],dmax[1]], cmap=get_cmap('jet'))

# Add scatter plots for the class data
print " --> Data overlay"
for c in unique(classes):
    cid = find(classes_train == c)
    dd = transformed_data[cid, :]
    scatter (dd[:,0], dd[:,1], color=get_cmap('jet')(c/max(unique(classes_train))))

# Show plot
print " --> Finalizing"
title ("Class prediction for the first 2 components of the PCA")
show()

print "Done!"
