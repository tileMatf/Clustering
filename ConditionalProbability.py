import Point
import math
import random
import FarthestFirstTraversal
import Euclidean 

#from Data, and Parameters we count conditionl probability
def ConditionalProbability(Parameters, Data, allShows):

	HiddenVector=[]
	for i in range (0, len(Data)):
		HiddenVector.append([])
 
	for k in range (0, len(Data)):
		a=pow(Parameters[0],allShows*Data[k])*pow(1-Parameters[0],allShows*(1-Data[k]))
		b=pow(Parameters[1],allShows*Data[k])*pow(1-Parameters[1],allShows*(1-Data[k]))
		if(a>b):
			HiddenVector[k]=1
		else :
			HiddenVector[k]=0
 
	#print(HiddenVector)
	return HiddenVector

  
#Coin filpping algorithm
#expextation maximization
def EStep(Parameters, Data, allShows):
	w, h =len(Data), 2
	matrix = [[1 for x in range(w)] for y in range(h)] 
  
	#for i in matrix:
	#	print (i)  
 
	for k in range (0, len(Data)):
		#print(Parameters[0], allShows, Data[k], pow(Parameters[0],allShows*Data[k]), pow(1-Parameters[0],allShows*(1-Data[k])))
		pom1=pow(Parameters[0],allShows*Data[k]) * pow(1-Parameters[0],allShows*(1-Data[k]))
		pom2=pow(Parameters[1],allShows*Data[k]) * pow(1-Parameters[1],allShows*(1-Data[k]))
		#print("pomocne", pom1, pom2, Parameters[0], Parameters[1], allShows)
		a=round(pom1/(pom1+pom2), 2)
		b=round(pom2/(pom1+pom2), 2)
		#print(a, b)
		matrix[0][k]=a
		matrix[1][k]=b
    
	#for i in matrix:
	#	print (i)
  
	return matrix  


#soft k means clustering
#centers to soft clusters
#Centers, Data > responsibility matrix	
def PartitionFunction(Parameters, Data):
	b=1
	k, n =len(Parameters), len(Data)
	matrix = [[0 for x in range(n)] for y in range(k)]	
	
	sum=[]
	for i in range(0, k):
		sum.append([])
	
	for i in range(0, k):
		sum[i]=0
		for j in range(0, n):
			exp=-b*Euclidean.EuclideanDistance(Data[j], Parameters[i])
			temp=pow(2.718, exp)
			sum[i]=sum[i]+temp
			#print(i, sum[i])
	#print("SUM: ", sum)	
	
	for i in range(0, k):
		for j in range(0, n):
			exp=-b*Euclidean.EuclideanDistance(Data[j], Parameters[i])
			temp=pow(2.718, exp)
			#print(sum[i], exp, temp)	
			matrix[i][j]=round(temp/sum[i], 1)
	
	#for i in matrix:
	#	print ( i)
		
	return matrix	
		
  
a = Point.Point([1,2])
b = Point.Point([6,8])
c = Point.Point([3,4])
d = Point.Point([5,6])
e = Point.Point([5,2])
Data = [a,b,c,d,e, a]		


#example1	
#Parameters=RandomParameters(3, len(Data[0].coord))	
#for i in range(0, len(Parameters)):
#		print ("_", Parameters[i].coord)
#PartitionFunction(Parameters, Data) 


#example2
#Parameters=[0.6, 0.83]
#Data=[0.4, 0.9, 0.8, 0.3, 0.7]
#allShows=10
#ConditionalProbability(Parameters, Data, allShows)
#EStep(Parameters, Data, allShows)



