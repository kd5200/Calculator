import numpy as np 


def calculate(list):
 if len(list) !=9 :
  raise ValueError('List must contain nine numbers')
  print(list)  
  
  a = np.array([0,1,2,3,4,5,6,7,8]).reshape((3,3))

  mean = [np.mean(a, axis=0), np.mean(a, axis=1),np.mean(a)]

  var = [np.var(a, axis=0), np.var(a, axis=1), np.var(a)]

  std = [np.std(a, axis=0), np.std(a, axis=1), np.std(a)]

  max = [np.max(a, axis=0), np.max(a, axis=1),np.max(a)]

  min = [np.min(a, axis=0), np.min(a, axis=1), np.min(a)]

  sum = [np.sum(a, axis=0), np.sum(a, axis=1), np.sum(a)]

  k = {
   "mean": mean,
   "variance": var,
   "standard deviation": std,
   "max": max,
   "min": min,
   "sum": sum
   }
  
  print(k)
