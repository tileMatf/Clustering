import Point
import random
import math
import ConditionalProbability
import FindParameters
import FarthestFirstTraversal
import Print
import time
import copy
import NearestCenter
import Euclidean
import Input

#Initialize k random parameters as points in m dimensional space in range [0.00, 9.99]
def RandomParameters(k, m):
	
	Parameters = []
	
	while (len(Parameters) < k):
		newParameter = Point.Point([])
		for i in range(0, m):
			random.seed(time.time()+k%(i+1))
			randCoord = round(random.randint(0,9) + random.random(), 2);
			newParameter.coord.append(randCoord)
		if FarthestFirstTraversal.PointNotInCenters(newParameter, Parameters):
			Parameters.append(newParameter)

	return Parameters

#E-Step transition
def CentersToClustersHard(Parameters, Data, HiddenVector):
	
	change = False
	newVector = []
	n = len(Data)
	
	for i in range(0, n):
		nearestCenter = NearestCenter.NearestCenter(Data[i], Parameters)
		newVector.append(nearestCenter[2]) 
  
	#if there is some change return true
	for i in range(0, n): 
		if(HiddenVector[i] != newVector[i]):
			change = True
	  
	#new HiddenVector            
	del HiddenVector[:]
	for i in range(0, n):
		HiddenVector.append(newVector[i])
  
	#print Matrix
	print("New hidden vector:")
	print(HiddenVector)
  
	return change  

#Compute new center of clusters as points which coordinates is avarage value of coordinates
#of points which is in the same cluster 
def ClustersToCentersHard(Parameters, Data, HiddenVector):

	spaceDim = len(Data[0].coord)
	Parameters_copy = copy.deepcopy(Parameters)
	del Parameters[:]
	
	for i in range(0, len(Parameters_copy)):
		newCenterCoords = []
		for k in range(0, spaceDim):
			sum = 0
			total = 0
			for j in range(0, len(HiddenVector)):
				if HiddenVector[j] == i:
					sum += Data[j].coord[k]
					total += 1
			if total != 0:
				newCenterCoords.append(round(sum/total, 2))
		if total == 0:
			newCenterCoords = Parameters_copy[i].coord	

		Parameters.append(Point.Point(newCenterCoords))


#Hard version of kmeans clustering		
def LloydHard(Data):
  
	k = Input.EnterNumberOfCluster(Data);
	Parameters = RandomParameters(k, len(Data[0].coord))
	vector = []
	for i in range(0, len(Data)):
		vector.append(0)
	changeExists = True
	
	print("\nFirst parameters:");
	Print.PrintPoints(Parameters)
	
	while changeExists:
		changeExists = CentersToClustersHard(Parameters, Data, vector)
		Print.PrintClustersThrowVector(Data, vector, k)
		ClustersToCentersHard(Parameters, Data, vector)
		print("\nNew Parameters:")
		Print.PrintPoints(Parameters)
	
	return vector

a = Point.Point([1,6])
b = Point.Point([1,3])
c = Point.Point([3,4])
d = Point.Point([5,6])
e = Point.Point([5,2])
f = Point.Point([7,1])
g = Point.Point([8,7])
h = Point.Point([10,3])
	
Data = [a,b,c,d,e,f,g,h]
#Data=[0.4, 0.9, 0.8, 0.3, 0.7]

LloydHard(Data)

