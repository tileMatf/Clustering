import Point 
import Euclidean
import copy
import math
import WeightedChoice
import Print
import Input

# Compute the probability of selection points for random choice 
# based on square distance from centers
def PointChoiceProbability(Points, Centers):
	PointsProbability = []
	for i in range(0, len(Points)):
		distance = Euclidean.AvarageDistance(Points[i], Centers)
		PointsProbability.append(math.pow(distance, 2))
	return PointsProbability

	
# Return k centers from data Points;
# first point is selected randomly or by user
# and other is selected randomly with probability proportional 
# to square distance from Centers
def KMeansInitializer(Points, k):
	Points_copy = copy.deepcopy(Points)
	firstPointIndex = Input.EnterFirstCenter(Points_copy)
	Centers = [Points[firstPointIndex]]
	del Points_copy[firstPointIndex]
	PointsProbability = []
	while len(Centers) < k:
		del PointsProbability[:]
		PointsProbability = PointChoiceProbability(Points_copy, Centers)
		newPointIndex = WeightedChoice.WeightedChoice(PointsProbability)
		Centers.append(Points_copy[newPointIndex])
		del Points_copy[newPointIndex]
		
	#print("\nCenters:")
	#Print.PrintPoints(Centers)
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
Centers = KMeansInitializer(Points, 3)
Print.PrintPoints(Centers)
"""