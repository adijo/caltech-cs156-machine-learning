"""
Implementation of the perceptron learning
algorithm described in the ML course offered by
Yaser Abu-Mostafa from Caltech. 
"""

# Imports

import numpy as np
import random
from utils import Line

# Globals

NEGATIVE = -1.0
POSITIVE = 1.0
SAMPLE_POINTS = 1000
ITERATIONS = 100


def sample(n, line):
	"""
	Returns a list of n points (3 D vectors)
	with a classification label
	"""
	dataset = []
	for i in xrange(n):
		x = random.uniform(NEGATIVE, POSITIVE)
		y = random.uniform(NEGATIVE, POSITIVE)
		label = line.classify(x, y)
		vector = np.array([1, x, y])
		dataset.append((vector, label))
	return dataset

def trainingFunction(weight, vector):
	"""
	Takes an input weight vector and point vector
	Finds the dot product and reports the -1 if dot product
	is negative, else 1. 0 case is unlikely, so currently classified 
	as 1. Add support later if causing erronous results
	"""
	dotProduct = weight.dot(vector)
	if dotProduct < 0:
		return -1
	else:
		return 1



def train(iterations, dataset):
	"""
	Trains the model by running 
	'iterations' number of iterations 
	with the input dataset
	and returns a weight vector
	"""
	weight = np.array([0, 0, 0])
	correct = []
	incorrect = []
	
	# Initial classification.
	for data in dataset:
		vector = data[0]
		label = data[1]
		if trainingFunction(weight, vector) != label:
			incorrect.append(data)
		else:
			correct.append(data)
	total = float(len(incorrect) + len(correct))
	print "\n"
	print "Total points: (before training)", total
	print "Correct classification: (before training)", 100 * (len(correct) / total), "%"
	print "Incorrect classification: (before training)", 100 * (len(incorrect) / total), "%"
	print "\n"
	for i in range(iterations):
		if len(incorrect) == 0:
			print "Total points:", SAMPLE_POINTS
			print "Correct classification:", "100.0", "%"
			print "Incorrect classification:", "0.0", "%"
			return weight # We are done, classified all points correctly.
		else:
			randomDataPoint = random.choice(incorrect)
			vector = randomDataPoint[0]
			label = randomDataPoint[1]

			# Update weight vector.
			newCorrect = []
			newIncorrect = []
			weight = weight + (label * vector)
			for data in correct:
				vector = data[0]
				label = data[1] 
				if trainingFunction(weight, vector) != label:
					newIncorrect.append(data)
				else:
					newCorrect.append(data)
			for data in incorrect:
				vector = data[0] 
				label = data[1] 
				if trainingFunction(weight, vector) != label:
					newIncorrect.append(data)
				else:
					newCorrect.append(data)
		correct = newCorrect
		incorrect = newIncorrect

		
	total = float(len(incorrect) + len(correct))
	print "Total points: ", total
	print "Correct classification: ", 100 * (len(correct) / total), "%"
	print "Incorrect classification: ", 100 * (len(incorrect) / total), "%"
	return weight


line = Line()
dataset = sample(SAMPLE_POINTS, line)
print train(ITERATIONS, dataset)