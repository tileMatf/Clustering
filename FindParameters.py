import Point
import math
import random
import ConditionalProbability
import FarthestFirstTraversal

#from Data and HiddenVector, we count Parameters
def FindParameters(HiddenVector, Data):
	n=len(Data);
	
	vector1=[]
	for i in range (0, n):
		vector1.append(1)

	a1, a2, b1, b2=0, 0, 0, 0
	for k in range (0, n):
		a1+=HiddenVector[k]*Data[k]
		a2+=HiddenVector[k]*vector1[k]
		b1+=(vector1[k]-HiddenVector[k])*Data[k]
		b2+=(vector1[k]-HiddenVector[k])*vector1[k]
	if(a2==0):
		a2=1
	if(b2==0):
		b2=1
		
	a=a1/a2
	b=b1/b2

	Parameters=[[], []]
	Parameters[1]=round(b, 2)
	Parameters[0]=round(a, 2)
	#print(Parameters[0:2])
	return Parameters

	
#Coin filpping algorithm
#expextation maximization
#M step alg
#from HiddenMatrih and Data >> Parameters
def MStep(HiddenMatrix, Data):
	Parameters=[[], []]
	n=len(Data)
	vector1=[]
	for i in range (0, n):
		vector1.append(1)
	
	a1, a2, b1, b2=0, 0, 0, 0
	for k in range (0, n):
		a1+=HiddenMatrix[0][k]*Data[k]
		a2+=HiddenMatrix[0][k]*vector1[k]
		b1+=HiddenMatrix[1][k]*Data[k]
		b2+=HiddenMatrix[1][k]*vector1[k]
		
	if(a2==0):
		a2=1
	if(b2==0):
		b2=1
	
	a=a1/a2
	b=b1/b2
	
	Parameters[0]=round(a, 3)
	Parameters[1]=round(b, 3)
 # print (Parameters)
	return Parameters

#soft k means clustering
#clasters to centers soft
#resp matrix, Data > centers
def WeightedCenterOfGravity(MatrixD, Data):  
	n=len(MatrixD)
	k=len(Data)
	
	vector1=[]
	for i in range (0, k):
		vector1.append(1)
	
	
	Parameters=[]
	for i in range(0, n):
		Parameters.append([0,0])
	
	

	for i in range(0, n):
		newCoords= []
		for p in range(0, len(Data[0].coord)):
			up=0
			down=0
			for j in range(0, k):
				#print(i, p, j)
				up=up + MatrixD[i][j]*Data[j].coord[p]
				down=down + MatrixD[i][j]*vector1[j]
			newCoords.append([])
			newCoords[p]=round(up/down, 1)
		#print(i,p)
		#print(newCoords)
		Parameters[i]=(Point.Point(newCoords))

	#for i in range(0, len(Parameters)):
	#	print(Parameters[i].coord)

	return Parameters


		

a = Point.Point([1,2])
b = Point.Point([6,8])
c = Point.Point([3,4])
d = Point.Point([5,6])
e = Point.Point([5,2])
Data = [a,b,c,d,e]		


'''
Parameters=RandomParameters(3, len(Data[0].coord))	
for i in range(0, len(Parameters)):
	print ( Parameters[i].coord)
matrix=ConditionalProbability.PartitionFunction(Parameters, Data) 
for i in matrix:
	print(i)
WeightedCenterOfGravity(matrix, Data)
'''

#example  
#HiddenVector=[1, 0, 0, 1, 0]
#Data=[0.4, 0.9, 0.8, 0.3, 0.7]
#Parameters=[0.6, 0.83]
#allShows=10
#Parameters=FindParameters(HiddenVector, Data)  
#print (Parameters)
#HiddenMatrix=ConditionalProbability.EStep(Parameters, Data, allShows)
#for i in HiddenMatrix:
#  print (i)
#Parameters=MStep(HiddenMatrix, Data)
#print (Parameters)
