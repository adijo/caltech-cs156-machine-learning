"""
Implementation of the linear regression
algorithm on non-linear transformations
described in the ML course offered by
Yaser Abu-Mostafa from Caltech. 
"""

# Imports

import numpy as np 
from utils import Line
import random

# Globals

NEGATIVE = -1.0
POSITIVE = 1.0
SAMPLE_POINTS = 1000
ITERATIONS = 100

def sample(n, line):
	"""
	Returns a list of n points (2 D vectors)
	with a classification label
	"""
	data = []
	labels = []
	for i in xrange(n):
		x = random.uniform(NEGATIVE, POSITIVE)
		y = random.uniform(NEGATIVE, POSITIVE)
		label = line.classify(x, y)
		vector = np.array([x, y])
		data.append(vector)
		labels.append(label)
	return np.array(data), np.array(labels)


def addnoise(data):
	"""
	Add noise to 10% of SAMPLE_POINTS
	in the dataset.
	"""
	 