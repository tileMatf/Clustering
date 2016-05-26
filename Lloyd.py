import Point
import random
import copy
import Print
import NearestCenter
import FarthestFirstTraversal
import Input
import KMeansInitializer

#return index of Cluster in which was point 
def PreviousCluster(point, Clusters):
	for i in range(0, len(Clusters)):
		if point in Clusters[i]:
			return i
	return -1

#return k random points from Points
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

#Arrange points from Points in to cluster which
#center is nearest to certain point
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

#Compute new centers of clusters as center gravity point
#i-th coordinate of center is avarage value of all i-th coordinates of points
#from same cluster
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
		
#Randomly selected k center from Points and iterate throw 2 steps:
#Arrange points to nearest center, and than compute new center until
#no more changes between clusters
def Lloyd(Points):

	k = Input.EnterNumberOfCluster(Points);
	answer = Input.EnterTypeOfChoiseOfFirstCenter();
	if answer == "r":
		Centers = RandomCenters(Points, k)
	elif answer == "p":
		Centers = KMeansInitializer.KMeansInitializer(Points, k);
		
	print("\nFirst centers:");
	Print.PrintPoints(Centers)
	Clusters = []
	changeExists = True
	
	while changeExists:
		changeExists = CentersToClusters(Points, Centers, Clusters)
		Print.PrintClusters(Clusters)
		ClustersToCenters(Centers, Clusters)
		print("\nnew Centers:")
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

Clusters = Lloyd(Points)
