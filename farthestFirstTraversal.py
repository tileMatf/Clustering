import random
import math
import Point

#Test if two point is equal
def EqualPoints(Point1, Point2):
    for i in range(0, len(Point1.coord)):
        if Point1.coord[i] != Point2.coord[i]:
            return False
    return True

#Test if point Point is in Centers
def PointNotInCenters(Point, Centers):
    for i in range(0, len(Centers)):
        for j in range(0, len(Centers[i].coord)):
            if EqualPoints(Point, Centers[i]) == True:
                return False
    return True

#Compute Euclidean distance between points Point1 and Point2
def EuclideanDistance(Point1, Point2):
	distance = 0
	for i in range(0, len(Point1.coord)):
		distance += pow((Point1.coord[i]-Point2.coord[i]), 2)
	distance = round(math.sqrt(distance),2)
	return distance

#Print list of points in readable form	
def PrintPoints(Points):	
	print()
	for i in range(0, len(Points)):
		if i != len(Points) - 1:
			print(Points[i].coord, end=", ")
		else:
			print(Points[i].coord)
			print()

#Asks the user to define first point to be the first center
def EnterFirstCenter(Points):
	answer = ""
	firstPointIndex = -1
	outOfRange = False
	
	while ((answer != "yes" and answer != "no") or outOfRange):
		
		answer = input("Whether you prefer to define the initial point? (type yes or no) ");
		
		if answer == "no": 
			firstPointIndex = random.randint(0, len(Points)-1)
		elif answer == "yes":
			PrintPoints(Points)
			try:
				firstPointIndex = int(input("Type index of initial point from list above: "))-1
			except ValueError:
				print("Index is not a integer, try again.")
				outOfRange = True
				continue
			if firstPointIndex not in range(0, len(Points)):
				print("Index out of range, try again.");
				outOfRange = True
			else:
				outOfRange = False
		else:
			print("You didn't enter neither yes neither no, try again.")
	return firstPointIndex
		
#Return k centers from Points
#In every iteration select point from Points which maximizing
#distance between current centers and other points from Points
def FarthestFirstTraversal(Points, k):
	
	firstPointIndex = EnterFirstCenter(Points)
	Centers = [Points[firstPointIndex]]
	#print ("First point: " + str(Points[firstPointIndex].coord))
	
	while len(Centers) < k:
		currentDistance = 0
		maxDistance = 0
		maxDistanceIndex = -1
		for i in range(0, len(Centers)):
			for j in range(0, len(Points)):
				currentDistance = EuclideanDistance(Centers[i], Points[j])
				if PointNotInCenters(Points[j], Centers) and currentDistance > maxDistance:
					maxDistance = currentDistance
					maxDistanceIndex = j
		Centers.append(Points[maxDistanceIndex])
	return Centers
				

#Example
a = Point.Point([1,6])
b = Point.Point([1,3])
c = Point.Point([3,4])
d = Point.Point([5,6])
e = Point.Point([5,2])
f = Point.Point([7,1])
g = Point.Point([8,7])
h = Point.Point([10,3])

Points = [a, b, c, d,e,f,g,h]
Centers = FarthestFirstTraversal(Points, 3)
PrintPoints(Centers)
