import numpy as np
from AutopyExtended.Curve.Curve import Curve

class CurveLinear(Curve):
	def __init__(self, start, end):
		self.__start = np.array(start)
		self.__end = np.array(end)
	def point(self, t, t_target):
		d = np.subtract(self.__end, self.__start)
		return np.add(self.__start, (round(d[0] * t / t_target), round(d[1] * t / t_target)))
