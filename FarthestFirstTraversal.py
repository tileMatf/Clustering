import random
import math
import Point
import Euclidean
import Print
import Input

#Test if two point is equal
def EqualPoints(Point1, Point2):
    for i in range(0, len(Point1.coord)):
        if Point1.coord[i] != Point2.coord[i]:
            return False
    return True

#Test if point Point is in Centers
def PointNotInCenters(Point, Centers):
    for i in range(0, len(Centers)):
        if EqualPoints(Point, Centers[i]) == True:
            return False
    return True

		
#Return k centers from Points
#In every iteration select point from Points which maximizing
#distance between current centers and other points from Points
#Point with max distance is calculating as avarage distance between 
#point and every center that is selected till now 
def FarthestFirstTraversal(Points, k):
	
	firstPointIndex = Input.EnterFirstCenter(Points)
	Centers = [Points[firstPointIndex]]
	#print ("First point: " + str(Points[firstPointIndex].coord))
	
	while len(Centers) < k:
		currentDistance = 0
		maxDistance = 0
		maxDistanceIndex = -1
		for j in range(0, len(Points)):
			for i in range(0, len(Centers)):
				currentDistance += Euclidean.EuclideanDistance(Centers[i], Points[j])
			currentDistance = currentDistance / len(Centers);
			if PointNotInCenters(Points[j], Centers) and currentDistance > maxDistance:
				maxDistance = currentDistance
				maxDistanceIndex = j
		Centers.append(Points[maxDistanceIndex])
	print("Centers: ")
	Print.PrintPoints(Centers)
	return Centers

"""
a = Point.Point([1,6])
b = Point.Point([1,3])
c = Point.Point([3,4])
d = Point.Point([5,6])
e = Point.Point([5,2])
f = Point.Point([7,1])
g = Point.Point([8,7])
h = Point.Point([10,3])

Points = [a, b, c, d, e, f, g, h]
Centers = FarthestFirstTraversal(Points, 3)
"""