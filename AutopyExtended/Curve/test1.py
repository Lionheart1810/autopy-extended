import matplotlib.pyplot as plot
from CurveBezier import CurveBezier

curve = CurveBezier([(0,0),(53,178),(5,87),(140,75),(48,647),(37,49)],1000)
points = [curve.point(t) for t in range(0,1000)]
x = [p[0] for p in points]
y = [p[1] for p in points]
plot.scatter(x,y)
plot.show()
