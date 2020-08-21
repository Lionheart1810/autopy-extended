import numpy as np

from Curve import Curve
from scipy.special import comb

class CurveBezier(Curve):
	def __init__(self, cp, tn):
		self.__tn = tn
		x = np.array([p[0] for p in cp])
		y = np.array([p[1] for p in cp])
		t = np.linspace(0, 1, tn)
		poly = np.array([CurveBezier.bernstein(i, len(cp) - 1, t) for i in range(0, len(cp))])
		self.__x = np.dot(x, poly)
		self.__y = np.dot(y, poly)

	def point(self, t, t_target=None):
		if(t_target == None):
			t_target = self.__tn
		if(t_target != self.__tn):
			raise ValueError("t_target must be equal to tn.")
		return (self.__x[t], self.__y[t])

	@staticmethod
	def bernstein(i, n, t):
		return comb(n, i) * (t ** (n - i)) * (1 - t) ** i
