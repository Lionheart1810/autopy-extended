import numpy as np

from AutopyExtended.Curve.Curve import Curve
from scipy.special import comb

class CurveBezier(Curve):
	def __init__(self, cp, tn):
		self.__tn = tn
		x = np.array([p[0] for p in cp])
		y = np.array([p[1] for p in cp])
		t = np.linspace(0, 1, tn)
		poly = np.array([CurveBezier.bernstein(i, len(cp) - 1, t) for i in range(0, len(cp))])
		self.__x = np.flip(np.dot(x, poly))
		self.__y = np.flip(np.dot(y, poly))

	def point(self, t, t_target):
		t_scaled = min([t * self.__tn / t_target, self.__tn - 1])
		return np.add((self.__x[int(np.floor(t_scaled))], self.__y[int(np.floor(t_scaled))]), 
			np.subtract((self.__x[int(np.ceil(t_scaled))], self.__y[int(np.ceil(t_scaled))]), 
				(self.__x[int(np.floor(t_scaled))], self.__y[int(np.floor(t_scaled))])) * (t_scaled - np.floor(t_scaled)))

	@staticmethod
	def bernstein(i, n, t):
		return comb(n, i) * (t ** (n - i)) * (1 - t) ** i
