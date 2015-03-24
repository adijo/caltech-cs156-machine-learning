"""
Utilities for learning algorithms
"""

class Line(object):
	"""Abstraction of a line."""

	def __init__(self):
		self.line = self.generateLine()
		self.slope, self.intercept = self.line[0], self.line[1]
		

	def generateLine(self):
		""" 
		Returns the slope and intercept of a randomly 
		generated line
		"""
		# Uniformly select two points in the interval [-1, 1] 
		x_1, y_1 = random.uniform(NEGATIVE, POSITIVE) , random.uniform(NEGATIVE, POSITIVE)
		x_2, y_2 = random.uniform(NEGATIVE, POSITIVE) , random.uniform(NEGATIVE, POSITIVE)
		a = np.array([[x_1, 1], [x_2, 1]])
		b = np.array([y_1, y_2])
		soln = np.linalg.solve(a, b)
		return soln

	def classify(self, x, y):
		"""
		Input: x and y co-ordinate
		Output: 
		  +1 if the point is to the right
		  -1 if the point is to the left
		  0 if point is on the line. (Highly unlikely)
		"""
		x_line = (y - self.intercept) / float(self.slope)
		if x > x_line:
		    return 1
		elif x < x_line:
		    return -1
		else:
		    return 0