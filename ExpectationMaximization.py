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
def CentersToClustersSoft(Parameters, Data, HiddenMatrix, allShows):
  change=0
  
  #newHiddenMatrix= [][], initialize newHiddenMatrih
  w, h =len(Data), 2
  matrix = [[0 for x in range(w)] for y in range(h)] 
  matrix=ConditionalProbability.EStep(Parameters, Data, allShows)
  #print Matrix
  #for i in matrix:
  # print i 
  
  #if there is some change return true
  for j in (0, len(Parameters)-1): #0,1
    for i in range (0,len(Data)): #0-4
      if(HiddenMatrix[j][i]!=matrix[j][i]):
        change=1
      
              
  #new HiddenMatrix            
  del HiddenMatrix
  for j in (0, len(Parameters)-1): #0,1
    for i in range (0,len(Data)): #0-4
      HiddenMatrix[j][i]=matrix[j][i]
  
  #print Matrix
  for i in HiddenMatrix:
    print i 
  
  return change  



#M-Step transition
def ClustersToCentersSoft(HiddenMatrix, Data):
  Parameters=FindParameters.MStep(HiddenMatrix, Data)
 # print ("parametri su ", Parameters)
  return Parameters

		
#ExpectationMaximization algorithm 
def ExpectationMaximization(Data, allShows):
  
  Parameters=RandomParameters()
  #matrix[][]
  w, h =len(Data), 2
  matrix = [[0 for x in range(w)] for y in range(h)]
  changeExist=1
  for i in matrix:
      print i
  
  while(changeExist):
    changeExist=CentersToClustersSoft(Parameters, Data, matrix, allShows) 
    print("new HiddenMatrix")
    #print matrix
	  #for i in matrix:
    #  print i
    Parameters=ClustersToCentersSoft(matrix, Data)
    print(" Parameters: ")
    print(Parameters)
    
  return matrix
    
#example    
Data=[0.4, 0.9, 0.8, 0.3, 0.7]
allShows=10
ExpectationMaximization(Data, allShows)
