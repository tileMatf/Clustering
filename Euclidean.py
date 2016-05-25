import Point
import math

#Compute Euclidean distance between points Point1 and Point2
def EuclideanDistance(Point1, Point2):
	distance = 0
	for i in range(0, len(Point1.coord)):
		distance += pow((Point1.coord[i]-Point2.coord[i]), 2)
	distance = math.sqrt(distance)
	return distance
	

#Compute avarage distance between point Point and all centers from Centers
def AvarageDistance(Point, Centers):
	distance = 0;
	
	for i in range(0, len(Centers)):
		distance += EuclideanDistance(Point, Centers[i])
	
	distance = distance * 1.0 / len(Centers);
	return distance
	

	