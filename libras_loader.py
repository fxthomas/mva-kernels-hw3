#!/usr/bin/python
# coding=utf-8

# Base Python File (libras_loader.py)
# Created: Sun Feb 12 15:33:10 2012
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
# 
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>

from numpy import append,array


def load (fname):
  data = None
  classes = []
  for l in open (fname):
    la = map (float, l.strip("\r\n ").split(","))
    la_data = array (la[0:90]).reshape ((1,90))
    la_class = la[-1]

    if data is None:
      data = la_data
      classes.append (la_class)
    else:
      data = append (data, la_data, axis=0)
      classes.append (la_class)

  return data, array(classes)
