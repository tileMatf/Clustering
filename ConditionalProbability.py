import Point
import math

#from Data, and Parameters we count conditionl probability
def ConditionalProbability(Parameters, Data):

  HiddenVector=[]
  for i in range (0, len(Data)):
    HiddenVector.append([])
 
  for k in range (0, len(Data)):
    a=pow(Parameters[0],Data[k])*pow(1-Parameters[0],(1-Data[k]))
    b=pow(Parameters[1],Data[k])*pow(1-Parameters[1],(1-Data[k]))
    if(a>b):
      HiddenVector[k]=1
    else :
      HiddenVector[k]=0
 
  print(HiddenVector[0:len(HiddenVector)])

#example
Parameters=[0.6, 0.83]
Data=[0.4, 0.9, 0.8, 0.3, 0.7]

ConditionalProbability(Parameters, Data)
