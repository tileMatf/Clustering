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
			randCoord = round(random.randint(0,9) + random.random(), 1);
			newParameter.coord.append(randCoord)
		if FarthestFirstTraversal.PointNotInCenters(newParameter, Parameters):
			Parameters.append(newParameter)

	return Parameters
	

	
#####___partition function Lloyd soft alg
def CentersToClustersSoft(Parameters, Data, MatrixR):
	
	change = 0
	k, n =len(Parameters), len(Data)
	matrix = [[0 for x in range(n)] for y in range(k)]	
	#for i in matrix:
	#	print (i)
		
	matrix=ConditionalProbability.PartitionFunction(Parameters, Data)	
	
	for i in range(0, k):
		for j in range (0,n):
			if MatrixR[i][j]!=matrix[i][j] :
				change = 1
	
	for i in range(0, k):
		for j in range (0,n):
			MatrixR[i][j]=matrix[i][j]
	
	for i in MatrixR:
		print (i)
	print()	
  
	return change  

#WeightedCenterOfGravity
#lloyd soft alg
def ClustersToCentersSoft(Parameters, Data, MatrixD):
	#for i in range(0, len(Parameters)):
	#	print("stari", Parameters[i].coord)
	newParameters= FindParameters.WeightedCenterOfGravity(MatrixD, Data)  
	#for i in range(0, len(newParameters)):
	#	print("novi", newParameters[i].coord)
	return newParameters




#soft version of kmeans clustering
def LloydSoft( Data):
	
	k = Input.EnterNumberOfCluster(Data)
	Parameters = RandomParameters(k, len(Data[0].coord))
	k, n =len(Parameters), len(Data)
	matrix = [[0 for x in range(n)] for y in range(k)]
	changeExists = True

	print("\nFirst parameters:");
	Print.PrintPoints(Parameters)

	while changeExists:
		changeExists = CentersToClustersSoft(Parameters, Data, matrix)

		print("CLUSTERS:")
		min1=[]
		for j in range(0,n):
			min1.append([])
			min1[j]=NearestCenter.NearestCenter(Data[j], Parameters)
		for i in range(0,k):
			print("klaster",i,":")
			for j in range(0, n):
				if min1[j][2]==i:
					print(Data[j].coord)

		Parameters= ClustersToCentersSoft(Parameters, Data, matrix)
		print("\nNew Parameters:", end=" ")
		Print.PrintPoints(Parameters)
	
	return matrix


a = Point.Point([1,6])
b = Point.Point([1,3])
c = Point.Point([3,4])
d = Point.Point([5,6])
e = Point.Point([5,2])
f = Point.Point([7,1])
g = Point.Point([8,7])
h = Point.Point([10,3])	
Data = [a,b,c,d,e]

'''
Parameters = RandomParameters(3, len(Data[0].coord))
for i in range(0, len(Parameters)):
	print(Parameters[i].coord)
#LloydHard(Data)
k, n =len(Parameters), len(Data)
matrix = [[0 for x in range(n)] for y in range(k)]
CentersToClustersSoft(Parameters, Data, matrix)

ClustersToCentersSoft(Parameters, Data, matrix)
'''
LloydSoft(Data)