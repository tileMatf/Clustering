import Point
import math

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
 
  print(HiddenVector[0:len(HiddenVector)])
  return HiddenVector
  
  
  
#matrixHiddenVector
def EStep(Parameters, Data, allShows):
  w, h =len(Data), 2
  matrix = [[0 for x in range(w)] for y in range(h)] 
  
  for i in matrix:
    print i  
 
  for k in range (0, len(Data)):
    pom1=pow(Parameters[0],allShows*Data[k])*pow(1-Parameters[0],allShows*(1-Data[k]))
    pom2=pow(Parameters[1],allShows*Data[k])*pow(1-Parameters[1],allShows*(1-Data[k]))
    a=round(pom1/(pom1+pom2), 3)
    b=round(pom2/(pom1+pom2), 3)
    matrix[0][k]=a
    matrix[1][k]=b
    
  for i in matrix:
    print i
  
  return matrix  
  
#example
Parameters=[0.6, 0.83]
Data=[0.4, 0.9, 0.8, 0.3, 0.7]
allShows=10
ConditionalProbability(Parameters, Data, allShows)
ConditionalProbabilityMatrix(Parameters, Data, allShows)
