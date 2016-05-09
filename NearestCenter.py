import Point 
import Euclidean 

#Return list of 2 elements - nearest center of point Point from Centers 
#and Euclidean distance between them
def NearestCenter(Point, Centers):
	minDistance = Euclidean.EuclideanDistance(Point, Centers[0])
	minDistanceIndex = 0
	for i in range(1, len(Centers)):
		currentDistance = Euclidean.EuclideanDistance(Point, Centers[i])
		if currentDistance < minDistance:
			minDistance = currentDistance
			minDistanceIndex = i
	return [Centers[minDistanceIndex], minDistance]

