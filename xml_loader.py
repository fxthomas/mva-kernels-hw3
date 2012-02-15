#!/usr/bin/python
# coding=utf-8

# Base Python File (xml_loader.py)
# Created: Mon Feb 13 20:03:28 2012
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
# 
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>

from xml.dom.minidom import parse
import numpy as np
from numpy import *
from scipy import *
from pylab import *
from scipy.interpolate import interp1d

touch_count = 30

def load (fname, resolution=touch_count):
  touch_resolution = 1./float(resolution)
  dom = parse (open (fname))
  records = dom.getElementsByTagName("record")
  characters = []
  symbols = []
  symbol_index = 0
  symbol_cache = {}

  for record in records:
    print "Processing index {0}".format (record.getAttribute ("common_id"))

    # Get an integer identifying the symbol
    symbol = record.getAttribute ("symbol")
    if symbol in symbol_cache:
      symbols.append (symbol_cache[symbol])
    else:
      symbols.append (symbol_index)
      symbol_cache[symbol] = symbol_index
      symbol_index = symbol_index + 1

    # Get list of touches
    moves = record.getElementsByTagName("move")
    print (" --> Found {0} moves".format (len (moves)))

    # Arrange touches into distance, angle and touched? lists
    distance = []
    angle = []
    touched = []
    last_distance = 0
    last_angle = 0.
    pi = 3.1415926524
    for move in moves:
      # Check if the distance if >0, else the interpolation will deviate badly
      _cd = float (move.getAttribute ("distance"))
      if _cd == 0 or last_distance > _cd:
        continue
      _ca = float (move.getAttribute ("angle"))
      _dc1 = last_angle - _ca
      _dc2 = last_angle - (_ca + 2*pi)
      _dc3 = last_angle - (_ca - 2*pi)
      _dci = argmin ((_dc1, _dc2, _dc3))
      if _dci == 1:
        _ca = _ca + 2*pi
      elif dci == 2:
        _ca = _ca - 2*pi

      distance.append (_cd)
      angle.append (_ca)
      touched.append (float(move.getAttribute ("touch")))

    # Convert sequences to numpy arrays
    distance = array(distance)
    angle = array (angle)
    touched = array (touched)

    # Interpolate to only have unitary distances
    distance = cumsum(distance)-distance[0]
    distance = distance/max(distance)
    print distance
    fangle = interp1d (distance, angle, kind='linear', fill_value=0)
    data = mod (fangle (arange (0., 1., touch_resolution)), 2*pi)

    # Save data
    characters.append (data)

  return array(characters), array(symbols)
