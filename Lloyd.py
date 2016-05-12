import Point
import random
import copy
import Print
import NearestCenter
import FarthestFirstTraversal

def PreviousCluster(point, Clusters):
	for i in range(0, len(Clusters)):
		if point in Clusters[i]:
			return i
	return -1

def RandomCenters(Points, k):
	Centers = []
	Indices = []
	randIndex = -1
	while k > 0:
		randIndex = random.randint(0, len(Points)-1)
		while randIndex in Indices:
			randIndex = random.randint(0, len(Points)-1)
		Indices.append(randIndex)
		Centers.append(Points[randIndex])
		k = k - 1
	return Centers

def CentersToClusters(Points, Centers, Clusters):
	change = False
	
	newClusters = []
	k = len(Centers)
	
	for i in range(0, k):
		newClusters.append([])
		
	for i in range(0, len(Points)):	
		nearestCenter = NearestCenter.NearestCenter(Points[i], Centers)
		for j in range(0, len(Centers)):
			if FarthestFirstTraversal.EqualPoints(nearestCenter[0], Centers[j]):
				newClusters[j].append(Points[i])
				#print("Point " + str(Points[i].coord) + " add to cluster " + str(j+1))
				#print("Previous cluster of point " + str(Points[i].coord) + " is " + str(PreviousCluster(Points[i], Clusters)))
				if j != PreviousCluster(Points[i], Clusters):
					change = True
	del Clusters[:]
	for i in range(0, len(newClusters)):
		Clusters.append(newClusters[i])
	return change

def ClustersToCenters(Centers, Clusters):
	
	spaceDim = len(Centers[0].coord)
	del Centers[:]
	
	for i in range(0, len(Clusters)):
		sum = 0
		newCenterCoords = []
		#print("For cluster: ")
		#Print.PrintPoints(Clusters[i])
		for k in range(0, spaceDim):
			sum = 0
			for j in range(0, len(Clusters[i])):
				sum += Clusters[i][j].coord[k]
			newCenterCoords.append(sum/len(Clusters[i]))
		#print(newCenterCoords)
		Centers.append(Point.Point(newCenterCoords))
		
def Lloyd(Points, k):
	
	Centers = RandomCenters(Points, k)
	print("First centers:");
	Print.PrintPoints(Centers)
	Clusters = []
	changeExists = True
	
	while changeExists:
		changeExists = CentersToClusters(Points, Centers, Clusters)
		Print.PrintClusters(Clusters)
		ClustersToCenters(Centers, Clusters)
		print("new Centers:")
		Print.PrintPoints(Centers)
	return Clusters
	

a = Point.Point([1,6])
b = Point.Point([1,3])
c = Point.Point([3,4])
d = Point.Point([5,6])
e = Point.Point([5,2])
f = Point.Point([7,1])
g = Point.Point([8,7])
h = Point.Point([10,3])
	
Points = [a,b,c,d,e,f,g,h]
#Centers = [a, d, e ,g]
#Clusters = [[a,b], [c,d], [e,f], [g,h]]
#Print.PrintClusters(Clusters)

Clusters = Lloyd(Points, 4)
