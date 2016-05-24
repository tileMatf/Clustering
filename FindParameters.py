import Point
import math
import ConditionalProbability

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

  Parameters=[a, b]
  print(Parameters[0:2])
  return Parameters
  
#MStep algorithm, soft clustering
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
    
  a=a1/a2
  b=b1/b2
  Parameters[0]=round(a, 2)
  Parameters[1]=round(b, 2)
 # print Parameters
  return Parameters



#example  
#HiddenVector=[1, 0, 0, 1, 0]
#Data=[0.4, 0.9, 0.8, 0.3, 0.7]
#Parameters=[0.6, 0.83]
#allShows=10


#Parameters=FindParameters(HiddenVector, Data)  
#print Parameters
#HiddenMatrix=ConditionalProbability.EStep(Parameters, Data, allShows)
#for i in HiddenMatrix:
#  print i
#Parameters=MStep(HiddenMatrix, Data)
#print Parameters
