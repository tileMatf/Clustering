import Point

#from Data and HiddenVector, we count Parameters
def FindParameters(HiddenVector, Data):
  n=len(Data);
  
  vector1=[]
  for i in range (0, len(Data)):
    vector1.append(1)
  
  a1=0
  a2=0
  b1=0
  b2=0
  
  for k in range (0, n):
    a1+=HiddenVector[k]*Data[k]
    a2+=HiddenVector[k]*vector1[k]
    b1+=(vector1[k]-HiddenVector[k])*Data[k]
    b2+=(vector1[k]-HiddenVector[k])*vector1[k]
    
  a=a1/a2
  b=b1/b2

  Parameters=[a, b]

  print(Parameters[0:2])

#example  
HiddenVector=[1, 0, 0, 1, 0]
Data=[0.4, 0.9, 0.8, 0.3, 0.7]

FindParameters(HiddenVector, Data)    
