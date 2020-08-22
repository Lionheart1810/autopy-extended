import autopy
import time

def move(curve, time_target, time_scale=(lambda x : 1 * x)):
	start = time.time()
	delta = 0
	while(delta < time_target):
		point = curve.point(time_scale(delta), time_target)
		autopy.mouse.move(point[0], point[1])
		delta = time.time() - start
