import Point
import random
import math
import ConditionalProbability
import FindParameters


#initialize random parameters in range [0.00, 1.00 ]
def RandomParameters():
  a=round(random.random(), 2)
  b=round(random.random(), 2)
  Parameters=[a, b]
  print("rand par", Parameters[:])
  return Parameters



#E-Step transition
def CentersToClustersHard(Parameters, Data, HiddenVector, allShows):
  change=0

  newVector = []
  k=len(Data)
	
  for i in range(0, k):
    newVector.append([])
  
  newVector=ConditionalProbability.ConditionalProbability(Parameters, Data, allShows)
  
  #if there is some change return true
  for j in (0, k-1): 
      if(HiddenVector[j]!=newVector[j]):
        change=1
      
              
  #new HiddenVector            
  del HiddenVector
  for i in range (0,k): #0-4
      HiddenVector[i]=newVector[i]
  
  #print Matrix
  print(HiddenVector)
  
  return change  



#
def ClustersToCentersHard(HiddenVector, Data):
  Parameters=FindParameters.FindParameters(HiddenVector, Data)
 # print ("parametri su ", Parameters)
  return Parameters



#hard version of kmeans clustering		
def LloydHard(Data, allShows):
  
  Parameters=RandomParameters()
  vector = []
  changeExist=1
  for i in range(0, len(Data)):
    vector.append(0)
  print(vector)
  
  while(changeExist):
    print("new HiddenMatrix, Parameters:")
    changeExist=CentersToClustersHard(Parameters, Data, vector, allShows) 
    Parameters=ClustersToCentersHard(vector, Data)
    
  return vector
	

Data=[0.4, 0.9, 0.8, 0.3, 0.7]
#Parameters=[0.6, 0.83]
allShows=10
LloydHard(Data, allShows)
