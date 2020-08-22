from AutopyExtended.Curve.Bezier import CurveBezier
import AutopyExtended.mouse as mouse

curve = CurveBezier([(0,0),(53,178),(5,87),(140,75),(48,647),(37,49)],1000)
mouse.move(curve, 1)
