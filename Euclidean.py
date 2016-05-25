import Point
import math

#Compute Euclidean distance between points Point1 and Point2
def EuclideanDistance(Point1, Point2):
	distance = 0
	for i in range(0, len(Point1.coord)):
		distance += pow((Point1.coord[i]-Point2.coord[i]), 2)
	distance = math.sqrt(distance)
	return distance
	